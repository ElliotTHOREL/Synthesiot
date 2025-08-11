from .files import router as files_router
from .analyzer import router as analyzer_router

all_routers = [
    (files_router,"/files"),
    (analyzer_router,"/analyzer"),
]
