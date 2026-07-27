from marshmallow import Schema, fields, validates, ValidationError


class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)

    sets = fields.Int(required=True)
    reps = fields.Int(required=True)
    duration = fields.Int()

    exercise = fields.Nested(
        "ExerciseSchema",
        only=("id", "name")
    )

    @validates("sets")
    def validate_sets(self, value, **kwargs):
        if value <= 0:
            raise ValidationError("Sets must be greater than zero.")


@validates("reps")
def validate_reps(self, value, **kwargs):
    if value <= 0:
        raise ValidationError("Reps must be greater than zero.")


@validates("duration")
def validate_duration(self, value, **kwargs):
    if value is not None and value <= 0:
        raise ValidationError("Duration must be greater than zero.")

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(required=True)

    exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True
    )

    @validates("name")
    def validate_name(self, value, **kwargs):
        if len(value.strip()) < 3:
            raise ValidationError(
                "Workout name must be at least 3 characters long."
            )


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(required=True)
    description = fields.Str(required=True)

    workouts = fields.Nested(
        WorkoutExerciseSchema,
        many=True,
        exclude=("exercise",)
    )

    @validates("name")
    def validate_name(self, value, **kwargs):
        if len(value.strip()) < 3:
            raise ValidationError(
                "Exercise name must be at least 3 characters long."
            )

    @validates("description")
    def validate_description(self, value, **kwargs):
        if len(value.strip()) < 10:
            raise ValidationError(
                "Description must be at least 10 characters long."
            )


workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)

