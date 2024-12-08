from fastapi import APIRouter

teacher_router = APIRouter()

@teacher_router.get("/teachers/")
async def get_all_users():
    return [{"id": 1, "name": "Prabhat", "email": "Prabhat@gmail.com"}, {"id": 2, "name": "Gaurav", "email": "Gaurav@gmail.com"}]