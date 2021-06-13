from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
import re

app = Flask(__name__)
api = Api(app)

DATA = { 
 "version": "v1", 
          "results": 
         [ 
             "Machine1 had 0 attempt(s)",
         
             "Machine2 had 0 attempt(s)",
         
             "Machine3 had 0 attempt(s)"
         ]
    
}


class Places(Resource):
    def get(self):
        # return our data and 200 OK HTTP code
        return {'data': DATA}, 200

    def post(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('m-location', required=True)
        args = parser.parse_args()
        DATA['results'].append(args['m-location'])
        return {'data': DATA}, 200

    def put(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('m-location')
        args = parser.parse_args()        
        if re.match("Machine1.*", args['m-location']):
            DATA['results'][0] = args['m-location']
        if re.match("Machine2.*", args['m-location']):
            DATA['results'][1] = args['m-location']
        if re.match("Machine3.*", args['m-location']):
            DATA['results'][2] = args['m-location']
        return {'data': DATA}, 200 



api.add_resource(Places, '/v1')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8082)))
