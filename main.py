from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

header = """
<!DOCTYPE html>
    <html>
        <head>
            <title>Signup</title>
        </head>
        <body>
            <h3>Signup</h3>
"""
required_form = """
            <form methods=["POST"]>
                Username<input type="username" name="username" />
                Password<input type="password" name="password" />
                Verify Password<input type="password" name="v_password" />
            </form>
"""

email = """
            <form methods=["POST"]>
                Email (optional)<input type="text" name="email" />
            </form>
"""

footer = """
        </body>
    </html>
"""


@app.route("/")
def index():
    return (header + required_form + email + footer)

app.run()