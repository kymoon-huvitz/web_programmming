# app/routes/auth.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db
from app.forms import RegisterForm, LoginForm
from app.models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.profile"))

    form = RegisterForm()
    if form.validate_on_submit():
        # 중복 아이디/이메일 체크
        if User.query.filter_by(username=form.username.data).first():
            flash("이미 존재하는 아이디입니다.", "warning")
            return render_template("register.html", form=form)

        if form.email.data and User.query.filter_by(email=form.email.data).first():
            flash("이미 사용 중인 이메일입니다.", "warning")
            return render_template("register.html", form=form)

        user = User(username=form.username.data, email=form.email.data or None)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("회원가입 완료! 로그인 해주세요.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.profile"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not user.check_password(form.password.data):
            flash("아이디 또는 비밀번호가 올바르지 않습니다.", "danger")
            return render_template("login.html", form=form)

        login_user(user, remember=form.remember.data)
        flash("로그인 성공!", "success")
        # next 파라미터로 돌아갈 위치 처리
        next_url = request.args.get("next")
        return redirect(next_url or url_for("main.profile"))

    return render_template("login.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("로그아웃되었습니다.", "info")
    return redirect(url_for("auth.login"))
