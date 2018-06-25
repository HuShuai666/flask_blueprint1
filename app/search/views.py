from flask import render_template, Blueprint



search=Blueprint('search',__name__)

def init_blue(app):
    app.register_blueprint(search, url_prefix='/search',template_folder='templates')
    app.add_template_filter(add,'add')
class Shop():
    def __init__(self,title,name):
        self.name=name
        self.title=title

def add(param1,param2):

    return param1+param2






@search.route('/temp/')
def temp2():

    return render_template('/search/search.html',hello='world',
                                                li=['1',2,3],
                                                dt={'name':'小明','age':12},
                                                shop=Shop('手机','华为')
                           )


@search.route('/fi/')
def filter1():
    return render_template('search/filter.html')


@search.route('/ext/')
def extend1():
    return render_template('extends/extend01.html')


