from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def all_users(): ...

@router.get("/user_id")
async def user_by_id(): ...

@router.post("/create")
async def create_user(): ...

@router.put("/update")
async def update_user(): ...

@router.delete("/delete")
async def delete_user(): ...