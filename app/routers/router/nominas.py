from fastapi import APIRouter
from app.routers.controllers.worker.functions import nominas

router = APIRouter(prefix='/nominas', tags=['nominas'])

router.post('/worker/nomina/{worker_id}')(nominas.create_nomina)
router.get('/worker/nomina/{worker_id}')(nominas.get_nomina)
router.get('/worker/nomina/one/{nomina_id}')(nominas.get_nomina_one)
router.get('/worker/nominas/all')(nominas.get_all_nominas)
router.delete('/worker/nomina/{nomina_id}')(nominas.delete_nomina)