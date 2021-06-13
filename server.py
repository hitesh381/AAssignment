from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
import re

app = Flask(__name__)
api = Api(app)



DATA2 = { 
 "version": "v2", 
          "results": 
         [ 
             "Machine1 - 0 time(s)",
         
             "Machine2 - 0 time(s)",
         
             "Machine3 - 0 time(s)"
         ]
    
}

class Places2(Resource):
    def get(self):
        # return our data and 200 OK HTTP code
        return {'data': DATA2}, 200

    def post(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('m-location', required=True)
        args = parser.parse_args()
        DATA2['results'].append(args['m-location'])
        return {'data': DATA2}, 200

    def put(self):
        # parse request arguments
        parser = reqparse.RequestParser()
        parser.add_argument('m-location')
        args = parser.parse_args()        
        if re.match("Machine1.*", args['m-location']):
            DATA2['results'][0] = args['m-location']
        if re.match("Machine2.*", args['m-location']):
            DATA2['results'][1] = args['m-location']
        if re.match("Machine3.*", args['m-location']):
            DATA2['results'][2] = args['m-location']
        return {'data': DATA2}, 200 



api.add_resource(Places2, '/v2')

if __name__ == '__main__':
    app.run(debug=True, host='10.14.24.69', port=int(os.environ.get('PORT', 8082)))
