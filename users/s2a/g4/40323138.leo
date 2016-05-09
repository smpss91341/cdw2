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
<v t="amd.20160329174131.1" a="E"><vh>@path ag4</vh>
<v t="amd.20160329174139.1"><vh>@clean 40323138-20160411.md</vh></v>
</v>
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
Title: 40323138-回報 ag4 40323138 期中報告
Category: ag4
Tags: 40323138, task1
Author: 40323138
@others
ag4 組員 40323138 已經在 cdw2 倉儲中的 master 分支建立對應的組員 40323138.leo 並且完成 Task1 的繪圖藍圖建立與註冊
組別繪圖 : http://cdw2fork-40323138.rhcloud.com/ag4/task1
個人繪圖 : http://cdw2fork-40323138.rhcloud.com/ag4_40323138abcd/abcd

&lt;img src="http://imgur.com/nrdvmDL.png="100%" /&gt;

40323109 red   
40323130 Orange 
40323135lightred
40323136lightpink
40323138blue
40323144balck
操作步驟
註冊位置及匯入藍圖(如圖)
&lt;img src="http://imgur.com/F83hvSN.png" width="100%" /&gt;

完成後進入倉儲輸入指令wsgi.py
&lt;img src="http://imgur.com/prjt0Kk.png" width="100%" /&gt;
成功啟動http://127.0.0.1:5000/    反之註冊失敗或程式有錯或顯示失敗無法開啟http://localhost:5000/

後開起瀏覽器
輸入http://localhost:5000/檔案名稱/圖名  如圖
&lt;img src="http://imgur.com/pj0ClSG.png" width="100%" /&gt;

導入HTML語法能在網路上顯示出來
&lt;img src="http://imgur.com/MD0qU0J.png" width="100%" /&gt;

心得報告:
裡面程式相當複雜，一開始沒有很用心去研究，而我又不是組長所以沒有很用心去研究，只好跳出來好好研究程式，研究程式在做什麼，研究到想不透時就去詢問40323131張元旭同學，問了蠻多地方的，要謝謝他的教導，到一定階段後發現其中的一些原理都差不多，後來越來越上手，有學習和了解該得如何去做參數式作圖的。
&lt;!-- PELICAN_END_SUMMARY --&gt;

目前所完成的 OpenShift 對應繪圖連結為: &lt;a href="http://cdw2-ag100.rhcloud.com/ag100/scrum1_task1"&gt;http://cdw2-ag100.rhcloud.com/ag100/scrum1_task1&lt;/a&gt;

其中已經在主程式中導入 scrum1_task1.py 中的 scrum1_task1 藍圖變數, 並且複製範例中的鏈條繪圖 ,準備進一步完成 Task1 協同任務.
</t>
<t tx="amd.20160329211330.1"></t>
</tnodes>
</leo_file>
