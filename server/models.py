from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint, UniqueConstraint
from app import db


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    exercises = db.relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    @validates("name")
    def validate_name(self, key, value):
        if not value.strip():
            raise ValueError("Workout name cannot be empty.")
        return value


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)

    workouts = db.relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    @validates("name")
    def validate_name(self, key, value):
        if not value.strip():
            raise ValueError("Exercise name cannot be empty.")
        return value

    @validates("description")
    def validate_description(self, key, value):
        if len(value.strip()) < 10:
            raise ValueError(
                "Description must be at least 10 characters long.")
        return value


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    __table_args__ = (
        CheckConstraint('sets > 0', name='check_sets_positive'),
        CheckConstraint('reps > 0', name='check_reps_positive'),
        CheckConstraint('(duration IS NULL) OR (duration > 0)',
                        name='check_duration_positive'),
        UniqueConstraint('workout_id', 'exercise_id',
                         name='uq_workout_exercise'),
    )

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey(
        "workouts.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey(
        "exercises.id"), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=True)  # Duration in seconds

    workout = db.relationship("Workout", back_populates="exercises")
    exercise = db.relationship("Exercise", back_populates="workouts")

    @validates("sets", "reps", "duration")
    def validate_numbers(self, key, value):
        if value is not None and value <= 0:
            raise ValueError(f"{key.capitalize()} must be greater than zero.")
        return value
