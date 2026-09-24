"""Login + roles. Tokens are signed and expire after TOKEN_HOURS."""
import hmac
import secrets
import time
from typing import Dict

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

from app.core.config import settings

USERS: Dict[str, tuple] = {}
for _item in settings.APP_USERS.split(","):
    _p = _item.strip().split(":")
    if len(_p) >= 2:
        USERS[_p[0]] = (_p[1], _p[2] if len(_p) > 2 else "user")

if not USERS or any("change_me" in pw for pw, _ in USERS.values()):
    raise RuntimeError(
        "Set real passwords in APP_USERS in RAG\\.env (format user:password:role). "
        "Startup is blocked while 'change_me' is left in."
    )

_secret = settings.SECRET_KEY
if not _secret or "change_me" in _secret:
    _secret = secrets.token_hex(32)  # random each start; set SECRET_KEY to stay logged in after restarts
_signer = URLSafeTimedSerializer(_secret)
_fails: Dict[str, list] = {}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


def authenticate(username: str, password: str) -> dict:
    now = time.time()
    recent = [t for t in _fails.get(username, []) if now - t < 300]
    if len(recent) >= 5:
        raise HTTPException(429, "Too many failed attempts. Try again in 5 minutes.")
    rec = USERS.get(username)
    if not rec or not hmac.compare_digest(rec[0].encode(), password.encode()):
        _fails[username] = recent + [now]
        raise HTTPException(401, "Wrong username or password.")
    _fails.pop(username, None)
    return {
        "access_token": _signer.dumps({"u": username, "r": rec[1]}),
        "token_type": "bearer",
        "role": rec[1],
    }


def current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        return _signer.loads(token, max_age=settings.TOKEN_HOURS * 3600)
    except SignatureExpired:
        raise HTTPException(401, "Session expired. Log in again.")
    except BadSignature:
        raise HTTPException(401, "Invalid login token.")


def admin_only(user: dict = Depends(current_user)) -> dict:
    if user["r"] != "admin":
        raise HTTPException(403, "Admin only.")
    return user
