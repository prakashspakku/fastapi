import logging
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from app.core.config import settings
from app.compute import compute_stats, prime_factors
from app import __version__

logging.basicConfig(level=getattr(logging, settings.log_level.upper(), logging.INFO), format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger(settings.app_name)

app = FastAPI(title=settings.app_name)

if settings.enable_metrics:
    try:
        from prometheus_fastapi_instrumentator import Instrumentator
        Instrumentator().instrument(app).expose(app)
    except Exception as e:
        logger.warning(f"Prometheus instrumentation failed: {e}")

class StatsRequest(BaseModel):
    values: List[float] = Field(..., description="List of numeric values")

class StatsResponse(BaseModel):
    count: float
    mean: float
    median: float
    stdev: float

class VersionResponse(BaseModel):
    app: str
    version: str
    env: str

@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}

@app.get("/version", response_model=VersionResponse)
async def version() -> VersionResponse:
    v: str = settings.version_override or __version__
    return VersionResponse(app=settings.app_name, version=v, env=settings.env)

@app.post("/compute/stats", response_model=StatsResponse)
async def stats(req: StatsRequest) -> StatsResponse:
    try:
        res = compute_stats(req.values)
        return StatsResponse(**res)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/compute/factors/{n}")
async def factors(n: int) -> dict:
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be non-negative")
    return {"n": n, "factors": prime_factors(n)}
