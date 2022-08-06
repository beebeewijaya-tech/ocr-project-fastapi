from fastapi import FastAPI

from router import file

app = FastAPI()

app.include_router(file.router)
