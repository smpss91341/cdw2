# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
bg2 = Blueprint('bg2', __name__, url_prefix='/bg2', template_folder='templates')

@bg2.route('/task0')
def task0():
    return "bg2 task0"
    
@bg2.route('/task1')
def task1():
    #return "bg2 task1"
    return render_template('task1.html', var1="來自 bg2 的 task1 變數")

# 展示傳回 Brython 程式
@bg2.route('/task2')
def task2():
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

    # 複製 cmbr, 然後命名為 basic1
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
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(0, 0, 0, 0, 0, "lightyellow", True, 4)
</script>
<!-- 以協同方式加上 ag100 的 task3 程式碼 -->
<script type="text/python" src="/ag100/task3"></script>
<!-- 以協同方式加上 bg99 的 task3 程式碼 -->
<script type="text/python" src="/bg99/task3"></script>
</body>
</html>
'''
    return outstring
    
# 展示傳回 Brython 程式
@bg2.route('/task3')
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

def task3(x, y, rx, ry, rot, color, border, linewidth):
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
    # basic1 轉 -60 度
    basic1.rotate(-60)

    cmbr.appendPath(basic1)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

task3(0, 0, 0, 0, 0, "red", True, 4)
'''
    return outstring
    #A的程式
@bg2.route('/ss1')
def solvespace1():
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

cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  

