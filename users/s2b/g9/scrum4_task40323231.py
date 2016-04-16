#各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
scrum4_task40323231 = Blueprint('scrum4_task40323231', __name__, url_prefix='/bg9', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@scrum4_task40323231.route('/scrum4_31')
def scrum4_31():
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
    
    
    
    cmbr.translate(40, 40)
  
    basic1 = cmbr.dup()
    basic1.translate(180, 100)
    
    basic2 = cmbr.dup()
    basic2.translate(180, 120)
    
    basic3 = cmbr.dup()
    basic3.translate(-40, -40)
    basic3.rotate(90)
    basic3.translate(200, 120)
    
    basic4 = cmbr.dup()
    basic4.translate(-40, -40)
    basic4.rotate(90)
    basic4.translate(200, 140)
    
    basic5 = cmbr.dup()
    basic5.translate(-40, -40)
    basic5.rotate(90)
    basic5.translate(200, 160)
    
    basic6 = cmbr.dup()
    basic6.translate(200, 120)
    
    basic7 = cmbr.dup()
    basic7.translate(200, 100)
    
    basic8 = cmbr.dup()
    basic8.translate(40+20*math.cos(30*deg), 20+20*math.sin(30*deg))
    
    basic9 = cmbr.dup()
    basic9.translate(-40, -40)
    basic9.rotate(-60)
    basic9.translate(80+20*math.cos(30*deg), 40+20*math.sin(30*deg))
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    
    # hole 為原點位置
    #hole = cobj(shapedefs.circle(4), "PATH") 
    #cmbr.appendPath(hole) 


    # 放大 1 倍
    cgo.render(cmbr, x, y, 1, rot)
    
O(0, 0, 0, 0, 0, "pink", True, 4)



'''
    return outstring