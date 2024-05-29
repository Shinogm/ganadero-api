from fastapi import HTTPException, Depends
from app.services.db import ganaderia_db
from app.models.worker import WorkerModel

async def create_worker(worker: WorkerModel = Depends(WorkerModel.as_form)):
    try:
        worker_id = ganaderia_db.execute(
            sql='INSERT INTO users (name, last_name, permissions_id) VALUES (%s, %s, 2)',
            params=(
                worker.name,
                worker.last_name
            )
        )

        get_worker = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(worker_id,)
        )
        
        return {
            'status': 'success',
            'message': 'Worker created successfully',
            'data': get_worker
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al crear trabajador')