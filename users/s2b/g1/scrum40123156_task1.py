# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 scrum40123156_task1, 並且 url 前綴為 /bg1, 並設定 template 存放目錄
scrum40123156_task1 = Blueprint('scrum40123156_task1', __name__, url_prefix='/bg1', template_folder='templates')

# scrum40123156_task1 為完整可以單獨執行的繪圖程式
@scrum40123156_task1.route('/scrum40123156_task1')
def task1():
    outstring = '''
    basic40123156_A_1 = cmbr.dup()
    basic40123156_A_1.rotate(30)
    basic40123156_A_1.translate(-40, 40)
    basic40123156_B_1 = cmbr.dup()
    basic40123156_B_1.rotate(0)
    basic40123156_B_1.translate(0, 40)
    basic40123156_B_2 = cmbr.dup()
    basic40123156_B_2.rotate(60)
    basic40123156_B_2.translate(20, 40)
    basic40123156_C_1 = cmbr.dup()
    basic40123156_C_1.rotate(0)
    basic40123156_C_1.translate(80, 60)
    basic40123156_D_1 = cmbr.dup()
    basic40123156_D_1.rotate(0)
    basic40123156_D_1.translate(160, 20)
    basic40123156_D_2 = cmbr.dup()
    basic40123156_D_2.rotate(90)
    basic40123156_D_2.translate(160, 0)

    cmbr.appendPath(basic40123156_A_1)
    cmbr.appendPath(basic40123156_B_1)
    cmbr.appendPath(basic40123156_B_2)
    cmbr.appendPath(basic40123156_C_1)
    cmbr.appendPath(basic40123156_D_1)
    cmbr.appendPath(basic40123156_D_2)
'''
    return outstring
    
