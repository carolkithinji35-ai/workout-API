from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import models before registering routes so SQLAlchemy knows about every table.
from models import Exercise, Workout, WorkoutExercise
from routes.exercise_routes import exercise_bp
from routes.workout_exercise_routes import workout_exercise_bp
from routes.workout_routes import workout_bp

app.register_blueprint(workout_bp)
app.register_blueprint(exercise_bp)
app.register_blueprint(workout_exercise_bp)


@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify({"errors": error.messages}), 400


@app.errorhandler(ValueError)
def handle_value_error(error):
    return jsonify({"error": str(error)}), 400


@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    db.session.rollback()
    return jsonify({"error": "This record violates a database constraint."}), 409


@app.route("/")
def home():
    return {"message": "Welcome to the Workout API. It working!"}


if __name__ == "__main__":
    app.run(debug=True, port=5555)
