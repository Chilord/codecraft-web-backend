from flask import Flask
from flask_cors import CORS
from .routes.router import auth_bp
from datetime import timedelta

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["https://codecraft-studio.surge.sh", "http://localhost:5173"])
app.secret_key = "i}UuBu_buG_BuHbh_ufIyu(f67*yfityf/diTurD67{t]ojbur.fdc6rdDufufFyfyf)fYutdydfI"  # change later
app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True
)
app.permanent_session_lifetime = timedelta(days=30)
app.register_blueprint(auth_bp)


if __name__ == "__main__":
    app.run(debug=True)
