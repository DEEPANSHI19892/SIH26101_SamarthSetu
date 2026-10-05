# Samarth Setu

## AI-Enabled Learning & Competency Platform for India's Official Statistical System

Samarth Setu is an AI-enabled learning and competency platform designed
for capacity building in India's Official Statistical System. The
platform focuses on identifying competency gaps, recommending relevant
learning opportunities, generating assessments from learning material,
and tracking learner progress.

> **Smart India Hackathon 2026 --- Problem Statement SIH26101**\
> Ministry of Statistics and Programme Implementation (MoSPI)\
> Department: Data Informatics & Innovation Division (DIID)\
> Theme: Smart Education

------------------------------------------------------------------------

## Problem

Officials working in the Official Statistical System need continuous
upskilling in statistical, technical and digital competencies. A large
learning catalogue can make it difficult to identify the training that
is most relevant to an individual's current role and skill gaps.

Samarth Setu addresses this through a competency-driven learning
workflow:

**Profile → Assess → Identify Gaps → Recommend → Learn → Quiz → Track
Progress**

------------------------------------------------------------------------

## Key Features

### 1. AI Competency Profiling

Creates a learner profile using information such as designation,
department, role, experience, education and previous training.

### 2. Competency Assessment

Assesses selected competencies such as: - Sampling - Statistical
Analysis - Python - SQL - Data Visualization - AI/ML

### 3. Skill-Gap Analysis

Assessment results are converted into competency levels and gap
categories so that weaker areas can be identified.

### 4. Personalized Recommendations

Learning recommendations are presented according to identified
competency gaps, priority and learning requirements.

### 5. AI MCQ & Quiz Generation

Trainers can provide learning material and generate objective questions
for assessment and self-evaluation.

### 6. Quiz Evaluation

Learners receive scores, correct/incorrect results and explanations
after attempting a quiz.

### 7. Progress Tracking

The learner can monitor competency improvement, quiz performance and
learning progress.

### 8. Dashboard-Based Experience

The platform is structured around learner information, competency
results, recommendations, assessments and progress.

------------------------------------------------------------------------

## MVP User Flow

``` text
Home
  ↓
Official Login
  ↓
Create Profile
  ↓
Competency Assessment
  ↓
Skill-Gap Analysis
  ↓
Personalized Recommendations
  ↓
Training / Learning
  ↓
Trainer Uploads Learning Material
  ↓
AI Generates MCQs
  ↓
Official Takes Quiz
  ↓
Score + Explanation
  ↓
Progress Updated
```

------------------------------------------------------------------------

## Project Structure

``` text
SIH26101_SamarthSetu/
│
├── backend/
│   └── Backend application and APIs
│
├── frontend/
│   └── User interface and client-side application
│
├── docs/
│   ├── project-overview.md
│   ├── features.md
│   ├── user-flow.md
│   ├── system-architecture.md
│   ├── ai-workflow.md
│   ├── database.md
│   ├── api-documentation.md
│   ├── setup-and-installation.md
│   ├── deployment.md
│   └── future-scope.md
│
├── .gitignore
├── LICENSE
└── README.md
```

------------------------------------------------------------------------

## Technology Stack

The MVP is organized around a modern web application architecture.

  Layer                 Technology / Approach
  --------------------- ------------------------------------------
  Frontend              React
  Backend               API-based backend
  Database              PostgreSQL
  Authentication        JWT-based authentication for MVP
  AI                    LLM-based competency/assessment features
  Version Control       Git + GitHub
  Frontend Deployment   Vercel
  Backend Deployment    Render
  Database Hosting      Neon PostgreSQL
  Monitoring            UptimeRobot

> Deployment/provider details should be updated if the team changes the
> production configuration.

------------------------------------------------------------------------

## AI Workflow

The AI layer is used primarily for: 1. interpreting
competency/assessment information, 2. supporting skill-gap
identification, 3. generating personalized learning suggestions, 4.
generating MCQs and explanations from learning material.

The system should keep generated assessment content connected to the
uploaded learning material so trainers can review it before official
use.

------------------------------------------------------------------------

## iGOT Integration

The SIH problem statement calls for integration with the iGOT Karmayogi
ecosystem.

For the MVP, the architecture should keep the recommendation layer
integration-ready. Actual production integration depends on the
availability of approved APIs, authentication mechanisms, data contracts
and access permissions.

The platform can therefore demonstrate the recommendation workflow
without claiming that a live government API connection exists unless
such access has actually been provided.

------------------------------------------------------------------------

## Security Considerations

The platform should follow secure development practices including: -
authenticated access, - role-based authorization, - secure password
handling, - protected API endpoints, - input validation, - environment
variables for secrets, - HTTPS in deployment, - restricted database
access, - protection of learner information.

Government deployment should additionally follow the applicable
government cybersecurity and data-protection requirements.

------------------------------------------------------------------------

## Expected Benefits

-   More targeted competency development
-   Faster identification of learning gaps
-   Personalized training recommendations
-   Automated assessment generation
-   Immediate learner feedback
-   Continuous progress tracking
-   Better visibility of competency development

------------------------------------------------------------------------

## Future Scope

-   Live iGOT Karmayogi API integration
-   SSO integration
-   Broader official-statistics competency framework
-   Multilingual learning support
-   Advanced adaptive assessments
-   Administrator analytics
-   Competency trend analysis
-   Course completion synchronization
-   AI learning assistant
-   Source-grounded MCQ validation
-   Role-specific learning pathways

------------------------------------------------------------------------

## Team

**Project:** Samarth Setu\
**Problem Statement:** SIH26101\
**Organization:** Ministry of Statistics and Programme Implementation
(MoSPI)

Add team member names, roles and institution details here before final
submission.

------------------------------------------------------------------------

## License

This project is released under the license included in this repository.
