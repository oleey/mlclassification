
from . import api_bp as api

from flask import jsonify

@api.route('/test', methods=['GET'])

def test():
    
    response = {'message': 'success'}

    return jsonify(response)
