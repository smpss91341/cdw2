# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 scrum40123129_task1, 並且 url 前綴為 /bg1, 並設定 template 存放目錄
scrum40123129_task1 = Blueprint('scrum40123129_task1', __name__, url_prefix='/bg1', template_folder='templates')

# scrum40123129_task1 為完整可以單獨執行的繪圖程式
@scrum40123129_task1.route('/scrum40123129_task1')
def task1():
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

    basic1A = cmbr.dup()
    basic1A.rotate(0)
    basic1A.translate(-90, 60)
    basic2A = cmbr.dup()
    basic2A.rotate(0)
    basic2A.translate(-30, 30)
    basic1B = cmbr.dup()
    basic1B.rotate(90)
    basic1B.translate(0, 80)
    basic2B = cmbr.dup()
    basic2B.rotate(120)
    basic2B.translate(20, 0)
    basic1C = cmbr.dup()
    basic1C.rotate(-120)
    basic1C.translate(100, 0)
    basic1D = cmbr.dup()
    basic1D.rotate(-300)
    basic1D.translate(180, 80)
    
    cmbr.appendPath(basic1A)
    cmbr.appendPath(basic2A)
    cmbr.appendPath(basic1B)
    cmbr.appendPath(basic2B)
    cmbr.appendPath(basic1C)
    cmbr.appendPath(basic1D)
    

    
    # hole 為原點位置
    #hole = cobj(shapedefs.circle(4), "PATH") 
    #cmbr.appendPath(hole) 

  
    # 放大 1 倍
    cgo.render(cmbr, x, y, 1, rot)
    
O(0, 0, 0, 0, 0, "orange", True, 4)

'''
    return outstring
    
