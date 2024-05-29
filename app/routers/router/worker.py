from fastapi import APIRouter
from app.routers.controllers.worker import create, get, modify, delete

router = APIRouter(prefix='/worker', tags=['worker'])

router.post('/create')(create.create_worker)
router.get('/get')(get.get_all_workers)
router.get('/get/worker/{worker_id}')(get.get_one_worker)
router.put('/modify/{worker_id}')(modify.modify_worker)
router.delete('/delete/{worker_id}')(delete.delete_worker)