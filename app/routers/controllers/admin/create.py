from fastapi import HTTPException, Depends
from app.services.db import ganaderia_db
from app.models.admin import AdminModel
import bcrypt

async def create_admin(admin: AdminModel = Depends(AdminModel.as_form)):

    try:

        admin_id = ganaderia_db.insert(
            table='users',
            data={
                'name': admin.name,
                'last_name': admin.last_name,
                'password': bcrypt.hashpw(admin.password.encode('utf-8'), bcrypt.gensalt()),
                'email': admin.email,
                'permissions_id': 1
            }
        )

        get_admin = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(admin_id,)
        )

        if not get_admin:
            raise HTTPException(status_code=400, detail='Error al crear usuario')

        return {
            'status': 'success',
            'id': get_admin['id'],
            'name': get_admin['name'],
            'last_name': get_admin['last_name'],
            'email': get_admin['email'],
            'permissions_id': get_admin['permissions_id']
        }
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al crear usuario catch')
    