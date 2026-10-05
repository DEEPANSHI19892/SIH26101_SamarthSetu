# Setup and Installation

## Prerequisites

Install: - Git - Node.js - npm - PostgreSQL or access to a hosted
PostgreSQL database

If the backend uses a different runtime, follow the backend's
`requirements.txt` or package configuration.

------------------------------------------------------------------------

## 1. Clone the Repository

``` bash
git clone <REPOSITORY_URL>
cd SIH26101_SamarthSetu
```

------------------------------------------------------------------------

## 2. Frontend Setup

``` bash
cd frontend
npm install
npm run dev
```

The development server URL depends on the frontend configuration.

------------------------------------------------------------------------

## 3. Backend Setup

Open a second terminal:

``` bash
cd backend
```

Install backend dependencies according to the backend project
configuration.

If the project uses Python:

``` bash
pip install -r requirements.txt
```

Start the backend using the command defined by the project.

------------------------------------------------------------------------

## 4. Environment Variables

Do not commit secrets.

Typical variables may include:

``` env
DATABASE_URL=
JWT_SECRET=
AI_API_KEY=
FRONTEND_URL=
```

Use the exact variable names required by the current code.

------------------------------------------------------------------------

## 5. Database

Create/configure the PostgreSQL database and set the connection string
in the backend environment.

Run any migration or initialization command required by the backend.

------------------------------------------------------------------------

## 6. Verify the Application

Check:

1.  Frontend loads.
2.  Login works.
3.  Profile can be created.
4.  Assessment can be submitted.
5.  Skill-gap results appear.
6.  Recommendations load.
7.  Quiz generation works.
8.  Quiz submission works.
9.  Progress updates.

------------------------------------------------------------------------

## Troubleshooting

### Frontend cannot connect to backend

Check: - backend is running, - API base URL, - CORS configuration, -
frontend environment variables.

### Database connection fails

Check: - database URL, - credentials, - network access, - database
availability.

### AI generation fails

Check: - API key, - model/provider availability, - request format, -
backend logs, - rate limits.

### Authentication fails

Check: - JWT secret, - token storage, - token expiration, -
Authorization header.
