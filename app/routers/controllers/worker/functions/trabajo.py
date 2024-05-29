from fastapi import HTTPException
from app.services.db import ganaderia_db

async def create_trabajo(worker_id: int, tareas_realizar: str):
    try:
        worker_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(worker_id,)
        )

        if not worker_db:
            raise HTTPException(status_code=400, detail='Error al crear nomina')
        
        if worker_db['permissions_id'] != 2:
            raise HTTPException(status_code=400, detail='Este usuario no es trabajador')

        ganaderia_db.execute(
            sql='INSERT INTO TrabajadorTareasRealizar (user_id, tareas_realizar) VALUES (%s, %s)',
            params=(
                worker_id,
                tareas_realizar
            )
        )

        get_tareas = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorTareasRealizar WHERE user_id = %s',
            params=(worker_id,)
        )

        if not get_tareas:
            raise HTTPException(status_code=400, detail='Error al crear nomina')

        return {
                'status': 'success',
                'message': 'Nomina created successfully',
                'id': worker_id,
                'tareas_realizar': get_tareas,
                'worker': worker_db
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al crear nomina')
    
async def status_finalizado(id: int):
    try:
        get_tareas = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorTareasRealizar WHERE id = %s',
            params=(id,)
        )

        if not get_tareas:
            raise HTTPException(status_code=400, detail='Error al obtener tareas')
        
        if get_tareas['status'] == 'realizada':
            raise HTTPException(status_code=400, detail='Esta tarea ya fue finalizada')
        
        if get_tareas['status'] != 'pendiente':
            raise HTTPException(status_code=400, detail='Esta tarea ya fue realizada o cancelada')

        ganaderia_db.execute(
            sql='UPDATE TrabajadorTareasRealizar SET status = %s WHERE id = %s',
            params=(
                'realizada',
                id
            )
        )

        get_worker = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorTareasRealizar WHERE id = %s',
            params=(id,)
        )

        if not get_worker:
            raise HTTPException(status_code=400, detail='Error al obtener trajador')
        
        return {
                'status': 'success',
                'message': 'Tarea finalizada',
                'id_tarea': id,
                'tareas_realizar': get_tareas,
                'worker': get_worker
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener nomina')
    
async def status_cancelado(id: int):
    try:
        get_tareas = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorTareasRealizar WHERE id = %s',
            params=(id,)
        )

        if not get_tareas:
            raise HTTPException(status_code=400, detail='Error al obtener tareas')
        
        if get_tareas['status'] == 'cancelada':
            raise HTTPException(status_code=400, detail='Esta tarea ya fue cancelada')
        
        if get_tareas['status'] != 'pendiente':
            raise HTTPException(status_code=400, detail='Esta tarea ya fue realizada o cancelada')

        ganaderia_db.execute(
            sql='UPDATE TrabajadorTareasRealizar SET status = %s WHERE id = %s',
            params=(
                'cancelada',
                id
            )
        )

        get_worker = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorTareasRealizar WHERE id = %s',
            params=(id,)
        )

        if not get_worker:
            raise HTTPException(status_code=400, detail='Error al obtener trajador')
        
        return {
                'status': 'success',
                'message': 'Tarea cancelada',
                'id_tarea': id,
                'tareas_realizar': get_tareas,
                'worker': get_worker
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener nomina')
    
async def status_pendiente(id: int):
    try:
        get_tareas = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorTareasRealizar WHERE id = %s',
            params=(id,)
        )

        if not get_tareas:
            raise HTTPException(status_code=400, detail='Error al obtener tareas')
        
        if get_tareas['status'] == 'realizada':
            raise HTTPException(status_code=400, detail='Esta tarea ya fue finalizada')
        
        if get_tareas['status'] != 'pendiente':
            raise HTTPException(status_code=400, detail='Esta tarea ya fue realizada o cancelada')

        ganaderia_db.execute(
            sql='UPDATE TrabajadorTareasRealizar SET status = %s WHERE id = %s',
            params=(
                'pendiente',
                id
            )
        )

        get_worker = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorTareasRealizar WHERE id = %s',
            params=(id,)
        )

        if not get_worker:
            raise HTTPException(status_code=400, detail='Error al obtener trajador')
        
        return {
                'status': 'success',
                'message': 'Tarea pendiente',
                'id_tarea': id,
                'tareas_realizar': get_tareas,
                'worker': get_worker
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener nomina')
    

async def get_tareas_pendientes(worker_id: int):
    try:
        worker_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(worker_id,)
        )

        if not worker_db:
            raise HTTPException(status_code=400, detail='Error al obtener nomina')

        if worker_db['permissions_id'] != 2:
            raise HTTPException(status_code=400, detail='Este usuario no es trabajador')
        
        get_tareas = ganaderia_db.fetch_all(
            sql='SELECT * FROM TrabajadorTareasRealizar WHERE user_id = %s AND status = %s',
            params=(
                worker_id,
                'pendiente'
            )
        )

        if not get_tareas:
            raise HTTPException(status_code=400, detail='Error al obtener nomina')

        return {
                'status': 'success',
                'message': 'Tareas pendientes',
                'worker': worker_db,
                'tareas_realizar': get_tareas
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener nomina')
    
