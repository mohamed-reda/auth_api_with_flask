from flask import Flask, url_for

from flask_restful import Resource, Api
# the Resource is something that the API will return

from flask_jwt import JWT, jwt_required

from auth.security import authenticate, identity
from auth.user import UserRegister
from images.images import Images
from item import Item, ItemList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True  # To allow flask propagating exception even if debug is set to false on app

app.secret_key = 'Mohamed'
api = Api(app)


class Student(Resource):
    def get(self, name):
        return {'student': name}


# the best practice of Flask Resources,this is getting access to the API on Student
api.add_resource(Student, '/student/<string:name>')

jwt = JWT(app, authenticate, identity)

# the best practice of Flask Resources,this is getting access to the API on Items
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')

api.add_resource(Images, "/images")
if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True

app.run(port=5000, debug=True)

# @app.route()
# def images():
#     
#     # return url_for('resources', filename=f'/{path}', _external=True)
#     # generate_img(path)
#     # fullpath = "/resources/" + path
#     # resp = app.make_response(open(fullpath).read())
#     # resp.content_type = "image/jpg"
#     # return resp
#
