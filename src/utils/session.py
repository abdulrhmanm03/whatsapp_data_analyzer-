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

def verify_session_token(file_name, token):
    token = load_session_token(token)
    if not token :
        return False
    if token != file_name:
        return False
    return True