from fastapi import FastAPI

app = FastAPI(title="Usalamaguard Core API")

@app.get("/")
def Home():
    return {
        "message": "Welcome to UsalamaGuard open-source API! "
    }