from . import app, login_manager, upload_folder, results_folder, login_manager_ukr
from flask import render_template, redirect, request, make_response
from .db_controls import add_account, get_db, check_user
from .user import func
from flask_login import logout_user, login_required, login_user, current_user
from werkzeug.utils import secure_filename
from .main import face_detection, fullbody_detection
import os
@app.route("/")
@app.route("/main")
def index():
    return render_template("main.html")


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_Post():
    username = request.form["username"]
    user_check = check_user(username)
    if user_check != []:
        user = func("name", username)
        login_user(user)
        # response = make_response({"IsLogged": True, "Username": username})
        return render_template("main.html", msg="Successfully logged in!", username=username)
    elif user_check == []:
        # response = make_response({"IsLogged": False, "Username": username})
        return render_template("login.html", msg="Wrong username!")


@app.route("/signup", methods=["GET"])
def signup():
    return render_template("signup.html")


@app.route("/signup", methods=["POST"])
def signup_Post():
    username = request.form["username"]
    password = request.form["password"]

    user_check = check_user(username)
    if user_check == []:
        add_account(username, password)
        print(f"new user -- {username, password}")
        user = func("name", username)
        login_user(user)
        return render_template("main.html", msg="Successfuly added!", username=username)
    else:
        return render_template("signup.html", msg="The user with the same username was already added to our database.\nPlease be sure that you typed a correct username, password.")

@app.route("/import_image", methods=['GET', 'POST'])
@login_required
def import_image():
    if request.method == 'POST':
        try:
            app.config['UPLOAD'] = upload_folder
            app.config['RESULTS'] = results_folder
            file = request.files['img']
            option = request.form["option"]
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD'], filename))
        except FileNotFoundError:
            return render_template("main.html", msg="You didn't send any file/photo.")
        if option == "Only Face detection":
            face_detection(filename)
            if face_detection(filename) == "Empty":
                return render_template("main.html", msg="Sorry, but neural network doesn't see any outlines of human face or body.")
            elif face_detection(filename) == "ERROR":
                return render_template("main.html", msg="Sorry, but an error has occurred while neural network was working on your photo, try again later.")
            else:
                img = os.path.join(app.config['RESULTS'], filename).replace("\\", "/")
                return render_template("export.html", img=img)
        elif option == "Full body detection":
            fullbody_detection(filename)
            if fullbody_detection(filename) == "Empty":
                return render_template("main.html", msg="Sorry, but neural network doesn't see any outlines of human face or body.")
            elif fullbody_detection(filename) == "ERROR":
                return render_template("main.html", msg="Sorry, but an error has occurred while neural network was working on your photo, try again later.")
            else:
                img = os.path.join(app.config['RESULTS'], filename).replace("\\", "/")
                return render_template("export.html", img=img)
    return render_template('import.html')

@app.route("/english")
def english():
    return render_template("main.html", msg="Successfully changed to english language")

@app.route("/ukrainian")
def ukrainian():
    return render_template("ukr/main_ukr.html", msg="Successfully changed to ukrainian language")

@app.route("/ukr")
@app.route("/main_ukr")
def index_ukr():
    return render_template("ukr/main_ukr.html")


@app.route("/login_ukr", methods=["GET"])
def login_ukr():
    return render_template("ukr/login_ukr.html")


@app.route("/login_ukr", methods=["POST"])
def login_Post_ukr():
    username = request.form["username"]
    user_check = check_user(username)
    if user_check != []:
        user = func("name", username)
        login_user(user)
        # response = make_response({"IsLogged": True, "Username": username})
        return render_template("ukr/main_ukr.html", msg="Успішно ввійшли в аккаунт!", username=username)
    elif user_check == []:
        # response = make_response({"IsLogged": False, "Username": username})
        return render_template("ukr/login_ukr.html", msg="Невірне ім'я користувача")


@app.route("/signup_ukr", methods=["GET"])
def signup_ukr():
    return render_template("ukr/signup_ukr.html")


@app.route("/signup_ukr", methods=["POST"])
def signup_Post_ukr():
    username = request.form["username"]
    password = request.form["password"]

    user_check = check_user(username)
    if user_check == []:
        add_account(username, password)
        print(f"new user -- {username, password}")
        user = func("name", username)
        login_user(user)
        return render_template("ukr/main_ukr.html", msg="Успішно додано!", username=username)
    else:
        return render_template("ukr/signup_ukr.html", msg="Користувач з таким самим іменем вже був доданий до нашої бази данної.\nЮудь ласка, будьте впевнені у тому, чи ви ввели правильні данні.")

@app.route("/import_image_ukr", methods=['GET', 'POST'])
@login_required
def import_image_ukr():
    if request.method == 'POST':
        try:
            app.config['UPLOAD'] = upload_folder
            app.config['RESULTS'] = results_folder
            file = request.files['img']
            option = request.form["option"]
            filename = secure_filename(file.filename)
            print(filename)
            file.save(os.path.join(app.config['UPLOAD'], filename))
        except FileNotFoundError:
            return render_template("ukr/main_ukr.html", msg="Ви не відправили жодного фото\файлу.")
        if option == "Детекція обличчя":
            face_detection(filename)
            if face_detection(filename) == "Empty":
                return render_template("ukr/main_ukr.html", msg="Вибачте, але нейронна мережа не бачить ніяких контурів людського тіла або обличчя.")
            elif face_detection(filename) == "ERROR":
                return render_template("ukr/main_ukr.html", msg="Вибачте, але відбулась помилка поки нейронна мережа працювала над вашою фоткою, спробуйте ще раз пізніше.")
            else:
                img = os.path.join(app.config['RESULTS'], filename).replace("\\", "/")
                return render_template("ukr/export_ukr.html", img=img)
        elif option == "Детекція всього тіла":
            fullbody_detection(filename)
            if fullbody_detection(filename) == "Empty":
                return render_template("ukr/main_ukr.html", msg="Вибачте, але нейронна мережа не бачить ніяких контурів людського тіла або обличчя.")
            elif fullbody_detection(filename) == "ERROR":
                return render_template("ukr/main_ukr.html", msg="Вибачте, але відбулась помилка поки нейронна мережа працювала над вашою фоткою, спробуйте ще раз пізніше.")
            else:
                img = os.path.join(app.config['RESULTS'], filename).replace("\\", "/")
                return render_template("ukr/export_ukr.html", img=img)
    return render_template('ukr/import_ukr.html')

@app.route("/log_out")
def logout():
    logout_user()
    return redirect("/")

@app.route("/log_out_ukr")
def logout_ukr():
    logout_user()
    return redirect("/main_ukr")

@login_manager.user_loader
def load_user(user):
    user = func("id", user)
    return user

@login_manager_ukr.user_loader
def load_user_ukr(user):
    user = func("id", user)
    return user






