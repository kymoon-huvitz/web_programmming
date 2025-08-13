"""
app/routes/main.py — 일반 페이지(홈/대시보드)
"""
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # 홈 페이지 (로그인/회원가입 진입)
    return render_template('index.html')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    # 로그인한 사용자만 볼 수 있습니다.
    # 템플릿에서 current_user.email 등을 사용할 수 있어요.
    return render_template('dashboard.html')
