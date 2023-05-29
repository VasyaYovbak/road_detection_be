from flask_restx import fields
from config import api

video_request_model = api.model('Country_Demo', {
    '': fields.String('Ukraine'),
    'official_language': fields.String('Ukrainian'),
    'population': fields.Integer(45000000),
    'details': fields.String('details')
})
