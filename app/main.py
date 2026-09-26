from fastapi import FastAPI

app = FastAPI(title="Fastapi fullstack")


@app.get("/")
def read_root():
    return {"Message": "Servidor Fastapi Activo"}
