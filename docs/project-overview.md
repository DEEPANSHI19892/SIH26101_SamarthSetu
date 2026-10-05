# Project Overview

## 1. Introduction

Samarth Setu is an AI-enabled learning and competency platform designed
for officials associated with India's Official Statistical System.

The platform follows a competency-based learning approach rather than
presenting learners with only a generic list of courses.

The central idea is:

> **Understand the learner → measure competencies → identify gaps →
> recommend learning → assess learning → update progress.**

## 2. Problem Statement

SIH26101 asks for an AI-enabled learning platform that can identify
competency gaps, recommend personalized training through the iGOT
Karmayogi ecosystem, and generate quizzes/MCQs from uploaded learning
materials.

## 3. Objectives

The project aims to:

1.  Build a structured learner competency profile.
2.  Assess selected technical and statistical competencies.
3.  Identify weak and strong competency areas.
4.  Recommend relevant learning resources.
5.  Generate MCQs from trainer-provided material.
6.  Evaluate learner performance.
7.  Track competency and learning progress.

## 4. Target Users

### Official / Learner

Uses the platform to: - create a profile, - complete assessments, - view
skill gaps, - follow recommendations, - attempt quizzes, - monitor
progress.

### Trainer

Uses the platform to: - provide learning material, - generate assessment
questions, - review generated content, - support learner assessment.

### Administrator

Can be extended to: - monitor competency distribution, - view learning
activity, - analyze training effectiveness, - manage users and learning
resources.

## 5. Core Learning Loop

``` text
Learner Profile
      ↓
Competency Assessment
      ↓
Skill-Gap Analysis
      ↓
Learning Recommendation
      ↓
Training / Study
      ↓
Quiz / Assessment
      ↓
Performance Feedback
      ↓
Progress Update
      ↓
Reassessment
```

## 6. Scope of the MVP

The MVP focuses on the core workflow needed to demonstrate competency
assessment, recommendations, AI-generated MCQs, quiz evaluation and
progress tracking.

Advanced government integrations, SSO and large-scale analytics are
treated as extension areas unless already implemented by the team.

## 7. Important Implementation Note

This document describes the intended MVP architecture and documented
project scope. Exact implementation details should be synchronized with
the source code before production deployment.
