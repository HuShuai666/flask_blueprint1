from flask import Flask

from app.ext import config_db, init_ext
from app.home.converter import RegexConverter
from app.home.views import home
from app.search.views import search, init_blue,temp2
from app.user.views import user, index

app = Flask(__name__)
app.debug=True
app.url_map.converters['re']=RegexConverter




def get_app():
    register_blue()
    init_ext(app)
    return app

def register_blue():
    init_blue(app)
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(home,url_prefix='/home')
    # app.register_blueprint(search, url_prefix='/search')
    init_blue(app)




















#
# blue=Blueprint('app',__name__)
# app.register_blueprint(blue,url_prefix='/app')