# Deployment

## Deployment Architecture

``` text
GitHub Repository
       │
       ├──────────────► Vercel
       │                  │
       │                  ▼
       │             Frontend
       │
       └──────────────► Render
                          │
                          ▼
                       Backend
                          │
                          ▼
                    Neon PostgreSQL
```

## Frontend --- Vercel

Typical deployment steps:

1.  Connect GitHub repository.
2.  Select the frontend directory if required.
3.  Configure build settings.
4.  Add frontend environment variables.
5.  Deploy.
6.  Verify API connectivity.

## Backend --- Render

Typical steps:

1.  Connect the GitHub repository.
2.  Select the backend service.
3.  Configure build/start commands.
4.  Add environment variables.
5.  Deploy.
6.  Test API endpoints.

## Database --- Neon PostgreSQL

Configure: - database, - connection string, - allowed access, - required
schema/migrations.

Never expose the database connection string to the frontend.

## Monitoring

A monitoring service such as UptimeRobot can periodically check the
deployed application/API.

## Production Checklist

-   [ ] HTTPS enabled
-   [ ] Secrets stored as environment variables
-   [ ] Debug mode disabled
-   [ ] CORS restricted
-   [ ] Database secured
-   [ ] Authentication tested
-   [ ] Error handling tested
-   [ ] AI API limits reviewed
-   [ ] File upload validation enabled
-   [ ] Logs reviewed
-   [ ] Backup/recovery plan considered
