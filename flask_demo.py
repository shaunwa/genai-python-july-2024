from flask import escape

def insert_name_into_h1(name):
    safe_name = escape(name)
    html = f"<h1>{safe_name}</h1>"
    return html
