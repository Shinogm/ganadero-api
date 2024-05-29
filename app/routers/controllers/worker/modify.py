from fastapi import HTTPException, Depends
from app.services.db import ganaderia_db
from app.models.worker import WorkerModifyModel

async def modify_worker(worker_id: int, worker: WorkerModifyModel = Depends(WorkerModifyModel.as_form)):
    try:
        get_worker = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(worker_id,)
        )

        if not get_worker:
            raise HTTPException(status_code=400, detail='El trabajador no existe')
        
        if get_worker['permissions_id'] != 2:
            raise HTTPException(status_code=400, detail='Este usuario no es trabajador')
        
        update_worker = ganaderia_db.execute(
            sql='UPDATE users SET name = %s, last_name = %s WHERE id = %s',
            params=(
                worker.name if worker.name is not None else get_worker['name'],
                worker.last_name if worker.last_name is not None else get_worker['lastname'],
                worker_id,
            )
        )
        
        return {
            'status': 'success',
            'message': 'Worker updated successfully',
            'data': get_worker,
            'id': get_worker['id'],
            'new_data': {
                'name': worker.name if worker.name is not None else '',
                'lastname': worker.last_name if worker.last_name is not None else ''
            }
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al modificar trabajador')