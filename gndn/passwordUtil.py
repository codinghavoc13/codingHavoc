import base64
import hashlib
import secrets

ALGORITHM = "pbkdf2_sha256"
ITERATIONS = 260000

def hash_password(password, salt=None, iterations=260000):
    if salt is None:
        salt = secrets.token_hex(32)
    assert salt and isinstance(salt, str) and "$" not in salt
    assert isinstance(password, str)
    pw_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations
    )
    b64_hash = base64.b64encode(pw_hash).decode("ascii").strip()
    return "{}${}".format(salt, b64_hash)


def verify_password(password, password_hash, password_salt):
    compare_hash = hash_password(password, password_salt, ITERATIONS)
    salt, b64_hash = compare_hash.split("$", 1)
    compare = b64_hash
    return secrets.compare_digest(password_hash, compare)