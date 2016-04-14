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
<v t="leo.20160310095118.1"><vh>@edit 40123202_w3_1.py</vh></v>
<v t="leo.20160331121254.1"><vh>@edit scrum2_task40123202.py</vh></v>
<<<<<<< HEAD
<v t="leo.20160310095542.1" a="E"><vh>@path ./../../../</vh>
<v t="leo.20160310095553.1"><vh>@edit 2016_cd_2a_3.txt</vh></v>
<v t="leo.20160310095640.1"><vh>@edit cdw2_1.py</vh></v>
=======
<v t="leo.20160412180045.1" a="E"><vh>@path ./../../../</vh>
<v t="leo.20160412180102.1" a="E"><vh>@path content</vh>
<v t="leo.20160412180113.1"><vh>@path bg2</vh></v>
<v t="leo.20160412180137.1"><vh>@clean scrum1-20160412bg2.md</vh></v>
</v>
<v t="leo.20160412180233.1"><vh>進入 content 目錄</vh></v>
<v t="leo.20160412180247.1" a="E"><vh>假如要在近端檢視, 使用下列按鈕</vh>
<v t="leo.20160412180258.1"><vh>@button local pelican</vh></v>
</v>
<v t="leo.20160412180340.1" a="E"><vh>假如要送到 gh-pages 分支, 使用下列按鈕</vh>
<v t="leo.20160412180349.1"><vh>@button gh-pages pelican</vh></v>
</v>
>>>>>>> 46882a9e75aae821be5d46ec1a426bfa3abe0746
</v>
</vnodes>
<tnodes>
<t tx="leo.20160412180045.1"></t>
<t tx="leo.20160412180102.1"></t>
<t tx="leo.20160412180113.1"></t>
<t tx="leo.20160412180137.1">@language md
Title: 40123202scrum1-回報 g2 scrum1 初步繪圖主機與連結
Category: bg2
Tags: scrum1, task1, 4012302
Author: kmol
@others
請注意: 這個 .md 檔案應該要放到 s2b/g2目錄中, 而且用學號作為 Tags 分類讓使用者可以較容易透過 Tags 找到某一學員所提供的所有內容.

bg2 已經在 cdw2 倉儲中的 master 分支建立對應的組員 g2.leo 並且完成 Task1 的繪圖藍圖建立與註冊

&lt;!-- PELICAN_END_SUMMARY --&gt;

目前所完成的 OpenShift 對應繪圖連結為: &lt;a href="http://cdw2-cadp13ag35.rhcloud.com/g2/scrum1_task40123235"&gt;http://cdw2-cadp13ag35.rhcloud.com/g2/scrum1_task40123235&lt;/a&gt;

其中已經在主程式中導入 scrum1_task1.py 中的 scrum1_task1 藍圖變數, 並且複製範例中的鏈條繪圖 ,準備進一步完成 Task1 協同任務.
</t>
<t tx="leo.20160412180233.1"></t>
<t tx="leo.20160412180247.1"></t>
<t tx="leo.20160412180258.1">@language python
import os
#os.system("pelican content -o output -s local_publishconf.py -t theme/pelican-bootstrap3")
os.system("pelican content -o post -s local_publishconf.py")
g.es("admin pelican 近端執行完畢")


</t>
<t tx="leo.20160412180340.1"></t>
<t tx="leo.20160412180349.1">@language python
import os
os.system("pelican content -o post -s publishconf.py")
g.es("admin pelican 執行完畢")

</t>
</tnodes>
</leo_file>
