from sqlalchemy.orm import Session
from passlib.context import CryptContext
from itsdangerous import URLSafeTimedSerializer
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

SECRET_KEY = os.getenv("SECRET_KEY")
if SECRET_KEY is None:
    raise ValueError("No SECRET_KEY set for Flask application. Did you forget to run `source .env`?")
serializer = URLSafeTimedSerializer(SECRET_KEY)



def create_session_token(data: str):
    return serializer.dumps(data)

def load_session_token(token: str):
    try:
        return serializer.loads(token, max_age=3600)  # 1 hour session
    except Exception:
        return None

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, user_name: str, password: str):
    from src.db.crud import get_user
    user = get_user(db, user_name)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user