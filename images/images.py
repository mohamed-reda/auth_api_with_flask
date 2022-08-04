from flask import url_for
from flask_restful import Resource


class Images(Resource):

    def get(self):
        return url_for('static', filename='images/assets/img.jpg', _external=True)
        # return url_for('resources', filename='images/img.jpg', _external=True)
