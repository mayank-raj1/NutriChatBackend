import flask
import flask_restful
import Generation

# Create Flask application instance
app = flask.Flask(__name__)
api = flask_restful.Api(app)


# Define resource for handling suggestions
class Suggestions(flask_restful.Resource):
    def post(self):
        # Retrieve JSON data from the request
        data = flask.request.get_json()
        try:
            # Generate recipe recommendations based on input data
            recommendations = Generation.generate_recipe(data)
            return recommendations
        except Exception as e:
            # If an error occurs during generation, return HTTP 400 Bad Request
            flask_restful.abort(400)


# Add Suggestions resource to the API with route /suggest
api.add_resource(Suggestions, "/suggest")

# Run the Flask application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=False)
