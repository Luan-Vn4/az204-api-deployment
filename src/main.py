import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    """
    Retorna uma mensagem de Hello World!
    """
    return {"message": "Hello World"}


if __name__ == '__main__':
    config = uvicorn.Config("main:app", port=5000, log_level="info", host="0.0.0.0")
    server = uvicorn.Server(config)
    server.run()
