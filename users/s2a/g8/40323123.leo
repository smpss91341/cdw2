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
<v t="amd.20160408224929.1"><vh>@edit 40323123-20160411.md</vh></v>
<v t="amd.20160329174131.1" a="E"><vh>@path ag8</vh>
<v t="amd.20160329174139.1"><vh>@clean 40323123-20160411.md</vh></v>
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
Title: 40323123-期中報告內容
Category: ag8
Tags: 40323123, Middle test
Author: 40323123
@others
ag8 組員 40323123 已經在 cdw2 倉儲中的 master 分支建立對應的組員 40323123.leo 並且完成 其中自評

&lt;!-- PELICAN_END_SUMMARY --&gt;
Onshape組裝與繪畫
============
由組員進行協同分配繪畫零組件與設計
組合圖如下圖所示
&lt;img src="./../files/ag8Files/Onshape_assamble.png"&gt;



組裝影片
============
&lt;iframe width="560" height="315" src="https://www.youtube.com/embed/1TnbR-ICf2E" frameborder="0" allowfullscreen&gt;&lt;/iframe&gt;


目前所完成的 OpenShift 對應繪圖連結為: &lt;a href="http://dwaring-40323123.rhcloud.com/ag100/scrum1_task1"&gt;http://dwaring-40323123.rhcloud.com/&lt;/a&gt;



</t>
<t tx="amd.20160329211330.1"></t>
</tnodes>
</leo_file>
