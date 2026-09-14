from fastapi import FastAPI

app = FastAPI(title="AI Agent")


@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/echo/{count}")
async def echo_count(count: int):
    return {"count": 2*count}