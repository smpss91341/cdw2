# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
bg99 = Blueprint('bg99', __name__, url_prefix='/bg99', template_folder='templates')

@bg99.route('/task0')
def task0():
    return "bg99 task0"
    
@bg99.route('/task1')
def task1():
    #return "bg99 task1"
    return render_template('task1.html', var1="來自 bg99 的 task1 變數")
    
    
