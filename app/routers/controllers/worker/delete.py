from fastapi import HTTPException
from app.services.db import ganaderia_db

async def delete_worker(worker_id: int):
    try:
        worker_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(worker_id,)
        )

        if not worker_db:
            raise HTTPException(status_code=400, detail='Error al eliminar trabajador')
        
        if worker_db['permissions_id'] != 2:
            raise HTTPException(status_code=400, detail='Este trabajador no es trabajador')

        ganaderia_db.execute(
            sql='DELETE FROM users WHERE id = %s',
            params=(worker_id,)
        )

        return {
            'status': 'success',
            'message': 'Worker deleted successfully',
            'id': worker_id,
            'data': worker_db,
            
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al eliminar trabajador')