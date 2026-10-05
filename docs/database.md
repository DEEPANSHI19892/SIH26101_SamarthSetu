# Database Design

## 1. Database

The planned MVP database is PostgreSQL.

## 2. Core Entities

### Users

Stores authentication and basic user information.

Suggested fields: - id - name - email - password_hash - role -
created_at - updated_at

### Profiles

Stores professional and educational information.

Suggested fields: - id - user_id - designation - department - job_role -
experience - education - previous_training

### Competencies

Stores competency definitions.

Suggested fields: - id - name - category - description - target_level

### Assessments

Stores assessment metadata.

Suggested fields: - id - user_id - competency_id - total_questions -
score - completed_at

### Questions

Stores assessment questions where persistence is required.

Suggested fields: - id - assessment_id - question_text - option_a -
option_b - option_c - option_d - correct_option - explanation -
source_reference

### Recommendations

Stores recommended learning resources.

Suggested fields: - id - user_id - competency_id - title - provider -
priority - duration - source_url

### Quiz Attempts

Stores learner quiz performance.

Suggested fields: - id - user_id - quiz_id - score - total_questions -
attempted_at

### Progress

Stores competency and learning progress.

Suggested fields: - id - user_id - competency_id - previous_score -
current_score - progress_percentage - updated_at

------------------------------------------------------------------------

## 3. Relationship Overview

``` text
User
 ├── Profile
 ├── Assessments
 │     └── Questions
 ├── Recommendations
 ├── Quiz Attempts
 └── Progress

Competency
 ├── Assessments
 ├── Recommendations
 └── Progress
```

## 4. Data Integrity

Recommended practices: - primary keys for every entity, - foreign keys
for relationships, - unique email constraint, - timestamps, - validation
at API level, - parameterized database queries, - indexes on frequently
searched fields.

## 5. Privacy

Only collect information required for the platform's functionality.

Production deployment should follow applicable government security and
privacy requirements.
