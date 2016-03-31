# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
scrum1_task40123235 = Blueprint('scrum1_task40123235', __name__, url_prefix='/g2', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@scrum1_task40123235.route('/scrum1_task1')
def task1():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
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

    # 複製 cmbr, 然後命名為 A1
    A1 = cmbr.dup()
    # A1 轉 120 度
    A1.rotate(150)
    A2 = cmbr.dup()
    A2.rotate(0)
    A2.translate(0, -20)
    
    A3 = cmbr.dup()
    A3.rotate(90)
    A3.translate(20*math.cos(60*deg), 20*math.sin(60*deg))
    
    A4 = cmbr.dup()
    A4.rotate(30)
    A4.translate(20*math.cos(60*deg)+20, 20*math.sin(60*deg))
    
    A5 = cmbr.dup()
    A5.translate(2*20*math.cos(60*deg) +20,0)
    
    A6 = cmbr.dup()
    A6.translate(2*20*math.cos(60*deg) +20,-20)
    
    A7 = cmbr.dup()
    A7.rotate(90)
    A7.translate(0,-20)
    
    A8 = cmbr.dup()
    A8.rotate(90)
    A8.translate(20,-20)
    
    A9 = cmbr.dup()
    A9.translate(0,-40)
    
    A10 = cmbr.dup()
    A10.translate(2*20*math.cos(60*deg)+20,-40)
    
    B1 = cmbr.dup()
    B1.rotate(0)
    B1.translate(60, 0)
    
    B2 = cmbr.dup()
    B2.rotate(0)
    B2.translate(60, 20)
    
    B3 = cmbr.dup()
    B3.rotate(0)
    B3.translate(60, -20)
    
    B4 = cmbr.dup()
    B4.rotate(90)
    B4.translate(60, 20)
    
    B5 = cmbr.dup()
    B5.rotate(90)
    B5.translate(60,-20)
    
    B9 = cmbr.dup()
    B9.rotate(0)
    B9.translate(60,-40)
    
    B6 = cmbr.dup()
    B6.rotate(60)
    B6.translate(80,20)
    
    B7 = cmbr.dup()
    B7.rotate(120)
    B7.translate(80,-20)
    
    B8 = cmbr.dup()
    B8.rotate(0)
    B8.translate(20*math.cos(30*deg)+80,10)
    
    B10 = cmbr.dup()
    B10.rotate(60)
    B10.translate(80,-20)
    
    B11 = cmbr.dup()
    B11.rotate(120)
    B11.translate(80,-60)
    
    B12 = cmbr.dup()
    B12.rotate(0)
    B12.translate(20*math.cos(30*deg)+80,-30)
    
    B13 = cmbr.dup()
    B13.rotate(90)
    B13.translate(60,-60)
    
    C1 = cmbr.dup()
    C1.rotate(00)
    C1.translate(120,0)
    
    cmbr.appendPath(A1)
    cmbr.appendPath(A2)
    cmbr.appendPath(A3)
    cmbr.appendPath(A4)
    cmbr.appendPath(A5)
    cmbr.appendPath(A6)
    cmbr.appendPath(A7)
    cmbr.appendPath(A8)
    cmbr.appendPath(A9)
    cmbr.appendPath(A10)
    cmbr.appendPath(B1)
    cmbr.appendPath(B2)
    cmbr.appendPath(B3)
    cmbr.appendPath(B4)
    cmbr.appendPath(B5)
    cmbr.appendPath(B6)
    cmbr.appendPath(B7)
    cmbr.appendPath(B8)
    cmbr.appendPath(B9)
    cmbr.appendPath(B10)
    cmbr.appendPath(B11)
    cmbr.appendPath(B12)
    cmbr.appendPath(B13)
    cmbr.appendPath(C1)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    cgo.render(cmbr, x, y, 1, rot)
    # 放大 5 倍
    #cgo.render(cmbr, x, y, 5, rot)

O(0, 0, 0, 0, 0, "yellow", True, 4)
</script>
<!-- 以協同方式加上 ag100 的 scrum-2 組員所寫的 task1 程式碼 -->
<!--script type="text/python" src="/ag100/scrum2_task1"></script>-->
<!-- 以協同方式加上 ag100 的  scrum-3 組員所寫的 task1 程式碼 -->
<!-- <script type="text/python" src="/ag100/scrum3_task1"></script>-->
</body>
</html>
'''
    return outstring
    

    
    
