# 주석 강화(설명용) Flask Auth 예제

이 버전은 학습을 위해 각 파일에 **설명 주석**을 촘촘히 추가했습니다.
아키텍처 개요, 실행 방법, 파일 관계가 모두 반영되어 있습니다.

## 빠른 실행(로컬, 가상환경 권장)


# 1) 프로젝트 루트로 이동 (run.py 파일이 있는 위치로)
cd D:\git_storage\web_programmming\root

# 2) 새 가상환경 생성
python -m venv .venv

# 3) 가상환경 활성화
.\.venv\Scripts\Activate

# 4) pip 최신화 + 의존성 설치
python -m pip install --upgrade pip
pip install -r requirements.txt
(requirements.txt 없으면 pip install Flask 실행해서 파이썬 설치)

# 5) 설치 확인(선택)
python -c "import flask_login, flask_sqlalchemy, flask; print('OK', flask.__version__)"

# 6) 실행
python run.py

```powershell
cd root
python -m venv .venv
.\.venv\Scripts\Activate
pip install -r requirements.txt

# 첫 실행: DB 테이블 생성 포함
python run.py
# http://127.0.0.1:8000
```

## 주요 파일
- `root/run.py` — 앱 시동키
- `root/app/__init__.py` — 앱 공장(create_app), 확장 초기화, 블루프린트 등록
- `root/app/extensions.py` — 공용 확장 인스턴스
- `root/app/models.py` — User 모델
- `root/app/forms.py` — Register/Login 폼(유효성검사)
- `root/app/routes/*.py` — URL 처리기
- `root/app/templates/*.html` — HTML 템플릿(Jinja2)
- `root/config.py` — 설정(SECRET_KEY/DB)
- `root/requirements.txt` — 패키지 목록
```



