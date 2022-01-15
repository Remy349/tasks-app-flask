from flask import redirect, url_for, session
from functools import wraps

def login_required(f):
    """ 
        Funcion para evitar que personas sin un usuario visiten
        otras rutas de la app, de lo contrario se les mostrara el formulario de registro
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("signup"))
        return f(*args, **kwargs)
    return decorated_function
