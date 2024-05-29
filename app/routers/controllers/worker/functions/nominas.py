from fastapi import HTTPException
from app.services.db import ganaderia_db

async def create_nomina(worker_id: int, nomina: int, otros_gastos: int | None = None):

    try:
        worker_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(worker_id,)
        )

        if not worker_db:
            raise HTTPException(status_code=400, detail='Error al crear nomina')
        
        if worker_db['permissions_id'] != 2:
            raise HTTPException(status_code=400, detail='Este usuario no es trabajador')

        if otros_gastos is not None:

            calculo_total = nomina - otros_gastos

            nomina_db = ganaderia_db.execute(
                sql='INSERT INTO TrabajadorNomina (user_id, nomina, otros_gastos, total_nomina) VALUES (%s, %s, %s, %s)',
                params=(
                    worker_id,
                    nomina,
                    otros_gastos,
                    calculo_total
                )
            )

        else:
            nomina_db = ganaderia_db.execute(
                sql='INSERT INTO TrabajadorNomina (user_id, nomina) VALUES (%s, %s)',
                params=(
                    worker_id,
                    nomina
                )
            )

        get_nomina = ganaderia_db.fetch_one(
                sql='SELECT * FROM TrabajadorNomina WHERE id = %s',
                params=(nomina_db,)
            )
        if not get_nomina:
            raise HTTPException(status_code=400, detail='Error al crear nomina')
        
        return {
                'status': 'success',
                'message': 'Nomina created successfully',
                'id': nomina_db,
                'nomina_id': nomina_db,
                'worker_id': worker_id,
                'worker': worker_db,
                'nomina': get_nomina
            }
            
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al crear nomina')
    
async def get_nomina(worker_id: int):
        worker_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(worker_id,)
        )
        

        if worker_db['permissions_id'] != 2:
            raise HTTPException(status_code=400, detail='Este usuario no es trabajador')
        
        get_nomina = ganaderia_db.fetch_all(
            sql='SELECT * FROM TrabajadorNomina WHERE user_id = %s',
            params=(worker_id,)
        )

        return {
                'status': 'success',
                'message': 'Nomina created successfully',
                'id': get_nomina,
                'nomina_id': get_nomina,
                'nomina': get_nomina
            }

async def get_nomina_one(nomina_id: int):
    try:
        get_nomina_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorNomina WHERE id = %s',
            params=(nomina_id,)
        )

        if not get_nomina_db:
            raise HTTPException(status_code=400, detail='Error al obtener nomina')

        return {
                'status': 'success',
                'message': 'Nomina created successfully',
                'nomina': get_nomina_db
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener nomina')
    
async def delete_nomina(nomina_id: int):
    try:
        get_nomina_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorNomina WHERE id = %s',
            params=(nomina_id,)
        )

        if not get_nomina_db:
            raise HTTPException(status_code=400, detail='Error al obtener nomina')

        ganaderia_db.execute(
            sql='DELETE FROM TrabajadorNomina WHERE id = %s',
            params=(nomina_id,)
        )

        return {
                'status': 'success',
                'message': 'Nomina deleted successfully',
                'id': get_nomina_db,
                'nomina_id': get_nomina_db,
                'nomina': get_nomina_db
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener nomina')
    
async def get_all_nominas():
    try:
        get_nominas = ganaderia_db.fetch_all(
            sql='SELECT * FROM TrabajadorNomina'
        )

        if not get_nominas:
            raise HTTPException(status_code=400, detail='Error al obtener nomina')

        return {
                'status': 'success',
                'message': 'Nomina created successfully',
                'nominas': get_nominas
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener nomina')