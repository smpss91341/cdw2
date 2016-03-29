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
<v t="amd.20160329124554.2" a="E"><vh>@path ./../</vh>
<v t="amd.20160329164739.1" a="E"><vh>假如要送到 gh-pages 分支, 使用下列按鈕</vh>
<v t="amd.20160329164739.2"><vh>@button gh-pages pelican</vh></v>
</v>
<v t="amd.20160329163719.1" a="E"><vh>假如要在近端檢視, 使用下列按鈕</vh>
<v t="amd.20160329163719.2"><vh>@button local pelican</vh></v>
</v>
<v t="amd.20160329124849.1"><vh>進入 content 目錄</vh></v>
<v t="amd.20160329124903.1" a="E"><vh>@path content</vh>
<v t="amd.20160329174131.1" a="E"><vh>@path user1</vh>
<v t="amd.20160329174139.1"><vh>@clean user1-20160329.md</vh></v>
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
Title: user1-測試 content 目錄下的 md 檔案轉換
Category: ag1
Tags: 範例, task1
Author: kmol
@others
網站類別分為 ag1~ag10, bg1~bg10, 與 MISC, 各組員必須透過 Leo Editor, Pelican,  與 Github pull requests 完成.

&lt;!-- PELICAN_END_SUMMARY --&gt;

CDW2 網頁: &lt;a href="http://2015fallhw.github.io/cdw2/"&gt;http://2015fallhw.github.io/cdw2/&lt;/a&gt;

二甲文章類別: ag1~ag10

二乙文章類別: bg1~bg10

本網頁將 Pelican 設定分為本地端與 gh-pages 端的原因在於 disqus 設定, 本地端無需 disqus 討論功能, 而 gh-pages 端則需要網址全稱才能正確與 disqus 設定連結, 因此所有使用者在近端檢視時, 必須採用近端的按鈕, 而要送到遠端前則必須要用遠端按鈕產生所需要的 post 目錄下的所有資料後, 再提交推送.

以下為圖片引用方法, 建議放到 files 目錄下, 並且用相對目錄引用各自放在以用戶名稱命名的子目錄中, 以避免多用戶因採相同檔名而覆寫:

&lt;pre class="brush: python;"&gt;
&lt;img src="./../files/user1/github.png" /&gt;
&lt;/pre&gt;

得到結果如下:

&lt;img src="./../files/user1/github.png" /&gt;

以下資料則從原先的 cdw2 gh-pages 分支中的 index.html 取出:

cdw2 所在倉儲: &lt;a href="https://github.com/2015fallhw/cdw2"&gt;https://github.com/2015fallhw/cdw2&lt;/a&gt;

以下繪圖由 s2a 的 g100 組所完成, 其中包括 s2b 的 g99 協同繪圖 (藍色零件). &lt;br /&gt;&lt;br /&gt;
&lt;a href="http://cdw2-ladisai.rhcloud.com/ag100/task2"&gt;http://cdw2-ladisai.rhcloud.com/ag100/task2&lt;/a&gt;
&lt;br /&gt;&lt;br /&gt;
以下則為4個零件中的第一個弧參數設定比較:
&lt;ol&gt;
&lt;li&gt;0(表示 x 軸轉角為0), 1(第一個選擇長度較大的弧), 0(且以右手向內畫弧)&lt;/li&gt;
&lt;li&gt;0(表示 x 軸轉角為0), 0(第一個選擇長度較小的弧), 0(且以右手向內畫弧)&lt;/li&gt;
&lt;li&gt;0(表示 x 軸轉角為0), 1(第一個選擇長度較大的弧), 1(且以右手向外畫弧)&lt;/li&gt;
&lt;li&gt;0(表示 x 軸轉角為0), 0(第一個選擇長度較小的弧), 1(且以右手向外畫弧)&lt;/li&gt;
&lt;/ol&gt;
&lt;a href="http://cdw2-ladisai.rhcloud.com/bg99/fourchain"&gt;http://cdw2-ladisai.rhcloud.com/bg99/fourchain&lt;/a&gt;
&lt;br /&gt;
&lt;br /&gt;
Task1 相關: &lt;a href="https://cmsimply-cadlab.rhcloud.com/get_page?heading=2016springCD"&gt;https://cmsimply-cadlab.rhcloud.com/get_page?heading=2016springCD&lt;/a&gt;
&lt;br /&gt;
&lt;br /&gt;
鍊條零件製造流程:
&lt;br /&gt;
&lt;br /&gt;
&lt;iframe width="560" height="315" src="https://www.youtube.com/embed/h8j5-dC6_x8" frameborder="0" allowfullscreen&gt;&lt;/iframe&gt;
&lt;br /&gt;
&lt;br /&gt;
組立流程:
&lt;br /&gt;
&lt;br /&gt;
&lt;iframe width="560" height="315" src="https://www.youtube.com/embed/ZwTryvdmzD4" frameborder="0" allowfullscreen&gt;&lt;/iframe&gt;

如何協同編輯 CADLAb 手冊:
</t>
</tnodes>
</leo_file>
