
# # backend/app/core/middleware.py
# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# import time
# import uuid
# from app.utils.logger import log

# def setup_cors(app: FastAPI) -> None:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=["*"],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

# def setup_access_log(app: FastAPI) -> None:
#     @app.middleware("http")
#     async def add_request_id_and_log(request: Request, call_next):
#         # Get request ID from header or generate a new one
#         rid = request.headers.get("x-request-id") or str(uuid.uuid4())
#         start = time.time()
#         response = None
#         try:
#             response = await call_next(request)
#             return response
#         finally:
#             dur_ms = int((time.time() - start) * 1000)
#             status = getattr(response, "status_code", 0)
#             log.info(
#                 f"rid={rid} {request.method} {request.url.path} status={status} dur_ms={dur_ms}"
#             )


from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time, uuid
from app.utils.logger import log
from app.core.stats import stats

def setup_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def setup_access_log(app: FastAPI) -> None:
    @app.middleware("http")
    async def add_request_id_and_log(request: Request, call_next):
        rid = request.headers.get("x-request-id") or str(uuid.uuid4())
        start = time.time()
        status = 0
        try:
            response = await call_next(request)
            status = response.status_code
            return response
        finally:
            dur_ms = int((time.time() - start) * 1000)
            stats.requests_total += 1
            stats.last_request_ms = dur_ms
            if 200 <= status < 400:
                stats.requests_success += 1
            else:
                stats.requests_error += 1
            log.info(f"rid={rid} {request.method} {request.url.path} status={status} dur_ms={dur_ms}")
