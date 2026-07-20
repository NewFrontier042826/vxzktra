from fastapi import FastAPI

app = FastAPI(
    title="vxzktra",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to vxzktra"
    }


@app.get("/health")
def health ():
    return {
        "status": "healthy"
    }