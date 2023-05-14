from flask import Flask, request
from flask_restful import Resource, Api
import json
from skills import Skills

app = Flask(__name__)
api = Api(app)

developers = [
    {"id": "0", "name": "Henrique", "skills": ["Python", "Flask"]},
    {"id": "1", "name": "Gisa", "Skills": ["Pyhton", "Django"]}
]


class Developers(Resource):

    def get(self, id):
        try:
            response = developers[id]
        except IndexError:
            message = f"developer with ID {id} doesn't exist"
            response = {"status": "error", "message": message}
        except Exception:
            message = "Unknowed error"
            response = {"status": "error", "message": message}
        return response

    def put(self, id):
        datas = json.loads(request.data)
        developers[id] = datas
        return datas

    def delete(self, id):
        developers.pop(id)
        return {"status": "deleted", "message": "the item was deleted"}


class ListDevelopers(Resource):
    def get(self):
        return developers

    def post(self):
        datas = json.loads(request.data)
        position = len(developers)
        datas["id"] = position
        developers.append(datas)
        return developers[position]


# rota w/ restful
api.add_resource(Developers, "/dev/<int:id>/")
api.add_resource(ListDevelopers, "/dev/")
api.add_resource(Skills, "/skills/")

if __name__ == '__main__':
    app.run(debug=True)