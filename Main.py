import flask
import flask_restful
import Generation
app = flask.Flask(__name__)
api = flask_restful.Api(app)

class Suggestions(flask_restful.Resource):
    def post(self):
        data = flask.request.get_json()
        try:
            recommendations = Generation.generate_recipe(data)
            return recommendations
        except Exception as e:
            flask_restful.abort(400)


api.add_resource(Suggestions, "/suggest")

if __name__ == "__main__":
    app.run(debug=True)