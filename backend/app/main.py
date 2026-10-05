from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import auth, profile, competency, recommendation, quiz, progress, dashboard
from secure import Secure
from secure.middleware import SecureASGIMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI(title="Samarth Setu API", version="1.0.0")

# ✅ 1. CORS first (outer layer)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL, "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ 2. Security headers (inner layer)
secure_headers = Secure.with_default_headers()
app.add_middleware(SecureASGIMiddleware, secure=secure_headers)

# ✅ 3. Rate limiter
limiter = Limiter(key_func=get_remote_address, default_limits=["100/minute"])
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ✅ 4. Routers
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(competency.router)
app.include_router(recommendation.router)
app.include_router(quiz.router)
app.include_router(progress.router)
app.include_router(dashboard.router)

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "samarth-setu"}