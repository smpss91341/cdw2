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

2D協同繪圖設計:
目前所完成的 OpenShift 對應繪圖連結為: &lt;a href="http://dwa-40323123.rhcloud.com/ag8/task1All"&gt;http://dwa-40323123.rhcloud.com/ag8/task1All&lt;/a&gt;
導入openshift並啟動2D協同繪圖的wsgi
步驟:
~~~script
1.先git clone cdw2的程式碼

2.確定可以用python wsgi.py執行

3.開啟OpenShift並且新增一個python3的程式

4.在中間可以看到open source URL →URL填你copy的網址

5.如果順利成功可以看到網頁已經建立成功了~接著打你們的網址列就可以看到2D的圖形顯示了

6.如果要進行修改，必須進入setting新增公私鑰(public key) (private key)

7.如果沒有，使用putty genrate去產生key，複製public key到網址上add public key的地方

8.Export OpenSSH到 Home/.ssh/id_rsa

9.接著就可以進行存取git clone ssh/~~~~~

10.進去資料夾下git rm -rf *  (強制刪除全部)

11.在將更改好的資料複製到資料夾，下git push 就會更新OpenShift中的網站

※主要下git rm all的原因是因為怕資料衝突，那部分要解比較困難，因為有些要遵守的規則和設定上的使用。

~~~
&lt;br /&gt;


協同畫完的ABCD
&lt;img src="./../files/ag8Files/2Ddwaring.png"&gt;

&lt;!-- PELICAN_END_SUMMARY --&gt;
Onshape組裝與繪畫
============
由組員進行協同分配繪畫零組件與設計
組合圖如下圖所示
&lt;img src="./../files/ag8Files/Onshape_assamble.png"&gt;
四個零組件ABCD
&lt;img src="./../files/ag8Files/Onshape_assamble_a.png"&gt;
&lt;img src="./../files/ag8Files/Onshape_assamble_b.png"&gt;
&lt;img src="./../files/ag8Files/Onshape_assamble_c.png"&gt;
&lt;img src="./../files/ag8Files/Onshape_assamble_d.png"&gt;

組裝影片
============
&lt;iframe width="560" height="315" src="https://www.youtube.com/embed/1TnbR-ICf2E" frameborder="0" allowfullscreen&gt;&lt;/iframe&gt;






</t>
<t tx="amd.20160329211330.1"></t>
</tnodes>
</leo_file>
