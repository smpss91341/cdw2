# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
scrum1_task40123235 = Blueprint('scrum1_task40123235', __name__, url_prefix='/g2', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@scrum1_task40123235.route('/scrum1_task40123235')
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
    #A1 = cmbr.dup()
    #A1.rotate(150)
    #A3 = cmbr.dup()
    #A3.rotate(90)
    #A3.translate(20*math.cos(60*deg), 20*math.sin(60*deg))
    #cmbr.appendPath(A3)
    #cmbr.appendPath(A1)
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    cgo.render(cmbr, x, y, 1, rot)
    # 放大 5 倍
    #cgo.render(cmbr, x, y, 5, rot)

O(0, 0, 0, 0, 0, "yellow", True, 4)
</script>
<!-- 以協同方式加上 g2 的 40123202 組員所寫的 task1 程式碼 -->
<script type="text/python" src="/g2/scrum2_task40123202"></script>
<!-- 以協同方式加上 g2 的 40123214 組員所寫的 task1 程式碼 -->
<script type="text/python" src="/g2/scrum2_task40123214"></script>
<!-- 以協同方式加上 g2 的 40123217 組員所寫的 task1 程式碼 -->
<script type="text/python" src="/g2/scrum2_task40123217"></script>
<!-- 以協同方式加上 g2 的 40123226 組員所寫的 task1 程式碼 -->
<script type="text/python" src="/g2/scrum2_task40123226"></script>
<!-- 以協同方式加上 g2 的 40123232 組員所寫的 task1 程式碼 -->
<script type="text/python" src="/g2/scrum2_task40123232"></script>
<!-- 以協同方式加上 g2 的 40123235 組員所寫的 task1 程式碼 -->
<script type="text/python" src="/g2/scrum2_task40123235"></script>
<!-- 以協同方式加上 g2 的 40123244 組員所寫的 task1 程式碼 -->
<script type="text/python" src="/g2/scrum2_task40123244"></script>
</body>
</html>
'''
    return outstring
    

    
    
