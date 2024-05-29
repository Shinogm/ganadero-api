from fastapi import HTTPException
from app.services.db import ganaderia_db

async def worker_horas(user_id: int, horas_trabajadas: int, dias_trabajados: str ):

    try:
        worker_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(user_id,)
        )

        if not worker_db:
            raise HTTPException(status_code=400, detail='Error al crear nomina')
        
        if worker_db['permissions_id'] != 2:
            raise HTTPException(status_code=400, detail='Este usuario no es trabajador')
        
        if dias_trabajados and horas_trabajadas is None:
            raise HTTPException(status_code=400, detail="No se puede trabajar sin horas")
        
        worker_db = ganaderia_db.insert(
            table='TrabajadorHorasTrabajadas',
            data={
                'user_id': user_id,
                'horas_trabajadas': horas_trabajadas,
                'dias_trabajados': dias_trabajados
            }
        )

        get_horario = ganaderia_db.fetch_one(
            sql='SELECT * FROM TrabajadorHorasTrabajadas WHERE user_id = %s',
            params=(user_id,)
        )

        if not get_horario:
            raise HTTPException(status_code=400, detail='Error al crear horario')

        return {
                'status': 'success',
                'message': 'Horario creado',
                'worker_id': user_id,
                'horario': get_horario,
                'worker': worker_db
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al crear horario')
    

async def asistencia_worker(user_id: int, asistencia: int):
    try:
        worker_db = ganaderia_db.fetch_one(
            sql='SELECT * FROM users WHERE id = %s',
            params=(user_id,)
        )

        if not worker_db:
            raise HTTPException(status_code=400, detail='Error al obtener al trabajador')
        
        if asistencia not in [0, 1]:
            raise HTTPException(status_code=400, detail='Asistencia no es en rango')
        
        if worker_db['permissions_id'] != 2:
            raise HTTPException(status_code=400, detail='Este usuario no es trabajador')
        
        if asistencia == 1:
            ganaderia_db.insert(
                table='TrabajadorAsistencia',
                data={
                    'user_id': user_id,
                }
            )
        else:
            ganaderia_db.insert(
                table='TrabajadorAsistencia',
                data={
                    'user_id': user_id,
                    'asistencia': 'no'
                }
            )
        get_asistencia = ganaderia_db.fetch_all(
            sql='SELECT * FROM TrabajadorAsistencia WHERE user_id = %s',
            params=(user_id,)
        )

        if not get_asistencia:
            raise HTTPException(status_code=400, detail='Error al crear asistencia')

        return {
                'status': 'success',
                'message': 'Asistencia creada',
                'worker_id': user_id,
                'asistencia_type': '1 = Sí, 0 = No',
                'asistencia': get_asistencia,
                'worker': worker_db
            }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al crear asistencia')
            

import datetime

async def asistencia_worker_all_in_this_week():
    try:
        # Obtener todos los trabajadores con permisos de id 2
        workers_db = ganaderia_db.fetch_all(
            sql='SELECT * FROM users WHERE permissions_id = 2'
        )

        if not workers_db:
            raise HTTPException(status_code=400, detail='Error al obtener trabajadores')

        # Fecha de inicio y fin de la semana actual
        today = datetime.datetime.today()
        start_of_week = today - datetime.timedelta(days=today.weekday())
        end_of_week = start_of_week + datetime.timedelta(days=6, hours=23, minutes=59, seconds=59)

        asistencia_this_week = []

        for worker in workers_db:
            # Obtener la asistencia del trabajador para la semana actual
            asistencia = ganaderia_db.fetch_all(
                sql='SELECT * FROM TrabajadorAsistencia WHERE user_id = %s AND created_at BETWEEN %s AND %s',
                params=(worker['id'], start_of_week, end_of_week)
            )

            if not asistencia:
                continue

            # Convertir la fecha de creación al formato datetime si es necesario
            for record in asistencia:
                if isinstance(record['created_at'], str):
                    record['created_at'] = datetime.datetime.strptime(record['created_at'], '%Y-%m-%d %H:%M:%S')

            worker['asistencia'] = asistencia
            asistencia_this_week.append(worker)

        if not asistencia_this_week:
            raise HTTPException(status_code=400, detail='No hay asistencia registrada para esta semana')

        return {
            'status': 'success',
            'message': 'Asistencia obtenida',
            'workers': asistencia_this_week,
            'asistencia_type': '1 = Sí, 0 = No'
        }

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail='Error al obtener asistencia')