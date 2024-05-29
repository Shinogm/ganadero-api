from fastapi import APIRouter
from app.routers.controllers.worker.functions.trabajo import create_trabajo, status_finalizado, status_cancelado, get_tareas_pendientes, status_pendiente

router = APIRouter(prefix='/activities', tags=['activities'])

router.post('/worker/tareas/realizar/{worker_id}')(create_trabajo)
router.get('/worker/tareas/realizar/{worker_id}')(get_tareas_pendientes)
router.put('/worker/tareas/finalized/{id}')(status_finalizado)
router.put('/worker/tareas/cancel/{id}')(status_cancelado)
router.put('/worker/tareas/pendiente/{id}')(status_pendiente)