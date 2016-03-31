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
<v t="amd.20160329174131.1" a="E"><vh>@path ag100</vh>
<v t="amd.20160330231545.1"><vh>@clean scrum2-20160330.md</vh></v>
<v t="amd.20160330205248.1"><vh>@clean scrum2-20160330-1.md</vh></v>
<v t="amd.20160329174139.1"><vh>@clean scrum2-20160330-2.md</vh></v>
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
Title: scrum2-再次利用 pull request 要求合併 gh-pages 分支中的改版資料
Category: ag100
Tags: scrum2, task1
Author: kmol
@others
假如各組員分別在各自同時段 fork 的版本持續工作, 則組長必須擔負以手動解決合併的工作

&lt;!-- PELICAN_END_SUMMARY --&gt;

各組員在建立 pull request 時, 一定要確定 base fork 與 head fork 的對應分支, master  對 master, gh-pages 對 
gh-pages, 而且基本的請求是要從 head fork 將版本要求合併到 base fork 中.
</t>
<t tx="amd.20160329211330.1"></t>
<t tx="amd.20160330205248.1" markdown-import="7d7100580e000000756e6465726c696e655f6469637471017d710258150000006d61726b646f776e206465636c61726174696f6e7371034e73732e">Title: scrum2-希望採 pull request 方式合併 gh-pages 網頁資料
Category: ag100
Tags: scrum2, task1
Author: kmol
目前 scrum2 只能透過 pull request 將新版本資料合併到全班的 gh-pages 網頁, 這一篇就是希望測試流程中的實際操作步驟

&lt;!-- PELICAN_END_SUMMARY --&gt;

以及組員與組長必須在流程中操作的步驟.

因為 gh-pages 中的 Pelican 靜態網頁可能無法直接在線上合併, 但是各用戶只要把握以 content 目錄中的 md 檔案為主, 而其他 post 目錄下的各 html 與頁面檔案, 都是從 .md 檔案與設定檔案, 透過 pelican 指令產生, 因此解決衝突的重點在 content 目錄中的 .md 檔案而非 post 目錄中的檔案.</t>
<t tx="amd.20160330231545.1">@language md
Title: scrum2-回報 ag100 scrum2 與 scrum1 繪圖結合
Category: ag100
Tags: scrum2, task1
Author: kmol
@others
ag100 組員 scrum2 已經在 cdw2 倉儲中的 master 分支建立對應的組員 scrum2.leo 並且完成 Task1 的繪圖藍圖建立與註冊

&lt;!-- PELICAN_END_SUMMARY --&gt;

已經將 scrum2 繪圖的部份納入, 並且塗上淡綠色: &lt;a href="http://cdw2-ag100.rhcloud.com/ag100/scrum1_task1"&gt;http://cdw2-ag100.rhcloud.com/ag100/scrum1_task1&lt;/a&gt;

其中已經在主程式中導入 scrum2_task1.py 中的 scrum2_task1 藍圖變數, 並且複製範例中的鏈條繪圖 ,準備進一步完成 Task1 協同任務.
</t>
</tnodes>
</leo_file>
