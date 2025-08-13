"""
app/routes/auth.py — 인증(회원가입/로그인/로그아웃) 관련 라우트
- URL ↔ 파이썬 함수(뷰)를 연결하는 곳입니다.
"""
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from ..forms import RegisterForm, LoginForm
from ..models import User
from ..extensions import db

auth_bp = Blueprint('auth', __name__)  # 블루프린트 이름: 'auth'

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    회원가입
    - GET: 폼 보여주기
    - POST: 유효성 검사 통과 시 유저 생성
    """
    if current_user.is_authenticated:
        # 이미 로그인한 사용자는 대시보드로 보냅니다.
        return redirect(url_for('main.dashboard'))

    form = RegisterForm()
    if form.validate_on_submit():  # 제출 + 유효성 검증 OK
        email = form.email.data.lower().strip()

        # 중복 이메일 방지
        if User.query.filter_by(email=email).first():
            flash('Email already registered. Please log in.', 'warning')
            return redirect(url_for('auth.login'))

        # 새 유저 생성 + 비밀번호 해시 저장
        user = User(email=email)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth.login'))

    # 처음 접근하거나, 검증 실패 시 폼 템플릿 렌더링
    return render_template('register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    로그인
    - GET: 로그인 폼
    - POST: 이메일/비밀번호 확인 후 세션에 로그인 기록
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(form.password.data):
            login_user(user)  # 세션에 로그인 상태 기록(쿠키 기반)
            flash('Logged in successfully.', 'success')
            # ?next=/dashboard 와 같은 쿼리를 지원(보호 페이지 접근 후 로그인 시 유용)
            next_url = request.args.get('next')
            return redirect(next_url or url_for('main.dashboard'))

        flash('Invalid email or password.', 'danger')

    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required  # 로그인해야만 접근 가능
def logout():
    """
    로그아웃: 세션에서 로그인 상태 제거
    """
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
