from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def all_tasks(): ...

@router.get("/task_id")
async def task_by_id(): ...

@router.post("/create")
async def create_task(): ...

@router.put("/update")
async def update_task(): ...

@router.delete("/delete")
async def delete_task(): ...