import polars as pl
from os.path import join
from flask import Flask, request

app = Flask('vyvy-art-club')


@app.route('/api/submit', methods=['POST'])
def submit():
    if request.is_json:
        data = request.get_json()
        keys = ['name', 'grade', 'school', 'email', 'ig_handle', 'referee', 'description']
        if type(data) is dict and all(key in data for key in keys):
            new_data = {key: data[key] for key in keys}

            with open(join('data', 'file.txt'), 'a') as f:
                df = pl.DataFrame(new_data)
                df.write_csv(f, include_header=False)
            return "Submitted", 200

    return "Bad Request", 400