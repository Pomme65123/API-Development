import bcrypt

def hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify(plain_password: str, hashed_password: str) -> bool:
    try:
        if isinstance(plain_password, bytes):
            plain = plain_password
        else:
            plain = plain_password.encode("utf-8")

        if isinstance(hashed_password, bytes):
            hashed = hashed_password
        else:
            hp = hashed_password
            if isinstance(hp, str) and ((hp.startswith("b'") and hp.endswith("'")) or (hp.startswith('b"') and hp.endswith('"'))):
                hp = hp[2:-1]
            hashed = hp.encode("utf-8")

        return bcrypt.checkpw(plain, hashed)
    except ValueError:
        
        return False
    except Exception:
        return False