def ss1(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M31.964 78.744 A7.000,7.000 0 0,0 39.250,75.828 A7.000,7.000 0 0,0 39.250,67.981 A7.000,7.000 0 0,0 31.964,65.065 A40.000,40.000 0 0,1 14.942,65.065 A7.000,7.000 0 0,0 7.656,67.981 A7.000,7.000 0 0,0 7.656,75.828 A7.000,7.000 0 0,0 14.942,78.744 A40.000,40.000 0 0,1 31.964,78.744 M20.293 73.394 A40.000,40.000 0 0,0 20.293,90.415 A7.000,7.000 0 0,1 17.377,97.701 A7.000,7.000 0 0,1 9.529,97.701 A7.000,7.000 0 0,1 6.613,90.415 A40.000,40.000 0 0,0 6.613,73.394 A7.000,7.000 0 0,1 9.529,66.108 A7.000,7.000 0 0,1 17.377,66.108 A7.000,7.000 0 0,1 20.293,73.394 M20.293 53.394 A7.000,7.000 0 0,0 17.377,46.108 A7.000,7.000 0 0,0 9.529,46.108 A7.000,7.000 0 0,0 6.613,53.394 A40.000,40.000 0 0,1 6.613,70.415 A7.000,7.000 0 0,0 9.529,77.701 A7.000,7.000 0 0,0 17.377,77.701 A7.000,7.000 0 0,0 20.293,70.415 A40.000,40.000 0 0,1 20.293,53.394M24.731 35.711 A7.000,7.000 0 0,0 23.743,27.926 A7.000,7.000 0 0,0 16.147,25.950 A7.000,7.000 0 0,0 11.492,32.268 A40.000,40.000 0 0,1 7.208,48.742 A7.000,7.000 0 0,0 8.196,56.527 A7.000,7.000 0 0,0 15.792,58.502 A7.000,7.000 0 0,0 20.447,52.184 A40.000,40.000 0 0,1 24.731,35.711M29.713 16.389 A7.000,7.000 0 0,0 28.764,8.582 A7.000,7.000 0 0,0 21.159,6.584 A7.000,7.000 0 0,0 16.495,12.915 A40.000,40.000 0 0,1 12.237,29.395 A7.000,7.000 0 0,0 13.542,37.503 A7.000,7.000 0 0,0 21.652,38.791 A7.000,7.000 0 0,0 25.405,31.487 A40.000,40.000 0 0,1 29.713,16.389M55.381 32.347 A7.000,7.000 0 0,0 50.768,25.967 A7.000,7.000 0 0,0 43.138,27.913 A7.000,7.000 0 0,0 42.145,35.723 A41.009,41.009 0 0,1 46.554,52.252 A6.872,6.872 0 0,0 51.164,58.396 A6.872,6.872 0 0,0 58.589,56.429 A6.872,6.872 0 0,0 59.551,48.807 A39.004,39.004 0 0,1 55.381,32.347M50.375 12.915 A7.000,7.000 0 0,0 45.729,6.590 A7.000,7.000 0 0,0 38.131,8.553 A7.000,7.000 0 0,0 37.131,16.337 A40.000,40.000 0 0,1 41.389,32.817 A7.000,7.000 0 0,0 46.035,39.142 A7.000,7.000 0 0,0 53.633,37.179 A7.000,7.000 0 0,0 54.633,29.395 A40.000,40.000 0 0,1 50.375,12.915M51.931 78.740 A6.995,6.995 0 0,0 59.210,75.826M59.210 75.826 A6.995,6.995 0 0,0 59.211,67.985M59.211 67.985 A6.995,6.995 0 0,0 51.933,65.069M51.933 65.069 A40.033,40.033 0 0,1 34.938,65.068M34.938 65.068 A6.996,6.996 0 0,0 27.658,67.984M27.658 67.984 A6.996,6.996 0 0,0 27.659,75.827M27.659 75.827 A6.996,6.996 0 0,0 34.940,78.741M34.940 78.741 A39.977,39.977 0 0,1 51.931,78.740M60.452 73.730 A7.268,7.268 0 0,0 57.209,65.704M57.209 65.704 A7.268,7.268 0 0,0 48.587,66.473M48.587 66.473 A7.268,7.268 0 0,0 46.816,74.946M46.816 74.946 A41.262,41.262 0 0,1 46.528,91.093M46.528 91.093 A6.936,6.936 0 0,0 49.806,97.827M49.806 97.827 A6.936,6.936 0 0,0 57.293,97.657M57.293 97.657 A6.936,6.936 0 0,0 60.262,90.781M60.262 90.781 A38.689,38.689 0 0,1 60.452,73.730M46.577 70.415 A7.000,7.000 0 0,0 49.493,77.701M49.493 77.701 A7.000,7.000 0 0,0 57.341,77.701M57.341 77.701 A7.000,7.000 0 0,0 60.257,70.415M60.257 70.415 A40.000,40.000 0 0,1 60.257,53.394M60.257 53.394 A7.000,7.000 0 0,0 57.341,46.108M57.341 46.108 A7.000,7.000 0 0,0 49.493,46.108M49.493 46.108 A7.000,7.000 0 0,0 46.577,53.394M46.577 53.394 A40.000,40.000 0 0,1 46.577,70.415M41.968 20.020 A39.977,39.977 0 0,0 24.977,20.021M24.977 20.021 A6.996,6.996 0 0,1 17.696,17.106M17.696 17.106 A6.996,6.996 0 0,1 17.695,9.264M17.695 9.264 A6.996,6.996 0 0,1 24.975,6.347M24.975 6.347 A40.033,40.033 0 0,0 41.969,6.348M41.969 6.348 A6.995,6.995 0 0,1 49.247,9.265M49.247 9.265 A6.995,6.995 0 0,1 49.246,17.105M49.246 17.105 A6.995,6.995 0 0,1 41.968,20.020"
    #cgoChamber = window.svgToCgoSVG(chamber)
    # -centerx 為 x 座標的 offset 值, 也就是新原點位於 (centerx, centery)
    #cgoChamber = window.svgToCgoSVG(chamber, -centerx, -centery)
    cgoChamber = window.svgToCgoRHC(chamber, -107.373, -91.26)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 放大 2 倍
    cgo.render(cmbr, x, y, 2, rot)

ss1(0, 0, 0, 0, 0, "red", True, 4)
</script>
</body>
</html>
'''
    return outstring
