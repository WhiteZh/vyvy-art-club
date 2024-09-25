import csv
import io
from os import environ

from flask import Flask, request, Response
from psycopg2 import connect, Error

app = Flask('vyvy-art-club')


conn_params = {
    'dbname': environ['POSTGRES_DATABASE'],
    'user': environ['POSTGRES_USER'],
    'password': environ['POSTGRES_PASSWORD'],
    'host': environ['POSTGRES_HOST'],
}


@app.route('/api/retrieve', methods=['GET'])
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

        conn = connect(**conn_params)
        cur = conn.cursor()

        cur.execute("""SELECT * FROM submits""")

        rows = cur.fetchall()
        headers = [des[0] for des in cur.description]

        buf = io.StringIO()

        writer = csv.writer(buf)

        writer.writerow(headers)
        writer.writerows(rows)

        ret = buf.getvalue()

        buf.close()
        cur.close()
        conn.close()

        return Response(
            ret,
            mimetype='text/csv',
            headers={"Content-disposition": "attachment; filename=submits.csv"}
        ), 200
    except Exception as e:
        print(e)

    return "Internal Server Error", 500


if 'LDEV' in environ:
    app.run(debug=True)
