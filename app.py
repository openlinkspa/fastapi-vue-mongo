from fastapi import FastAPI
from routes.testHolder import testHolder
from docs import tags_metadata

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    title="SPED-API Test (Fastapi/Vue/Mongodb)",
    description="This is a test REST API.",
    version="v1",
    docs_url="/",
    openapi_tags=tags_metadata
)

app.include_router(testHolder)
