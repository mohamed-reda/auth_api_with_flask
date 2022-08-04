from flask import Flask

from flask_restful import Resource, Api
# the Resource is something that the API will return

from flask_jwt import JWT, jwt_required

from auth.security import authenticate, identity
from auth.user import UserRegister
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

if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True

app.run(port=5000, debug=True)

# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('price',
#                         type=float,
#                         required=True,
#                         help="This field cannot be left blank!"
#                         )

#     @jwt_required()
#     def get(self, name):
#         return {'item': next(filter(lambda x: x['name'] == name, items), None)}
# 
#     def post(self, name):
#         if next(filter(lambda x: x['name'] == name, items), None) is not None:
#             return {'message': "An item with name '{}' already exists.".format(name)}
# 
#         data = Item.parser.parse_args()
# 
#         item = {'name': name, 'price': data['price']}
#         items.append(item)
#         return item
# 
#     @jwt_required()
#     def delete(self, name):
#         global items
#         items = list(filter(lambda x: x['name'] != name, items))
#         return {'message': 'Item deleted'}
# 
#     @jwt_required()
#     def put(self, name):
#         data = Item.parser.parse_args()
#         # Once again, print something not in the args to verify everything works
#         item = next(filter(lambda x: x['name'] == name, items), None)
#         if item is None:
#             item = {'name': name, 'price': data['price']}
#             items.append(item)
#         else:
#             item.update(data)
#         return item
# 
# 
# class ItemList(Resource):
#     def get(self):
#         return {'items': items}
