from flask import Flask, render_template, request, session, redirect
from functools import wraps
from dbUtils import getList, add, setFinish

# creates a Flask application, specify a static folder on /
app = Flask(__name__, static_folder='static',static_url_path='/')
#set a secret key to hash cookies
app.config['SECRET_KEY'] = '123TyU%^&'

#define a function wrapper to check login session
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        loginID = session.get('loginID')
        if not loginID:
            return redirect('/loginPage.html')
        return f(*args, **kwargs)
    return wrapper

@app.route("/") 
#check login with decorator funtion
@login_required
def hello(): 
    message = "Hello, World 1"
    return message

    
@app.route("/test/<string:name>/<int:id>")
#取得網址作為參數
def useParam(name,id):
    if not isLogin():
        return redirect('/loginPage.html')
    return f"got name={name}, id={id} "
    
#handles login request
@app.route('/login', methods=['POST'])
def login():
    form =request.form
    id = form['ID']
    pwd =form['PWD']
    #idate id/pwd
    if id=='123' and pwd=='456':
        session['loginID']=id
        return redirect("/")
    else:
        session['loginID']=False
        return redirect("/loginPage.html")


@app.route("/edit")
#使用server side render: template 樣板
def h1():
    dat={
        "name": "大牛",
        "content":"內容說明文字"
    }
    #editform.html 存在於 templates目錄下, 將dat 作為參數送進 editform.html, 名稱為 data
    return render_template('editform.html', data=dat)
    
@app.route("/update",methods=['Post'])
#使用server side render: template 樣板
def upd():
    name=request.form['name']
    cnt=request.form['content']
    #sql
    html=f"update===> nnn:{name},cnt={cnt}"
    return html

@app.route("/list")
#使用server side render: template 樣板
def h2():
    dat=[
        {
            "name": "大牛",
            "p":"愛吃瓜"
        },
        {
            "name": "小李",
            "p":"怕榴槤"
        },
        {
            "name": "",
            "p":"ttttt"
        },
        {
            "name": "老謝",
            "p":"來者不拒"
        }
    ]
    return render_template('list.html', data=dat)


@app.route('/input', methods=['GET', 'POST'])
def userInput():
    if request.method == 'POST':
        form =request.form
    else:
        form= request.args
#取得使用者參數
    txt = form['txt']  # pass the form field name as key
    note =form['note']
    select = form['sel']
    msg=f"method: {request.method} txt:{txt} note:{note} sel: {select}"
    return msg

@app.route("/listJob")
#使用server side render: template 樣板
def gl():
    dat=getList()
    return render_template('todolist.html', data=dat)
    
@app.route('/addJob', methods=['POST']) #用於提交數據到伺服器，通常是用於創建或更新資源。
def addJob():
    if request.method == 'POST':
        form =request.form
    else:
        form= request.args
#取得使用者參數
    jobName= form['name']  # pass the form field name as key
    jobContent =form['content']
    due = form['due']
    add(jobName,jobContent,due)
    return redirect("/listJob")

@app.route('/setfinish', methods=['GET']) #用於請求資料。它從伺服器獲取信息，而不會改變伺服器的狀態。
def done():
    if request.method == 'POST':
        form =request.form
    else:
        form= request.args
#取得使用者參數
    id = form['id']  # pass the form field name as key
    setFinish(id)
    return redirect("/listJob")
    

