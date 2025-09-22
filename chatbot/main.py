from fastapi import FastAPI



app = FastAPI()


@app.post('/webhook')
def root(data:dict):
    print(data)