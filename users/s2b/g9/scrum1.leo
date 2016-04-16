<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<?xml-stylesheet ekr_test ?>
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5" body_secondary_ratio="0.5">
	<global_window_position top="50" left="50" height="500" width="700"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="amd.20160329211330.1"><vh>因為位於 users/s2a/g100 目錄, 必須跳三層才到外圍</vh></v>
<v t="amd.20160329124554.2" a="E"><vh>@path ./../../../</vh>
<v t="amd.20160329164739.1" a="E"><vh>假如要送到 gh-pages 分支, 使用下列按鈕</vh>
<v t="amd.20160329164739.2"><vh>@button gh-pages pelican</vh></v>
</v>
<v t="amd.20160329163719.1" a="E"><vh>假如要在近端檢視, 使用下列按鈕</vh>
<v t="amd.20160329163719.2"><vh>@button local pelican</vh></v>
</v>
<v t="amd.20160329124849.1"><vh>進入 content 目錄</vh></v>
<v t="amd.20160329124903.1" a="E"><vh>@path content</vh>
<v t="amd.20160329174131.1"><vh>@path ag100</vh></v>
<v t="amd.20160329174139.1"><vh>@clean 40323250.md</vh></v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="amd.20160329124554.2"></t>
<t tx="amd.20160329124849.1"></t>
<t tx="amd.20160329124903.1"></t>
<t tx="amd.20160329163719.1"></t>
<t tx="amd.20160329163719.2">@language python
import os
#os.system("pelican content -o output -s local_publishconf.py -t theme/pelican-bootstrap3")
os.system("pelican content -o post -s local_publishconf.py")
g.es("admin pelican 近端執行完畢")


</t>
<t tx="amd.20160329164739.1"></t>
<t tx="amd.20160329164739.2">@language python
import os
os.system("pelican content -o post -s publishconf.py")
g.es("admin pelican 執行完畢")

</t>
<t tx="amd.20160329174131.1"></t>
<t tx="amd.20160329174139.1">@language md
Title: 40323250-回報 bg9 初步繪圖主機與連結
Category: bg9
Tags: scrum1, task1, 40323250
Author: kmol
@others

bg9 組員 40323250 已經在 cdw2 倉儲中的 master 分支建立對應的組員 暫時完成繪圖AB字母

&lt;!-- PELICAN_END_SUMMARY --&gt;

目前所完成的 OpenShift 對應繪圖連結: &lt;a href="http://2016spring-40323250.rhcloud.com/bg9/task2"&gt;bg9藍圖&lt;/a&gt; 

個人畫布 : &lt;a href="http://2016spring-40323250.rhcloud.com/bg9/scrum1_test"&gt;scrum1_50_fortest&lt;/a&gt;

目前完成兩個字母，但是都以非常耗時的方式繪圖，在旋轉零件部分較為複雜，與組員的座標定位也要準確，否則會導致圖形組不起來

繪圖要注意自己的圖形的起始位置，以及複製圖形的旋轉中心，能夠掌握這兩點就能減少繪圖的出錯率。

暫時先做到這邊。

</t>
<t tx="amd.20160329211330.1"></t>
</tnodes>
</leo_file>
