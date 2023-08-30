from fastapi import FastAPI
from routes.refuel import router
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI()
origins = [config('FRONTEND_URL')]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def welcome():
    return {'message': 'Welcome to RefuelOps API'}


app.include_router(router)

