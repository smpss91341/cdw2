# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag4_40323135 = Blueprint('ag4_40323135', __name__, url_prefix='/ag4_40323135', template_folder='templates')

# 展示傳回 Brython 程式
@ag4_40323135.route('/A')
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

cgo.setWorldCoords(-250, -4500, 5000, 5000) 

# 決定要不要畫座標軸線
#cgo.drawAxes(0, 240, 0, 240, {
#    "strokeColor":"#aaaaaa",
#    "fillColor": "#aaaaaa",
#    "xTickInterval": 20,
#    "xLabelInterval": 20,
#    "yTickInterval": 20,
#    "yLabelInterval": 20})
        
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

    # 複製 cmbr, 然後命名為 basic1
    basic1 = cmbr.dup()
    basic1.rotate(180)
    
    cmbr.appendPath(basic1)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(0, 0, 0, 0, 0, "Orange", True, 4)
'''
    return outstring
    
@ag4_40323135.route('/B')
def task2():
    outstring = '''
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -4500, 5000, 5000) 

# 決定要不要畫座標軸線
#cgo.drawAxes(0, 240, 0, 240, {
#    "strokeColor":"#aaaaaa",
#    "fillColor": "#aaaaaa",
#    "xTickInterval": 20,
#    "xLabelInterval": 20,
#    "yTickInterval": 20,
#    "yLabelInterval": 20})
        
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

    # 複製 cmbr, 然後命名為 basic1
    basic4 = cmbr.dup()
    basic4.rotate(0)
    basic4.translate(60, 60) 
    
    basic5 = cmbr.dup()
    basic5.rotate(90)
    basic5.translate(60, 60) 
    
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(0, 0, 0, 0, 0, "Orange", True, 4)
'''
    return outstring
    
@ag4_40323135.route('/C')
def task3():
    outstring = '''
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -4500, 5000, 5000) 

# 決定要不要畫座標軸線
#cgo.drawAxes(0, 240, 0, 240, {
#    "strokeColor":"#aaaaaa",
#    "fillColor": "#aaaaaa",
#    "xTickInterval": 20,
#    "xLabelInterval": 20,
#    "yTickInterval": 20,
#    "yLabelInterval": 20})
        
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

    # 複製 cmbr, 然後命名為 basic1
    basic3 = cmbr.dup()
    basic3.rotate(0)
    basic3.translate(120, 40) 
    
    cmbr.appendPath(basic3)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(0, 0, 0, 0, 0, "Orange", True, 4)
'''
    return outstring
    
@ag4_40323135.route('/D')
def task4():
    outstring = '''
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -4500, 5000, 5000) 

# 決定要不要畫座標軸線
#cgo.drawAxes(0, 240, 0, 240, {
#    "strokeColor":"#aaaaaa",
#    "fillColor": "#aaaaaa",
#    "xTickInterval": 20,
#    "xLabelInterval": 20,
#    "yTickInterval": 20,
#    "yLabelInterval": 20})
        
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

    # 複製 cmbr, 然後命名為 basic1
    basic3 = cmbr.dup()
    basic3.rotate(0)
    basic3.translate(180, 40)
    
    basic4 = cmbr.dup()
    basic4.rotate(0)
    basic4.translate(180, 60)
    
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(0, 0, 0, 0, 0, "Orange", True, 4)
'''
    return outstring
