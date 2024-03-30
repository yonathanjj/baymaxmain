from baymax import app, db
from user_model import Users


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""

    db.create_all()
    print("Database tables created!")
