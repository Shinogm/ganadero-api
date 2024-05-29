from app.services.fastapi import App
from fastapi.responses import StreamingResponse
from datetime import datetime
import asyncio
from app.routers.router import admin, nominas, worker, activities, horario
from app.utils.middlewae import custom_middleware

def main():
    app = App(
    routers=[
        admin.router,
        worker.router,
        nominas.router,
        activities.router,
        horario.router
    ],
    ).get_app()

    return app
if __name__ == '__main__':
    app = main()

    #app.middleware('http')(custom_middleware)

    @app.get('/')
    async def home():

        async def generate():
            for i in range(10):
                yield f"data: {datetime.now()}\n\n"
                await asyncio.sleep(1)
                

        return StreamingResponse(generate(), media_type="text/event-stream")

    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=3001)

