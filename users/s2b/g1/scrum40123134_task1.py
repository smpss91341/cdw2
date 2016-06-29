# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 scrum40123134_task1, 並且 url 前綴為 /bg1, 並設定 template 存放目錄
scrum40123134_task1 = Blueprint('scrum40123134_task1', __name__, url_prefix='/bg1', template_folder='templates')

# scrum40123134_task1 為完整可以單獨執行的繪圖程式
@scrum40123134_task1.route('/scrum40123134_task1')
def task1():
    outstring = '''
<<<<<<< HEAD
from javascript import JSConstructor
from browser import window
import math
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
cgo.setWorldCoords(-250, -250, 500, 500) 
# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })
deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })
    basic40123134_A_1 = cmbr.dup()
    basic40123134_A_1.rotate(90)
    basic40123134_A_1.translate(-70, 38.38)
  
    basic40123134_B_1 = cmbr.dup()
    basic40123134_B_1.rotate(180)
    basic40123134_B_1.translate(0, 20)

    basic40123134_B_2 = cmbr.dup()
    basic40123134_B_2.rotate(120)
    basic40123134_B_2.translate(20, 0)

    basic40123134_C_1 = cmbr.dup()
    basic40123134_C_1.rotate(120.63)
    basic40123134_C_1.translate(82.74, 29.81)

    basic40123134_D_1 = cmbr.dup()
    basic40123134_D_1.rotate(155.3)
    basic40123134_D_1.translate(196.13, -28.17)

    basic40123134_D_2 = cmbr.dup()
    basic40123134_D_2.rotate(180)
    basic40123134_D_2.translate(160, 0)


    cmbr.appendPath(basic40123134_A_1)
    cmbr.appendPath(basic40123134_B_1)
    cmbr.appendPath(basic40123134_B_2)
    cmbr.appendPath(basic40123134_C_1)
    cmbr.appendPath(basic40123134_D_1)
    cmbr.appendPath(basic40123134_D_2)


    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)
    # 表示放大 1 倍
    #cgo.render(cmbr, x, y, 1, rot)
    # 放大 1 倍
    cgo.render(cmbr, x, y, 1, rot)
O(0, 0, 0, 0, 0, "blue", True, 4)
=======
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

>>>>>>> e89a8e1c4ce1add6961e51c30a4712170e0a4ae8
'''
    return outstring
    
