from os import environ

from flask import Flask, request
from psycopg2 import connect, Error

app = Flask('vyvy-art-club')


conn_params = {
    'dbname': environ['DBNAME'],
    'user': environ['DBUSER'],
    'password': environ['DBPW'],
    'host': environ['DBHOST'],
}


@app.route('/api/submit', methods=['POST'])
def submit():
    try:
        print({
            "method": request.method,  # HTTP method (e.g., GET, POST)
            "host": request.host,  # Host (including port if present)
            "url": request.url,  # Full URL of the request
            "path": request.path,  # Path of the request
            "full_path": request.full_path,  # Full path with query string
            "headers": dict(request.headers),  # Request headers (converted to a dictionary)
            "remote_addr": request.remote_addr,  # Client IP address
            "user_agent": str(request.user_agent),  # User-Agent string
            "data": request.get_data(as_text=True)  # Request body (as string)
        })
        if request.is_json:
            data = request.get_json()
            keys = ['name', 'grade', 'school', 'email', 'ig_handle', 'referee', 'description']
            if type(data) is dict and all(key in data for key in keys) and all(type(value) is str for value in data.values()) and all(value.strip() != '' for value in data.values()):
                try:
                    conn = connect(**conn_params)
                    cur = conn.cursor()
                    cur.execute("""INSERT INTO submits (name, grade, school, email, ig_handle, referee, description)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);""", [data[key] for key in keys])
                    conn.commit()
                    conn.close()
                except Error as e:
                    print(e)
                    return "Bad Request", 400
                return "Submitted", 200

        return "Bad Request", 400
    except Exception as e:
        print(e)

    return "Internal Server Error", 500


if environ['LDEV']:
    app.run(debug=True)
