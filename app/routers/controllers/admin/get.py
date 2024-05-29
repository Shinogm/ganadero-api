from fastapi import HTTPException
from app.services.db import ganaderia_db

async def get_all_admins():
    try:
        admins = ganaderia_db.fetch_all(
            sql='SELECT * FROM users WHERE permissions_id = 1'
        )
        return {
            'status': 'success',
            'admins': admins
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener usuarios')

async def get_one_admin(admin_id: int):
    try:
        admin = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(admin_id,)
        )
        return {
            'status': 'success',
            'admin': admin
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener usuario')
