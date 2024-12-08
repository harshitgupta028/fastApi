from fastapi import FastAPI
from fastapi import HTTPException

from controller.user_controller import user_router
from controller.teacher_controller import teacher_router
from exception.user_exception_handler import http_exception

app = FastAPI()

# Exception handlers
app.add_exception_handler(HTTPException, http_exception)

# Endpoint routes
app.include_router(user_router)
app.include_router(teacher_router)
