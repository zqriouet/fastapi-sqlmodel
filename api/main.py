from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine
from routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    from models import Item

    print("Start")
    Item.metadata.create_all(engine)
    yield
    print("Shut down")


app = FastAPI(lifespan=lifespan)
app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
