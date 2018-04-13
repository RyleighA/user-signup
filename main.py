from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

#Cant make password validation error show
#Not sure how to make username and email stay

def input_check(string):
    error4 = ""
    if len(string) < 3 or len(string) > 20:
        error4 = "Invalid username/password"
        return error4

    if " " in string:
        error4 = "Invalid username/password"
        return error4

    return error4

def email_check(email):
    error6 = ""
    if len(email) < 3 or len(email) > 20:
        error6 = "Invalid email"
        return error6

    if " " in email:
        error6 = "Invalid email"
        return error6

    char1 = email.count('@')
    char2 = email.count('.')

    if char1 is not 1:
        error6 = "Invalid email"
        return error6

    if char2 is not 1:
        error6 = "Invalid email"
        return error6

    return error6
    
@app.route("/submit", methods=['POST'])
def submit():
    error1 = ""
    error2 = ""
    error3 = ""
    error4 = ""
    error5 = ""
    error6 = ""
    email_c = ""

    username = request.form['username']
    password = request.form['password']
    v_password = request.form['v_password']
    email = request.form['email']

    username_check = input_check(username)
    password_check = input_check(password)

    if email is not "":
        email_c = email_check(email)

    if email_c == "Invalid email":
        error6 = "Invalid email"

    if username_check or password_check == "Invalid username/password":
        error4 = "Invalid username/password"

    if username == "":
        error1 = "Please enter a username"
    
    if password == "":
        error2 = "Please enter a password"
    
    if v_password == "":
        error3 = "Please verify your password"

    if password != v_password:
        error5 = "Passwords do not match"

    if error4 and error6:
        return redirect("/?error=C")

    if error1 and error2 and error3:
        return redirect("/?error=1")

    if error2 and error3 and error4:
        return redirect("/?error=0")
    
    if error1 and error2:
        return redirect("/?error=2")

    if error2 and error3:
        return redirect("/?error=3&" + "username=" + username)

    if error1 and error3:
        return redirect("/?error=4")

    if error1:
        return redirect("/?error=5")

    if error2:
        return redirect("/?error=6&" + "username=" + username)

    if error3 and error4:
        return redirect("/?error=7&" + "username=" + username)

    if error4:
        return redirect("/?error=8&" + "username=" + username)
    
    if error3:
        return redirect("/?error=9&" + "username=" + username)

    if error5:
        return redirect("/?error=A&" + "username=" + username)

    if error6:
        return redirect("/?error=B&" + "username=" + username)
    
    return render_template('submit.html', username=username)

@app.route("/")
def index():
    error_check = request.args.get("error")
    username = request.args.get("username")

    error1 = "Please enter a username"
    error2 = "Please enter a password"
    error3 = "Please verify your password"
    error4 = "Invalid username/password"
    error5 = "Passwords do not match"
    error6 = "Invalid email"

    if error_check is "C":
        return render_template("mainpage.html", error4=error4, error6=error6)

    if error_check is "0":
        return render_template("mainpage.html", error2=error2, error3=error3, error4=error4)

    if error_check is "1":
        return render_template("mainpage.html", error1=error1, error2=error2, error3=error3)

    if error_check is "2":
        return render_template("mainpage.html", error1=error1, error2=error2,)

    if error_check is "3":
        return render_template("mainpage.html", error2=error2, error3=error3, username=username)

    if error_check is "4":
        return render_template("mainpage.html", error1=error1, error3=error3)

    if error_check is "5":
        return render_template("mainpage.html", error1=error1)

    if error_check is "6":
        return render_template("mainpage.html", error2=error2, username=username)

    if error_check is "7":
        return render_template("mainpage.html", error3=error3, error4=error4, username=username)

    if error_check is "8":
        return render_template("mainpage.html", error4=error4, username=username)

    if error_check is "9":
        return render_template("mainpage.html", error3=error3, username=username)

    if error_check is "A":
        return render_template("mainpage.html", error5=error5, username=username)

    if error_check is "B":
        return render_template("mainpage.html", error6=error6, username=username)

    return render_template("mainpage.html")

app.run()