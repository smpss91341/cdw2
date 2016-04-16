#各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
scrum2_task40323218 = Blueprint('scrum2_task40323218', __name__, url_prefix='/bg9', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@scrum2_task40323218.route('/scrum2_18')
def scrum2_18():
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
    cgoChamber = window.svgToCgoSVG(chamber,60 ,60)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })
            
            
    basic1 = cmbr.dup()
    basic1.translate(0, 20)
    
    basic2 = cmbr.dup()
    basic2.translate(-60, -60)    
    basic2.rotate(-90)
    basic2.translate(30, 40+20*math.cos(30*deg))
    
    basic3 = cmbr.dup()
    basic3.translate(20, 80)
    
    basic4 = cmbr.dup()
    basic4.translate(20, 100)
   
    basic5 = cmbr.dup()
    basic5.translate(40, 100)
    
    basic6 = cmbr.dup()
    basic6.translate(40, 80)
    
    basic7 = cmbr.dup()
    basic7.translate(60, 100)
    
    basic8 = cmbr.dup()
    basic8.translate(60, 80)
    
    basic9 = cmbr.dup()
    basic9.translate(-60, -60)    
    basic9.rotate(-90)
    basic9.translate(120, 160)
    
    basic10 = cmbr.dup()
    basic10.translate(-60, -60)    
    basic10.rotate(-90)
    basic10.translate(120, 120)
    
    basic11 = cmbr.dup()
    basic11.translate(-60, -60)    
    basic11.rotate(-90)
    basic11.translate(120, 140)
     
      
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
    
    
    
    # hole 為原點位置
    #hole = cobj(shapedefs.circle(4), "PATH") 
    #cmbr.appendPath(hole) 

  
    # 放大 1 倍
    cgo.render(cmbr, x, y, 1, rot)
    
O(0, 0, 0, 0, 0, "blue", True, 4)




'''
    return outstring