from fastapi import FastAPI
from app.core.middleware import setup_cors, setup_access_log
from app.core.events import on_startup, on_shutdown
from app.routers.user import query, pest, irrigation, market
from app.routers.admin import ops as admin_ops
from app.routers import ws
from app.config.settings import settings

app = FastAPI(title=settings.app_name, version="0.1.0")

# Middleware
setup_cors(app)
setup_access_log(app)

# Lifespan hooks (stubs for now)
app.add_event_handler("startup", on_startup)
app.add_event_handler("shutdown", on_shutdown)

# Routers
app.include_router(query.router, prefix="/api/v1", tags=["query"])
app.include_router(pest.router, prefix="/api/v1", tags=["pest"])
app.include_router(irrigation.router, prefix="/api/v1", tags=["irrigation"])
app.include_router(market.router, prefix="/api/v1", tags=["market"])
app.include_router(admin_ops.router, prefix="/api/v1/admin", tags=["admin"])
app.include_router(ws.router, tags=["ws"])  # /ws/live
