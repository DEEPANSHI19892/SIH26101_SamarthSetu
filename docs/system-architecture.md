# System Architecture

## 1. High-Level Architecture

Samarth Setu follows a frontend-backend-database architecture with an AI
service layer.

``` text
                    ┌─────────────────────┐
                    │       User          │
                    │ Official / Trainer  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Frontend       │
                    │       React         │
                    └──────────┬──────────┘
                               │ HTTPS / API
                               ▼
                    ┌─────────────────────┐
                    │       Backend       │
                    │   REST/API Layer    │
                    └──────┬───────┬──────┘
                           │       │
              ┌────────────┘       └─────────────┐
              ▼                                  ▼
     ┌─────────────────┐                ┌─────────────────┐
     │   PostgreSQL    │                │    AI / LLM     │
     │    Database     │                │     Services    │
     └─────────────────┘                └────────┬────────┘
                                                 │
                                                 ▼
                                      ┌────────────────────┐
                                      │ Quiz / Recommendation│
                                      │     Processing      │
                                      └────────────────────┘
```

## 2. Frontend Layer

Responsibilities: - display pages, - collect user input, - show
competency results, - display recommendations, - present quizzes, -
display progress, - communicate with backend APIs.

## 3. Backend Layer

Responsibilities: - authentication, - user/profile management, -
competency calculations, - recommendation logic, - quiz generation
requests, - quiz evaluation, - progress updates, - database
communication.

## 4. Database Layer

PostgreSQL stores structured application information such as: - users, -
profiles, - competencies, - assessment results, - recommendations, -
quizzes, - quiz attempts, - progress.

## 5. AI Layer

The AI layer can support: - natural-language processing of learning
material, - MCQ generation, - explanations, - recommendation
assistance, - competency interpretation where applicable.

## 6. External Integration Layer

The architecture can expose an integration layer for approved external
services such as iGOT Karmayogi.

A production integration requires: - approved API access, -
authentication, - API contracts, - data mapping, - error handling, -
secure data exchange.

## 7. Security Boundary

Sensitive operations should remain behind the backend.

The frontend should never contain: - database credentials, - private API
keys, - secret tokens, - service credentials.

Secrets should be stored in environment variables on the
server/deployment platform.
