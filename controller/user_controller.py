
import logging

from fastapi import APIRouter
from fastapi import HTTPException

from model.response.user_response_model import UserResponseModel
from model.response.user_response_model import User as SingleUserResponse
from model.response.user_response_model import UserResponseDeletedModel
from model.request.user_request_model import UserRequestModel
from model.request.user_request_model import UserRequestUpdateModel

from service.user_service import get_users
from service.user_service import add_user
from service.user_service import get_user_by_id
from service.user_service import update_user
from service.user_service import delete_user

from config import get_db_connection


# Setup logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


user_router = APIRouter()

@user_router.get("/v1/users/", response_model=UserResponseModel, response_model_exclude_none=True)
async def get_all_users():
    try:
        user_response = get_users()
        validated_response = UserResponseModel(**user_response)
        return validated_response
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail="Invalid user response")
    
@user_router.post("/v1/users/", response_model=SingleUserResponse, response_model_exclude_none=True)
async def add_user_in_memory(request: UserRequestModel):
    logger.debug(f"Received request: {request}")
    user_added = add_user(request)
    return user_added

@user_router.get("/v1/user/{user_id}")
async def get_user_by_user_id(user_id: int):
    logger.debug(f"Received request: {user_id}")
    return get_user_by_id(user_id)

@user_router.put("/user/{user_id}", response_model=UserResponseModel, response_model_exclude_none=True)
async def update_user_by_id(request: UserRequestUpdateModel, user_id: int):
    logger.debug(f"Received request: {request}")
    user_updated = update_user(request, user_id)
    return user_updated

@user_router.delete("/user/{user_id}", response_model=UserResponseDeletedModel)
async def delete_user_by_id(user_id: int):
    logger.debug(f"Request received: {user_id}")
    return delete_user(user_id)
    
