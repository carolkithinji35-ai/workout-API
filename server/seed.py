from app import app, db
from models import Exercise, Workout, WorkoutExercise


with app.app_context():
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    strength = Workout(name="Full Body Strength")
    cardio = Workout(name="Quick Cardio")
    squat = Exercise(
        name="Bodyweight Squat",
        description="A lower-body exercise that builds leg strength.",
    )
    plank = Exercise(
        name="Plank",
        description="A core exercise performed while holding a stable position.",
    )
    db.session.add_all([strength, cardio, squat, plank])
    db.session.flush()

    db.session.add_all([
        WorkoutExercise(workout_id=strength.id, exercise_id=squat.id, sets=3, reps=12),
        WorkoutExercise(workout_id=cardio.id, exercise_id=plank.id, sets=3, reps=1, duration=45),
    ])
    db.session.commit()
    print("Database seeded.")
