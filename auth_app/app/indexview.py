from flask import g
from flask_appbuilder import expose, IndexView


class CustomIndexView(IndexView):
    @expose("/")
    def index(self):
        user = g.user
        return self.render_template("index.html")
