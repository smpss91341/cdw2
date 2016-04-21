# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 scrum40123134_task1, 並且 url 前綴為 /bg1, 並設定 template 存放目錄
scrum40123134_task1 = Blueprint('scrum40123134_task1', __name__, url_prefix='/bg1', template_folder='templates')

# scrum40123134_task1 為完整可以單獨執行的繪圖程式
@scrum40123134_task1.route('/scrum40123134_task1')
def task1():
    outstring = '''
   basic1 = cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(120)
    basic2 = cmbr.dup()
    basic2.rotate(60)
    basic2.translate(0, -20)
    
    basic3 = cmbr.dup()
    basic3.rotate(60)
    basic3.translate(20*math.cos(30*deg), 20*math.sin(30*deg))
    
    basic4 = cmbr.dup()
    basic4.rotate(120)
    basic4.translate(20*math.cos(30*deg), -20*math.sin(30*deg)-20)
    
    basic5 = cmbr.dup()
    basic5.translate(2*20*math.cos(30*deg), 0)
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)

O(0, 0, 0, 0, 0, "red", True, 4)

'''
    return outstring
    
