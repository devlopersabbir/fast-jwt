from passlib.context import CryptContext

passwordContext = CryptContext(schemes=["bcrypt"], deprected="auto")
def hashPassword(password: str)->str:
    return passwordContext.hash(password)