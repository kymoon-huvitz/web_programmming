from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import GuestbookForm
from app.extensions import db
from app.models import GuestbookEntry

main_bp = Blueprint("main", __name__)

@main_bp.route("/", methods=["GET"])
def index():
    return redirect(url_for("main.guestbook"))

@main_bp.route("/guestbook", methods=["GET", "POST"])
def guestbook():
    form = GuestbookForm()
    if form.validate_on_submit():
        entry = GuestbookEntry(name=form.name.data, message=form.message.data)
        db.session.add(entry)
        db.session.commit()
        flash("방명록이 등록되었습니다.", "success")
        return redirect(url_for("main.guestbook"))
    entries = GuestbookEntry.query.order_by(GuestbookEntry.created_at.desc()).all()
    return render_template("guestbook.html", form=form, entries=entries)

# ✅ 삭제 라우트 추가 (POST 전용)
@main_bp.route("/guestbook/delete/<int:entry_id>", methods=["POST"])
def delete_entry(entry_id):
    entry = GuestbookEntry.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("삭제되었습니다.", "info")
    return redirect(url_for("main.guestbook"))

@main_bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)
