<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="leo.20160421090922.3"><vh>因為位於 users/s2a/g100 目錄, 必須跳三層才到外圍</vh></v>
<v t="leo.20160421090946.1" a="E"><vh>@path ./../../../</vh>
<v t="leo.20160421090953.1" a="E"><vh>假如要送到 gh-pages 分支, 使用下列按鈕</vh>
<v t="leo.20160421091015.1"><vh>@button gh-pages pelican</vh></v>
</v>
<v t="leo.20160421091037.1" a="E"><vh>假如要在近端檢視, 使用下列按鈕</vh>
<v t="leo.20160421091049.1"><vh>@button local pelican</vh></v>
</v>
<v t="leo.20160421091113.1"><vh>進入 content 目錄</vh></v>
<v t="leo.20160421091128.1" a="E"><vh>@path content</vh>
<v t="leo.20160421091141.1" a="E"><vh>@path bg2</vh>
<v t="leo.20160421091214.1"><vh>@clean 40123202_2.md</vh></v>
</v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="leo.20160421090922.3"></t>
<t tx="leo.20160421090946.1"></t>
<t tx="leo.20160421090953.1"></t>
<t tx="leo.20160421091015.1">@language python
import os
os.system("pelican content -o post -s publishconf.py")
g.es("admin pelican 執行完畢")

</t>
<t tx="leo.20160421091037.1"></t>
<t tx="leo.20160421091049.1">@language python
import os
#os.system("pelican content -o output -s local_publishconf.py -t theme/pelican-bootstrap3")
os.system("pelican content -o post -s local_publishconf.py")
g.es("admin pelican 近端執行完畢")


</t>
<t tx="leo.20160421091113.1"></t>
<t tx="leo.20160421091128.1"></t>
<t tx="leo.20160421091141.1"></t>
<t tx="leo.20160421091214.1">@language md
Title: 40123202 - 期中報告
Category: bg2
Tags: scrum1, task1, 40123202
Author: 40123202
@others


期中報告

&lt;!-- PELICAN_END_SUMMARY --&gt;

自評分數85

期中報告操作流程：

md檔從2015fallhwfork cdw2並且git clone下來切換分支到 gh-pages,在content目錄下新增組別資料夾

&lt;img src="./../files/bg2/1.png"&gt;

在cdw2=&gt;users=&gt;s2b=&gt;bg2下新增個人的.leo檔,在裡面新增md檔,將期中自評內容打進去

&lt;img src="./../files/bg2/2.png"&gt;

繪製2D-ABCD

繪製自己負責的部分，需在master分支下執行,需先在myflaskapp.py註冊各組組員的檔案如圖所示

&lt;img src="./../files/bg2/3.png"&gt;

&lt;img src="./../files/bg2/4.png"&gt;

&lt;img src="./../files/bg2/9.png"&gt;

繪圖程式採用老師給的scrum1及scrum2,scrum1放在組別leo裡作為統組所有組員scum2的內容所用

&lt;img src="./../files/bg2/5.png"&gt;

&lt;img src="./../files/bg2/6.png"&gt;

而每位組員的scrum2則繪製ABCD各部位所用

&lt;img src="./../files/bg2/7.png"&gt;

上述完成後須先python wsgi.py在近端測試可否執行，如果可執行，會在localhost:5000/g2/scrum1_task40123235顯示出來。

&lt;img src="./../files/bg2/8.png"&gt;

近端測試完後即可推上openshift的遠端網頁:&lt;a href="http://cdw2-cadp13ag35.rhcloud.com/g2/scrum1_task40123235"&gt;bg2-openshift&lt;/a&gt; 

個人ABCD畫布

&lt;img src="./../files/bg2/ABCD.PNG"&gt;

Onshape繪製3D鍊條組立ABCD

&lt;a href="https://cad.onshape.com/documents/57182837e4b09398edad79e9"&gt;Onshape3D鏈條組立&lt;/a&gt; 

&lt;img src="./../files/bg2/A.PNG"&gt;

&lt;img src="./../files/bg2/B.PNG"&gt;

&lt;img src="./../files/bg2/C.PNG"&gt;

&lt;img src="./../files/bg2/D.PNG"&gt;


心得：

　　在onshape的操作上因為是第一次接觸，所以研究了一下，雖然可能不是最正確的方法，但也是盡力組立了ABCD。
　　2D組立則是抓準點的座標才會變得比較容易一些，協同組立有點難。
</t>
</tnodes>
</leo_file>
