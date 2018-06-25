from flask import Blueprint, render_template, request, redirect

from app.ext import db
from  .models import User

"""
蓝图，模块化，


"""
user = Blueprint('user', __name__,static_folder='static',template_folder='templates')


# 把注册动态的东西拿到自己的views下





@user.route('/index/')
def index():
    # user=User.query.get(1)
    # User.query.fillter(User.name=='老王')
    # user=User()
    # db.session.add(user)
    # db.session.commit(name='老王')
    user=User(name='老王')
    db.session.add(user)
    db.session.commit()
    return render_template('index.html', msg='东京热还是武汉热')



"""
查表  行跟列的组合
查询所有 select * from 表


"""
@user.route('/find/')
def find():
    user=User.query.get(1)  #用id查
    User.query.all()  #查询所有
    User.query.filter(User.name=='老王').first()  #用姓名查
    return render_template('index.html', msg='东京热还是武汉热',user=user)




@user.route('/1/')
def test():
    return '123'



@user.route('/add/')
def add():
    objects=[]
    for i in range(1,11):
        objects.append(User(name='test'+str(i)))
    db.session.bulk_save_objects(objects)
    db.session.commit()
    return '批量保存'


@user.route('/list/')
def list():
    page=request.values.get('page',default=1,type=int)
    size=request.values.get('size',default=10,type=int)
    paginate=db.session.query(User.uid,User.name).order_by(User.uid).paginate(page=page,per_page=size,error_out=False)
    shops=paginate.items
    return  render_template('index.html',shops=shops,paginate=paginate)



@user.route('/add3/',methods=['GET','POST'])
def add3():
    if request.method=='GET':
        return render_template('add.html')
    elif request.method=='POST':
        name=request.values.get('name')
        uid=request.values.get('uid',default=1,type=int)
        user=User(name=name,uid=uid)
        db.session.add(user)
        db.session.commit()
        return redirect('/user/list/')




@user.route('/update/', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        uid = request.values.get('uid', type=int)
        user = User.query.get(uid)
        return render_template('update.html', user=user)
    elif request.method == 'POST':
        uid = request.values.get('uid', type=int)
        name = request.values.get('name')
        User.query.filter(User.uid == uid).update({User.uid: uid, User.name: name})
        db.session.commit()
        return redirect('/user/list/')


@user.route('/del/')
def delete():
    uid=request.values.get('uid',type=int)
    db.session.delete(User.query.get(uid))
    db.session.commit()
    return redirect('/user/list/')