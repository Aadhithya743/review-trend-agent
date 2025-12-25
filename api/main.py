from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import os

app = FastAPI(
    title="Agentic AI Review Trend API",
    description="Backend API for review trend analysis",
    version="1.0"
)

TREND_FILE = "output/trend_report.csv"


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.get("/trends")
def get_trends():
    if not os.path.exists(TREND_FILE):
        return JSONResponse(
            status_code=404,
            content={"error": "Trend report not found"}
        )

    df = pd.read_csv(TREND_FILE)
    return df.to_dict(orient="records")
