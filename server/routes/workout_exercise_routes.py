from flask import Blueprint, jsonify, request

from app import db
from models import Exercise, Workout, WorkoutExercise
from schemas import workout_exercise_schema


workout_exercise_bp = Blueprint("workout_exercises", __name__)


@workout_exercise_bp.post("/workouts/<int:workout_id>/exercises")
def add_exercise_to_workout(workout_id):
    Workout.query.get_or_404(workout_id)
    payload = request.get_json(silent=True) or {}
    payload["workout_id"] = workout_id
    data = workout_exercise_schema.load(payload)
    Exercise.query.get_or_404(data["exercise_id"])

    workout_exercise = WorkoutExercise(**data)
    db.session.add(workout_exercise)
    db.session.commit()
    return jsonify(workout_exercise_schema.dump(workout_exercise)), 201
