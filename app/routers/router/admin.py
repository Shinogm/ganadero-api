from fastapi import APIRouter
from app.routers.controllers.admin import create, get, modify, delete
from app.utils.login import verify_password

router = APIRouter(prefix='/admin', tags=['admin'])

router.post('/create')(create.create_admin)
router.post('/login')(verify_password)
router.get('/get')(get.get_all_admins)
router.get('/get/admin/{admin_id}')(get.get_one_admin)
router.put('/modify/{admin_id}')(modify.modify_admin)
router.delete('/delete/{admin_id}')(delete.delete_admin)

