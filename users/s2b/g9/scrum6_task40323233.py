#各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
scrum6_task40323233 = Blueprint('scrum6_task40323233', __name__, url_prefix='/bg9', template_folder='templates')

# scrum6_task33 為完整可以單獨執行的繪圖程式
@scrum6_task40323233.route('/scrum6_33')
def scrum6_33():
    outstring = '''

from javascript import JSConstructor
from browser import window
import math
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
cgo.setWorldCoords(-250, -250, 500, 500) 

        
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
  
    cmbr.translate(100, -60)
    
    
    basic1 = cmbr.dup()
    basic1.translate(-100, 60)
    basic1.rotate(-90)
    basic1.translate(40, 20)
    
    basic2 = cmbr.dup()
    basic2.translate(0, -20)
    
    basic3 = cmbr.dup()
    basic3.translate(-100, 60)
    basic3.rotate(-90)
    basic3.translate(100, -60)
    
    basic4 = cmbr.dup()
    basic4.translate(-100, 60)
    basic4.rotate(-90)
    basic4.translate(100, -80)
    
    basic5 = cmbr.dup()
    basic5.translate(-100, 60)
    basic5.rotate(-90)
    basic5.translate(100, -100)
    
    basic6 = cmbr.dup()
    basic6.translate(-100, 60)
    basic6.rotate(-90)
    basic6.translate(140, -100)
    
    basic7 = cmbr.dup()
    basic7.translate(-100, 60)
    basic7.rotate(-90)
    basic7.translate(140, -60)
    
    basic8 = cmbr.dup()
    basic8.translate(-100, 60)
    basic8.rotate(-90)
    basic8.translate(140, -80)
    
    basic9 = cmbr.dup()
    basic9.translate(40, 0)
    
    basic10 = cmbr.dup()
    basic10.translate(40, -20)
    
    basic11 = cmbr.dup()
    basic11.translate(-100, 60)
    basic11.rotate(-60)
    basic11.translate(80+20*math.cos(30*deg), 20*math.sin(30*deg))
    
    basic12 = cmbr.dup()
    basic12.translate(-100, 60)
    basic12.rotate(90)
    basic12.translate(60, 0)
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    
    # hole 為原點位置
    #hole = cobj(shapedefs.circle(4), "PATH") 
    #cmbr.appendPath(hole) 


    # 放大 1 倍
    cgo.render(cmbr, x, y, 1, rot)
    
O(0, 0, 0, 0, 0, "purple", True, 4)


'''
    return outstring