from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_filename=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jj1995123@localhost:3306/baymax_db'
    db.init_app(app)

    return app
