from flask import Blueprint, jsonify, request

from app import db
from models import Workout
from schemas import workout_schema, workouts_schema


workout_bp = Blueprint("workouts", __name__, url_prefix="/workouts")


@workout_bp.get("")
def get_workouts():
    return jsonify(workouts_schema.dump(Workout.query.all())), 200


@workout_bp.post("")
def create_workout():
    data = workout_schema.load(request.get_json(silent=True) or {})
    workout = Workout(name=data["name"])
    db.session.add(workout)
    db.session.commit()
    return jsonify(workout_schema.dump(workout)), 201


@workout_bp.get("/<int:workout_id>")
def get_workout(workout_id):
    workout = db.get_or_404(Workout, workout_id)
    return jsonify(workout_schema.dump(workout)), 200


@workout_bp.delete("/<int:workout_id>")
def delete_workout(workout_id):
    workout = db.get_or_404(Workout, workout_id)
    db.session.delete(workout)
    db.session.commit()
    return "", 204
