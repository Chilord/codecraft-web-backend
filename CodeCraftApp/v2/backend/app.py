from flask import Flask
from flask_cors import CORS
from .routes.router import auth_bp
from datetime import timedelta

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = "i}UuBu_buG_BuHbh_ufIyu(f67*yfityf/diTurD67{t]ojbur.fdc6rdDufufFyfyf)fYutdydfI"  # change later
app.permanent_session_lifetime = timedelta(days=30)
app.register_blueprint(auth_bp)


if __name__ == "__main__":
    app.run(debug=True)