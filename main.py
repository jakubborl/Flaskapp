from website import create_app
from flask_migrate import Migrate
from website.views import views as views_blueprint
from website import db
from website import db
from website import create_app, db 



app = create_app()

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True, port=8080)