from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import vocab

app = FastAPI()

@app.get("/")
async def read_root():
    return RedirectResponse(url="/docs")

# Allows frontend to access api
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# api routers
app.include_router(vocab.router)