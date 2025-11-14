# -----------------------------
# SECURITY
# -----------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "your-default-secret-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
ALLOWED_HOSTS.append("forms-2-2ajg.onrender.com")  # optional: your Render URL

# CSRF trusted origins (fixes 403 CSRF error)
CSRF_TRUSTED_ORIGINS = [
    'https://forms-2-2ajg.onrender.com',
]

# Optional: secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
