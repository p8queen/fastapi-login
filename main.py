from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()

# Base de datos simulada de usuarios y sesiones
fake_users_db = {
    "user1": {"username": "user1", "password": "password1"},
    "user2": {"username": "user2", "password": "password2"}
}

# Diccionario para almacenar tokens de sesión (simulado)
active_sessions = {}

# Modelo para los datos de inicio de sesión
class LoginRequest(BaseModel):
    username: str
    password: str

# Función para autenticar al usuario
def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and user["password"] == password:
        return True
    return False
@app.get("/")
def read_root():
    return {"Hello": "World"}


# Ruta para el login
@app.post("/login")
async def login(request: LoginRequest):
    if authenticate_user(request.username, request.password):
        # Crear un "token" de sesión (aquí lo simulamos con el nombre de usuario)
        session_token = f"token_{request.username}"
        active_sessions[request.username] = session_token
        return {"message": "Login successful", "session_token": session_token}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

# Ruta para el logout
@app.post("/logout")
async def logout(username: str):
    if username in active_sessions:
        # Eliminar la sesión activa
        del active_sessions[username]
        return {"message": "Logout successful"}
    else:
        raise HTTPException(status_code=401, detail="User is not logged in")

# Para probarlo, corre el servidor y realiza las solicitudes POST a /login y /logout
