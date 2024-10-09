from website import create_app, db
from website.models import Note

app = create_app()

with app.app_context():
    Note.query.delete()
    db.session.commit()
    print("Všechny poznámky byly smazány.")
