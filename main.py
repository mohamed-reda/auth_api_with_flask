from flask import Flask, request

from flask_restful import Resource, Api, reqparse
# the Resource is something that the API will return

from flask_jwt import JWT, jwt_required

from auth.security import authenticate, identity

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

items = [
    {
        "name": "Piano",
        "price": "20"
    }
]


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
        # return {'item': next(filter(lambda x: x['name'] == name, items), None)}

    def post(self, name):
        # data = request.get_json(silent=True)
        data = Item.parser.parse_args()
        if next(filter(lambda x: x['name'] == data['name'], items), None) is not None:
            name = data['name']
            return {'message': f'An item with name {name} already exists.'}, 404
        item = {'name': str(data['name']), 'price': str(data['price'])}
        items.append(item)
        return item, 201

    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    # @jwt_required()
    def put(self, name):
        # data = request.get_json()
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


# the best practice of Flask Resources,this is getting access to the API on Items
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

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
