from flask import Blueprint

# Blueprint: 라우트를 묶어서 관리
main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return "Hello, Flask World!"