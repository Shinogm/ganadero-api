from fastapi import HTTPException
from app.services.db import ganaderia_db

async def get_all_workers():
    try:
        workers_db = ganaderia_db.fetch_all(
            sql='SELECT * FROM users'
        )

        return {
            'status': 'success',
            'message': 'Workers fetched successfully',
            'workers': workers_db
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener trabajadores')
    
async def get_one_worker(worker_id: int):
    try:
        worker_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(worker_id,)
        )

        return {
            'status': 'success',
            'message': 'Worker fetched successfully',
            'id': worker_id,
            'worker': worker_db
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener trabajador')