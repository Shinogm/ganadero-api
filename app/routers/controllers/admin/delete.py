from fastapi import HTTPException
from app.services.db import ganaderia_db

async def delete_admin(admin_id: int):
    try:
        admin_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(admin_id,)
        )

        if not admin_db:
            raise HTTPException(status_code=400, detail='Error al eliminar usuario')
        
        if admin_db['permissions_id'] != 1:
            raise HTTPException(status_code=400, detail='Este usuario no es admin')

        ganaderia_db.execute(
            sql='DELETE FROM users WHERE id = %s',
            params=(admin_id,)
        )

        return {
            'status': 'success',
            'message': 'Client deleted successfully',
            'id': admin_id,
            'data': admin_db,
            
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al eliminar usuario')