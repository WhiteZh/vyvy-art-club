import json
from http.server import BaseHTTPRequestHandler
import polars as pl
from os.path import join


class handler(BaseHTTPRequestHandler):

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        try:
            json_data: dict = json.loads(post_data)

            keys = ['name', 'grade', 'school', 'email', 'ig_handle', 'referee', 'description']

            if type(json_data) != dict:
                raise BaseException('Invalid JSON')
            if not all(key in json_data for key in keys):
                raise BaseException('Invalid JSON')

            new_data = {key: json_data[key] for key in keys}

            with open(join('data', 'file.txt'), 'a') as f:
                df = pl.DataFrame(new_data)
                df.write_csv(f, include_header=False)
        except BaseException as e:
            self.send_error(400)
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))

        self.send_response(200)
        self.end_headers()

