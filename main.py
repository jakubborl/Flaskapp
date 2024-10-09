from website import create_app, db
from flask_migrate import Migrate
from website.views import views as views_blueprint

app = create_app()

migrate = Migrate(app, db)
