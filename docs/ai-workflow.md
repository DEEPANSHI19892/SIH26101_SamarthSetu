# AI Workflow

## 1. Purpose

AI is used to reduce manual effort in assessment and learning
personalization.

The two major AI-assisted workflows are:

1.  Competency / learning recommendation support
2.  Learning-material-to-MCQ generation

------------------------------------------------------------------------

## 2. MCQ Generation Workflow

``` text
Trainer
  │
  ▼
Upload Learning Material
  │
  ▼
Content Extraction
  │
  ▼
Clean / Chunk Content
  │
  ▼
Send Relevant Context to LLM
  │
  ▼
Generate:
  ├── Question
  ├── Option A
  ├── Option B
  ├── Option C
  ├── Option D
  ├── Correct Answer
  └── Explanation
  │
  ▼
Validate Output
  │
  ▼
Store / Present Quiz
```

## 3. Prompting Requirements

The generation prompt should clearly specify: - subject/topic, - number
of questions, - question type, - four options, - one correct answer, -
explanation, - difficulty if supported, - output format.

## 4. Grounding

Questions should be based on the uploaded learning material rather than
unrelated model knowledge.

A stronger production implementation should preserve the source passage
used to generate each question.

This makes trainer verification easier.

## 5. Skill-Gap Logic

A simple MVP approach can calculate a competency score from assessment
performance.

Example:

``` text
Competency Score = Correct Answers / Total Questions × 100
```

A configurable interpretation can then be applied:

``` text
0–49   → High development need
50–69  → Medium development need
70–100 → Lower development need
```

These thresholds are example MVP values and can be changed by the team.

## 6. Recommendation Logic

Example:

``` text
IF competency score is low
    → identify competency
    → find learning resources mapped to competency
    → assign high priority
ELSE IF score is medium
    → recommend reinforcement material
ELSE
    → recommend advanced / next-level material
```

## 7. AI Safety and Quality

Generated questions should be treated as AI-generated content and
reviewed before official/high-stakes use.

Quality checks should consider: - factual correctness, - relevance to
source material, - one unambiguous correct answer, - plausible
distractors, - clear explanation, - absence of unsupported information.

## 8. Important Limitation

The exact AI model, provider, prompt implementation and validation
pipeline should be documented from the actual backend configuration
before final production documentation.
