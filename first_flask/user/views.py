from flask import Blueprint,jsonify,request
from first_flask import db
from first_flask.user.models import Show

mod=Blueprint('user',__name__)

@mod.route('/',methods=['GET'])
def fetch_user():
    users = Show.query.all()
    response=[user.__repr__() for user in users]
    return jsonify(response)

@mod.route('/<user_id>',methods=['GET'])
def show1(user_id):
    user=Show.query.get(int(user_id))
    response=user.__repr__()
    return jsonify(response)


@mod.route('/create_user',methods=['GET','POST'])
def show():
    if request.method=='POST':
       emp=request.get_json()

       name=emp['name']
       age = emp['age']
       entry= Show(name=name,age=age)
       db.session.add(entry)
       db.session.commit()
    #    return "data sent"
    return 'data sent successfully'

@mod.route('/get_user',methods=['GET'])
def fetch_user_by_name():
    name=request.args.get('name')
    user=Show.query.filter(Show.name==name).first()
    response=user.__repr__()
    return jsonify(response)

@mod.route('/get_user1',methods=['PUT'])
def fetch_user_by_name1():
    name=request.args.get('name')
    user=Show.query.filter(Show.name==name).first()
    age=request.form.get('age')
    user.age=age
    db.session.commit()

    return "data update successfully"


