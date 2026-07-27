# Workout API Backend

A Flask REST API for personal trainers to create workouts, manage reusable exercises, and assign exercises to workouts. Each assignment stores sets, reps, and an optional duration.

## Features

- Create, view, and delete workouts.
- Create, view, and delete reusable exercises.
- Add an existing exercise to a workout.
- Validate data at the schema, model, and database levels.

## Built with

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- SQLite

## Requirements

- Python 3.12
- Pipenv

## Installation

```bash
pipenv install
cd server
pipenv run flask --app app db upgrade
pipenv run python seed.py
```

## Run the application

From the `server` directory:

```bash
pipenv run flask --app app run --port 5555
```

## Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/workouts` | List all workouts. |
| POST | `/workouts` | Create a workout with a `name`. |
| GET | `/workouts/<id>` | View one workout and its exercises. |
| DELETE | `/workouts/<id>` | Delete a workout and its workout exercises. |
| GET | `/exercises` | List reusable exercises. |
| POST | `/exercises` | Create an exercise with `name` and `description`. |
| GET | `/exercises/<id>` | View one exercise and its workout assignments. |
| DELETE | `/exercises/<id>` | Delete an exercise and its workout assignments. |
| POST | `/workouts/<workout_id>/exercises` | Add an existing exercise using `exercise_id`, `sets`, `reps`, and optional `duration`. |

## Example requests

Create a workout:

```json
POST /workouts

{
  "name": "Full Body Strength"
}
```

Create an exercise:

```json
POST /exercises

{
  "name": "Bodyweight Squat",
  "description": "A lower-body exercise that builds leg strength."
}
```

Add an exercise to a workout:

```json
POST /workouts/1/exercises

{
  "exercise_id": 1,
  "sets": 3,
  "reps": 12,
  "duration": 45
}
```

## Validation

Workout and exercise names must contain text. Exercise descriptions must be at least 10 characters. Sets, reps, and durations must be positive numbers. A workout cannot contain the same exercise more than once.

## Author

Carol Kithinji
