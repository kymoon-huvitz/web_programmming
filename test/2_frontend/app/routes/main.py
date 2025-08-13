from flask import Blueprint, render_template

# Blueprint: 라우트를 묶어서 관리
main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("index.html", name="Mun Kwangyul")