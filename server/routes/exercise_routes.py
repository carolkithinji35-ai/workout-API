from flask import Blueprint, jsonify, request

from app import db
from models import Exercise
from schemas import exercise_schema, exercises_schema


exercise_bp = Blueprint("exercises", __name__, url_prefix="/exercises")


@exercise_bp.get("")
def get_exercises():
    return jsonify(exercises_schema.dump(Exercise.query.all())), 200


@exercise_bp.post("")
def create_exercise():
    data = exercise_schema.load(request.get_json(silent=True) or {})
    exercise = Exercise(**data)
    db.session.add(exercise)
    db.session.commit()
    return jsonify(exercise_schema.dump(exercise)), 201


@exercise_bp.get("/<int:exercise_id>")
def get_exercise(exercise_id):
    exercise = db.get_or_404(Exercise, exercise_id)
    return jsonify(exercise_schema.dump(exercise)), 200


@exercise_bp.delete("/<int:exercise_id>")
def delete_exercise(exercise_id):
    exercise = db.get_or_404(Exercise, exercise_id)
    db.session.delete(exercise)
    db.session.commit()
    return "", 204
