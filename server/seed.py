from app import app, db
from models import Exercise, Workout, WorkoutExercise


with app.app_context():
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    strength = Workout(name="Full Body Strength")
    cardio = Workout(name="Quick Cardio")
    core = Workout(name="Core Focus")
    upper_body = Workout(name="Upper Body Workout")

    squat = Exercise(
        name="Bodyweight Squat",
        description="A lower-body exercise that builds leg strength.",
    )
    plank = Exercise(
        name="Plank",
        description="A core exercise performed while holding a stable position.",
    )
    push_up = Exercise(
        name="Push Up",
        description="An upper-body exercise that strengthens the chest and arms.",
    )
    jumping_jack = Exercise(
        name="Jumping Jack",
        description="A full-body cardio movement that raises the heart rate.",
    )
    lunge = Exercise(
        name="Forward Lunge",
        description="A lower-body exercise that builds balance and leg strength.",
    )
    db.session.add_all([
        strength,
        cardio,
        core,
        upper_body,
        squat,
        plank,
        push_up,
        jumping_jack,
        lunge,
    ])
    db.session.flush()

    db.session.add_all([
        WorkoutExercise(workout_id=strength.id, exercise_id=squat.id, sets=3, reps=12),
        WorkoutExercise(workout_id=strength.id, exercise_id=push_up.id, sets=3, reps=10),
        WorkoutExercise(workout_id=strength.id, exercise_id=lunge.id, sets=3, reps=10),
        WorkoutExercise(workout_id=cardio.id, exercise_id=jumping_jack.id, sets=4, reps=20),
        WorkoutExercise(workout_id=cardio.id, exercise_id=plank.id, sets=3, reps=1, duration=45),
        WorkoutExercise(workout_id=core.id, exercise_id=plank.id, sets=3, reps=1, duration=60),
        WorkoutExercise(workout_id=upper_body.id, exercise_id=push_up.id, sets=4, reps=12),
    ])
    db.session.commit()
    print("Database seeded.")
