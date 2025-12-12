
# app/main.py
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse, JSONResponse
from typing import Dict

# Prometheus client for /metrics
# Install: pip install prometheus-client
from prometheus_client import Counter, Histogram, Gauge, CollectorRegistry, generate_latest, CONTENT_TYPE_LATEST
import time
import os

app = FastAPI(title="FastAPI CI/CD Service")

# -----------------------------
# Friendly home route
# -----------------------------
@app.get("/")
async def home() -> Dict[str, str]:
    return {
        "message": "FastAPI CI/CD service is running.",
        "docs": "/docs",
        "health": "/health",
        "metrics": "/metrics"
    }

# -----------------------------
# Health endpoint
# -----------------------------
# Returns a simple JSON indicating service liveness
@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}

# -----------------------------
# Basic Prometheus metrics
# -----------------------------
# Create a Registry to hold metrics (default global registry works too)
# Using the default global registry for simplicity here.
REQUEST_COUNT = Counter(
    "app_request_count",
    "Total HTTP requests",
    ["method", "endpoint", "http_status"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Latency of HTTP requests in seconds",
    ["endpoint"]
)

APP_INFO = Gauge(
    "app_info",
    "Static metadata about the app (version=label)",
    ["version"]
)

# Set an info gauge (use an env var for version if available)
APP_INFO.labels(version=os.getenv("APP_VERSION", "1.0.0")).set(1)


# Simple middleware to observe request count & latency
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    latency = time.perf_counter() - start

    endpoint_path = request.url.path
    REQUEST_LATENCY.labels(endpoint=endpoint_path).observe(latency)
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint_path,
        http_status=str(response.status_code)
    ).inc()

    return response


# Expose metrics in Prometheus text format
@app.get("/metrics")
def metrics():
    # Use the default collector registry
    data = generate_latest()
