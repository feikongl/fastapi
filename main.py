from fastapi import FastAPI

app = FastAPI()


@app.get("/test/{id}")
async def root(id: float):
    return f"hello world    {id}"
