from flask import g
from flask import redirect, flash, render_template
from flask_appbuilder import expose, BaseView
from flask_login import login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, UserMixin,  login_required, login_user, current_user, logout_user

from . import appbuilder


class AuthForm(FlaskForm):
    username = StringField("Имя пользователя: ", validators=[DataRequired()])
    password = PasswordField("Пароль: ", validators=[DataRequired()])
    submit = SubmitField("Клац")


class AuthView(BaseView):
    route_base = "/auth"

    @expose("/", methods=["GET", "POST"])
    def auth(self):
        if g.user.is_authenticated:
            flash("Вы уже авторизованы", "message")
            return redirect("/")
        auth_form = AuthForm()
        if auth_form.validate_on_submit():
            username = auth_form.username.data
            password = auth_form.password.data
            user = self.appbuilder.sm.auth_user_db(username, password)
            if user:
                login_user(user=user)
                flash("Авторизация успешно выполнена", "success")
                return redirect("/")
            else:
                flash("Неверное имя пользователя или пароль", "danger")

        return self.render_template("auth.html", form=auth_form)

    @expose("/logout/", methods=["GET"])
    def logout(self):
        if g.user.is_anonymous:
            redirect("/")
        logout_user()
        flash("Вы успешно разлогинились", "message")
        return redirect("/")


appbuilder.add_view_no_menu(AuthView())
