from fastapi import APIRouter
from app.routers.controllers.worker.functions.horas import worker_horas, asistencia_worker, asistencia_worker_all_in_this_week

router = APIRouter(prefix='/horario', tags=['horario'])

router.post('/create')(worker_horas)
router.post('/asistencia')(asistencia_worker)
router.get('/asistencia')(asistencia_worker_all_in_this_week)
