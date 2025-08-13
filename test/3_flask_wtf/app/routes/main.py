from flask import Blueprint, render_template
from app.forms import InfoForm

# Blueprint: 라우트를 묶어서 관리
main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET", "POST"])
def home():
    form = InfoForm()
    name = None
    age = None

    if form.validate_on_submit(): # POST 요청 + 유효성 검사 통과
        name = form.name.data
        age = form.age.data
        form.name.data = ""
        form.age.data = ""

    return render_template("form.html", form=form, name=name, age=age)