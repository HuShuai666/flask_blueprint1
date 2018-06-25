from os import abort

from flask import Blueprint, render_template
import logging
home=Blueprint('home',__name__)




#动态url   自定义路由
@home.route('/<re("\d{4}"):year>/',methods=['post','get','head','put','delete'])
def test1(year):
   # logging.info(year)
   print(year)
   return 'home'



#异常处理
# @home.route('/2/')
# def test2():
#     return abort(400)
#
# @home.errorhandler(404)
# def error(e):
#     return render_template('errors/404.html')