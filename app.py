from fastapi import FastAPI
from .config.db import engine
from .routes import product, rating
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(product.router)
app.include_router(rating.router)


@app.get("/")
async def root():
    return {"message": "Fakeapi"}

if __name__ == '__main__':
    app.run()