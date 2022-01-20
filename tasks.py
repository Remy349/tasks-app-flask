from flaskr import app, db
from flaskr.models import Users, Tasks

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Users": Users, "Tasks": Tasks}
