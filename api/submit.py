import polars as pl
from os.path import join, exists
from flask import Flask, request

app = Flask('vyvy-art-club')


@app.route('/api/submit', methods=['POST'])
def submit():
    try:
        if request.is_json:
            data = request.get_json()
            keys = ['name', 'grade', 'school', 'email', 'ig_handle', 'referee', 'description']
            if type(data) is dict and all(key in data for key in keys) and all(type(value) is str for value in data.values()) and all(value.strip() != '' for value in data.values()):
                new_data = {key: data[key] for key in keys}
                if exists(join('data', 'data.csv')):
                    df = pl.read_csv(join('data', 'data.csv'), schema_overrides={'grade': str})
                    df = pl.concat([df, pl.DataFrame(new_data)])
                else:
                    df = pl.DataFrame(new_data)
                print(df)
                df.write_csv(join('data', 'data.csv'))
                return "Submitted", 200

        return "Bad Request", 400
    except Exception as e:
        print(e)

    return "Internal Server Error", 500

