from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.forms import GuestbookForm
from app.extensions import db
from app.models import GuestbookEntry

# Blueprint: 라우트를 묶어서 관리
main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def index():
    # 메인은 방명록으로 가이드
    return redirect(url_for("main.guestbook"))

@main_bp.route("/guestbook", methods=["GET", "POST"])
def guestbook():
    form = GuestbookForm()

    if form.validate_on_submit():
        entry = GuestbookEntry(name=form.name.data, message=form.message.data)
        db.session.add(entry)
        db.session.commit()   # 실제 DB에 반영
        flash("방명록이 등록되었습니다.", "success")
        return redirect(url_for("main.guestbook"))

    # 최신 글이 위로 오게 정렬
    entries = GuestbookEntry.query.order_by(GuestbookEntry.created_at.desc()).all()
    return render_template("guestbook.html", form=form, entries=entries)

@main_bp.route("/guestbook/delete/<int:entry_id>", methods=["POST"])
def delete_entry(entry_id):
    entry = GuestbookEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("삭제되었습니다.", "info")
    return redirect(url_for("main.guestbook"))