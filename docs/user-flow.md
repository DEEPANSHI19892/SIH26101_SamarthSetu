# User Flow

## End-to-End Learner Flow

### Step 1 --- Home

The official opens Samarth Setu and selects **Get Started / Login**.

### Step 2 --- Login

The official enters credentials and accesses the platform.

### Step 3 --- Create Profile

The official provides: - designation, - department, - job role, -
experience, - education, - previous training.

### Step 4 --- Competency Assessment

The official completes questions covering selected competencies.

### Step 5 --- Skill-Gap Analysis

The system processes assessment results and classifies competencies into
levels such as: - Low gap / strong competency - Medium gap - High gap /
development required

### Step 6 --- Personalized Recommendations

The system maps identified gaps to relevant learning resources.

### Step 7 --- Learning

The official follows the recommended training or learning material.

### Step 8 --- Trainer Assessment

A trainer can upload learning content for assessment generation.

### Step 9 --- AI MCQ Generation

The AI generates questions, options, answers and explanations from the
provided material.

### Step 10 --- Quiz Attempt

The official attempts the generated quiz.

### Step 11 --- Result

The platform calculates the score and displays feedback.

### Step 12 --- Progress Update

The learner's progress is updated so future recommendations can consider
the latest performance.

## Flow Diagram

``` text
┌──────────┐
│   Home   │
└────┬─────┘
     ↓
┌──────────┐
│  Login   │
└────┬─────┘
     ↓
┌──────────┐
│ Profile  │
└────┬─────┘
     ↓
┌──────────────┐
│  Assessment  │
└──────┬───────┘
       ↓
┌──────────────┐
│ Skill Gaps   │
└──────┬───────┘
       ↓
┌────────────────────┐
│ Recommendations    │
└─────────┬──────────┘
          ↓
     Learning
          ↓
┌────────────────────┐
│ AI Quiz Generation │
└─────────┬──────────┘
          ↓
┌────────────────────┐
│ Quiz + Evaluation  │
└─────────┬──────────┘
          ↓
┌────────────────────┐
│ Progress Updated   │
└────────────────────┘
```
