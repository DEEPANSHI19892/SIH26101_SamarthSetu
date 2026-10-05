# Features

## 1. Home / Landing Page

The home page introduces Samarth Setu and provides access to the
platform.

Expected elements: - Project/platform name - Short description - Key
features - Get Started / Login action

## 2. Official Login

The MVP uses a simple authenticated login flow.

Expected inputs: - Email - Password

Authentication should return a secure session/token for authorized API
requests.

## 3. Learner Profile

The profile collects information useful for competency mapping.

Fields: - Name - Designation - Department - Job Role - Experience -
Education - Previous Training

## 4. Competency Assessment

The learner is assessed across selected competencies.

Example competencies: - Sampling - Statistical Analysis - Python - SQL -
Data Visualization - AI/ML

The assessment produces scores that are used by the skill-gap logic.

## 5. Skill-Gap Dashboard

The dashboard converts assessment results into understandable competency
information.

Example:

  Competency     Score Gap Level
  ------------ ------- -----------
  Python           40% High
  SQL              70% Medium
  Sampling         45% High
  AI/ML            30% High

The exact thresholds can be configured by the implementation.

## 6. Personalized Recommendations

Recommendations should contain: - Course / training name - Related
competency - Priority - Provider/source - Duration

The recommendation engine should use the learner's identified gaps as
the main input.

## 7. AI MCQ Generator

A trainer uploads learning material.

The AI processing flow is:

``` text
Learning Material
      ↓
Text / Content Extraction
      ↓
Relevant Content Identification
      ↓
LLM Prompt / Question Generation
      ↓
MCQ + Options + Correct Answer + Explanation
      ↓
Trainer Review
```

For reliable use, generated questions should be reviewed before
high-stakes assessment.

## 8. Quiz

The learner receives: - Question - Four options - Submit action

## 9. Result

The result page can show: - Total score - Correct answers - Weak
competency/area - Explanations - Recommended revision

Example:

**Score:** 80%\
**Correct:** 8/10\
**Weak Area:** Sampling\
**Suggested Action:** Revise Sampling Methods

## 10. Progress Dashboard

Progress can include: - previous competency score, - current competency
score, - learning activity, - quiz average, - improvement over time.

## 11. Administrator Dashboard

Future/extended capability: - organization-wide competency
distribution, - training participation, - learning hours, - course
effectiveness, - emerging skill requirements, - competency trends.

## 12. iGOT Integration

The platform is designed so that a recommendation layer can connect with
approved iGOT services.

Do not describe the MVP as having live iGOT API integration unless the
team has verified and deployed that integration.
