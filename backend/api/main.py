from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import vocab

app = FastAPI()

@app.get("/")
async def read_root():
    return RedirectResponse(url="/docs")

app.include_router(vocab.router)

# run command if in api folder:
# uvicorn main:app --reload