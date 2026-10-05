# API Documentation

> This is an MVP API contract/template. Endpoint names should be
> synchronized with the actual backend routes before final submission.

## Authentication

### POST `/api/auth/register`

Creates a user account.

Request:

``` json
{
  "name": "Example User",
  "email": "user@example.com",
  "password": "********"
}
```

Response:

``` json
{
  "message": "User registered successfully"
}
```

### POST `/api/auth/login`

Authenticates a user.

Request:

``` json
{
  "email": "user@example.com",
  "password": "********"
}
```

Response:

``` json
{
  "token": "JWT_TOKEN",
  "user": {
    "id": 1,
    "name": "Example User",
    "role": "learner"
  }
}
```

------------------------------------------------------------------------

## Profile

### GET `/api/profile`

Returns the authenticated user's profile.

### PUT `/api/profile`

Updates profile information.

Example:

``` json
{
  "designation": "Statistical Officer",
  "department": "Example Department",
  "job_role": "Data Analyst",
  "experience": 3,
  "education": "M.Sc. Statistics"
}
```

------------------------------------------------------------------------

## Assessment

### GET `/api/competencies`

Returns available competencies.

### POST `/api/assessment`

Submits an assessment.

Example:

``` json
{
  "competency_id": 1,
  "answers": [
    {
      "question_id": 101,
      "answer": "B"
    }
  ]
}
```

Response:

``` json
{
  "score": 70,
  "gap_level": "medium"
}
```

------------------------------------------------------------------------

## Recommendations

### GET `/api/recommendations`

Returns recommendations based on the learner's competency profile.

Example response:

``` json
[
  {
    "title": "Introduction to SQL",
    "competency": "SQL",
    "priority": "High",
    "duration": "4 weeks"
  }
]
```

------------------------------------------------------------------------

## AI Quiz Generation

### POST `/api/quiz/generate`

Accepts learning material and requests MCQ generation.

The exact upload mechanism depends on the backend implementation.

Expected logical output:

``` json
{
  "questions": [
    {
      "question": "Example question?",
      "options": ["A", "B", "C", "D"],
      "correct_answer": "B",
      "explanation": "Explanation..."
    }
  ]
}
```

------------------------------------------------------------------------

## Quiz Evaluation

### POST `/api/quiz/submit`

Submits quiz answers.

Response:

``` json
{
  "score": 80,
  "correct": 8,
  "total": 10,
  "weak_area": "Sampling"
}
```

------------------------------------------------------------------------

## Progress

### GET `/api/progress`

Returns learner progress.

Example:

``` json
{
  "overall_progress": 68,
  "competencies": [
    {
      "name": "Python",
      "score": 60
    }
  ]
}
```

## API Security

Protected endpoints should require authentication.

Example:

``` text
Authorization: Bearer <JWT_TOKEN>
```

Never place API secrets directly in frontend source code.
