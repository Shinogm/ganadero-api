from fastapi import HTTPException, Depends
from app.services.db import ganaderia_db
from app.models.admin import AdminModifyModel
import bcrypt

async def modify_admin(admin_id: int, admin: AdminModifyModel = Depends(AdminModifyModel.as_form)):
    try:
        get_admin = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(admin_id,)
        )

        if not get_admin:
            raise HTTPException(status_code=400, detail='Error al modificar usuario')
        
        if get_admin['permissions_id'] != 1:
            raise HTTPException(status_code=400, detail='Este usuario no es admin')
        
        update_admin = ganaderia_db.execute(
            sql='UPDATE users SET name = %s, last_name = %s, email = %s, password = %s WHERE id = %s',
            params=(
                admin.name if admin.name is not None else get_admin['name'],
                admin.last_name if admin.last_name is not None else get_admin['lastname'],
                admin.email if admin.email is not None else get_admin['email'],
                bcrypt.hashpw(admin.password.encode('utf-8'), bcrypt.gensalt()) if admin.password is not None else get_admin['password'],
                admin_id,
            )
        )

        return {
        'status': 'success',
        'message': 'Client updated successfully',
        'data': get_admin,
        'id': get_admin['id'],
        'new_data': {
            'name': admin.name if admin.name is not None else '',
            'lastname': admin.last_name if admin.last_name is not None else '',
            'email': admin.email if admin.email is not None else '',
            'password': admin.password if admin.password is not None else ''
        }
    }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al modificar usuario')
