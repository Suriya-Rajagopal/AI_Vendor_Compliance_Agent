from fastapi import FastAPI
from app.api.routes import router
from app.api.vendor_routes import router as vendor_router
from app.api.compliance_routes import router as compliance_router
from app.api.dashboard_routes import router as dashboard_router


app = FastAPI(
    title="AI Vendor Compliance Agent",
    description=(
        "AI-powered vendor compliance system "
        "using Selenium, RAG, Gemini and SQLite."
    ),
    version="1.0.0"
)


app.include_router(router)
app.include_router(vendor_router)
app.include_router(compliance_router)
app.include_router(dashboard_router)


@app.get("/")
def health_check():

    return {
        "status": "running",
        "service": "AI Vendor Compliance Agent"
    }