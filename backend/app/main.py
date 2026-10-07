from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .routes.health import router as health_router
from .routes.analysis import router as analysis_router

# Initialize FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Backend API for Decision Arena — Autonomous Multi-Agent Consensus Platform",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Exception handler for clean, user-friendly validation error messages
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    first_error = errors[0] if errors else {}
    msg = first_error.get("msg", "Validation error occurred.")
    if msg.startswith("Value error, "):
        msg = msg[len("Value error, "):]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": msg},
    )

# Configure CORS Middleware for React frontend (supports all local dev ports & hostnames)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_origin_regex=r"^https?://.*$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root Welcome Endpoint
@app.get("/", summary="Root Endpoint")
async def root():
    return {
        "message": "Welcome to Decision Arena API",
        "docs": "/docs",
        "health": f"{settings.API_PREFIX}/health",
    }

# Register Routers under /api prefix
app.include_router(health_router, prefix=settings.API_PREFIX)
app.include_router(analysis_router, prefix=settings.API_PREFIX)
