from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
@login_required

def home():
    if request.method == "POST":
        note_data = request.form.get("note")
        if len(note_data) < 1:
            flash("Zpráva je moc krátká!", category="error")
        else:
            new_note = Note(data=note_data, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Zpráva odeslána.", category="success")

    notes = Note.query.all()
    print(notes)  # Debugging: Print notes to check if they are being retrieved
    return render_template("home.html", user=current_user, notes=notes)


@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note["noteId"]
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})


