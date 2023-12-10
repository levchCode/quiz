import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@quiz-db-1:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "1212"

db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)

from controllers.main_controller import main_controller

app.register_blueprint(main_controller)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
