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
<v t="amd.20160329124554.2" a="E"><vh>@path ./../../../</vh>
<v t="amd.20160329164739.1" a="E"><vh>假如要送到 gh-pages 分支, 使用下列按鈕</vh>
<v t="amd.20160329164739.2"><vh>@button gh-pages pelican</vh></v>
</v>
<v t="amd.20160329163719.1" a="E"><vh>假如要在近端檢視, 使用下列按鈕</vh>
<v t="amd.20160329163719.2"><vh>@button local pelican</vh></v>
</v>
<v t="amd.20160329124849.1"><vh>進入 content 目錄</vh></v>
<v t="amd.20160329124903.1" a="E"><vh>@path content</vh>
<v t="leo.20160414134149.2" a="E"><vh>@path bg11</vh>
<v t="leo.20160414134149.1"><vh>@edit 40323245.md</vh></v>
<v t="544.20160421135227.1"><vh>@edit 40323245_2.md</vh></v>
</v>
</v>
</v>
</vnodes>
<tnodes>
<t tx="544.20160421135227.1">@language md
Title: 40323245 - 期中報告
Category: bg11
Tags: scrum1, task1, 40323245
Author: 40323245


&lt;h3&gt;40323245 - 期中報告&lt;/h3&gt;  


&lt;!-- PELICAN_END_SUMMARY --&gt;
協同繪圖&lt;a href="http://2016spring-40323245.rhcloud.com/bg9/task2_homework"&gt;bg9藍圖&lt;/a&gt; 
&lt;/br&gt;
個人繪圖&lt;a href="http://2016springbg11-40323245.rhcloud.com/bg11/scrum1_task40323245"&gt;scrum1_task40323245&lt;/a&gt;
&lt;/br&gt;
&lt;hr size="1" align="center" noshade width="100%" color=red&gt;
&lt;h2&gt;Gh-pages : &lt;/h2&gt;
&lt;h3&gt;在 gh-pages 裡的user/組別 目錄下 新增個人leo檔案，並將.md檔路徑放在content，至於紅色框框為檔案名稱，很多人都使用日期導致檔案一直覆寫。&lt;/h3&gt;

&lt;h3&gt;和上學期個人md檔相同作法，編輯個人學期心得，並顯示於&lt;/h3&gt;&lt;a href="http://2015fallhw.github.io/cdw2/post/"&gt;cdw2首頁&lt;/a&gt; 

&lt;img src="./../files/bg9/1.png"&gt;

&lt;img src="./../files/bg9/2.png"&gt;
&lt;hr size="1" align="center" noshade width="100%" color=red&gt;


&lt;h2&gt;Master : &lt;/h2&gt;
&lt;h3&gt;用於儲存繪圖程式檔案，並將檔案傳上openshift，能夠在遠端直接顯示圖檔，並能夠導入組員零件，已達成協同要求。
近端要在cdw2目錄下，使用python wsgi.py指令，才能夠在localhost5000顯示個人圖檔。&lt;/h3&gt;
&lt;/br&gt;
&lt;h3&gt;繪圖須註冊藍圖，包括組別與個人，註冊位置在cdw2目錄下之simpleflask.leo&lt;/h3&gt;

&lt;img src="./../files/bg9/3.png"&gt;

&lt;img src="./../files/bg9/4.png"&gt;
&lt;hr size="1" align="center" noshade width="100%" color=red&gt;
&lt;/br&gt;
&lt;/br&gt;
&lt;h2&gt;繪圖 : &lt;/h2&gt;
&lt;h3&gt;此部分依照你的需求，若是使用你的藍圖為主畫布，則使用此串原始碼
若為被導入之零件則刪除(尾端/script也要記得刪)&lt;/h3&gt;
&lt;img src="./../files/bg9/5.png"&gt;

&lt;/br&gt;

&lt;h3&gt;個人檔案  可以使用多個畫布，但導入圖檔畫布要相同&lt;/h3&gt;

&lt;img src="./../files/bg9/6.png"&gt;



&lt;img src="./../files/bg9/8.png"&gt;

&lt;/br&gt;
&lt;h3&gt;會依照導入順序顯示圖形&lt;/h3&gt;


&lt;img src="./../files/bg9/9.png"&gt;

&lt;/br&gt;
&lt;h3&gt;若傳上openshift後，幾天沒有開啟會導致頁面暫時關閉，只需按下重啟即可&lt;/h3&gt;


&lt;img src="./../files/bg9/10.png"&gt;
&lt;/br&gt;
&lt;/br&gt;

&lt;img src="./../files/bg9/ABCD.png"&gt;
&lt;/br&gt;
&lt;/br&gt;
&lt;h3&gt;協同繪圖(可能)使用Allow-Contorl-Allow-Origin功能&lt;/h3&gt;

&lt;img src="./../files/bg9/11.png"&gt;


&lt;/br&gt;
&lt;/br&gt;
&lt;a href="https://github.com/40323250/STL_png/blob/gh-pages/stl/ABCD.stl"&gt;OnshapeABCD組立stl檔案&lt;/a&gt;
&lt;/br&gt;
&lt;h3&gt;A與B的連接部分會有三層，所以有長短軸之分，且一開始就要決定哪一部分為最外層，否則最後接點會重疊&lt;/h3&gt;
&lt;/br&gt;
&lt;/br&gt;
&lt;script src="https://embed.github.com/view/3d/40323250/STL_png/gh-pages/stl/ABCD.stl"&gt;&lt;/script&gt;
&lt;/br&gt;
&lt;/br&gt;
&lt;hr size="1" align="center" noshade width="100%" color=red&gt;
&lt;h3&gt;04/26 02:10 更新&lt;/h3&gt;
&lt;/br&gt;
&lt;h3&gt;協同需要另外設定允許權限&lt;/h3&gt;
&lt;img src="./../files/bg9/code.png"&gt;
&lt;/br&gt;
&lt;/br&gt;
&lt;h3&gt;完成之協同組合圖&lt;/h3&gt;
&lt;img src="./../files/bg9/bg9.png"&gt;








</t>
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
<t tx="leo.20160414134149.1">@language md
Title: 40323245-回報 bg11 初步繪圖主機與連結
Category: bg11
Tags: scrum1, task1, 40323245
Author: 40323245


bg11 組員 40323245 已經在 cdw2 倉儲中的 master 分支建立對應的組員 完成繪圖ABCD字母

&lt;!-- PELICAN_END_SUMMARY --&gt;

目前所完成的 OpenShift 對應繪圖連結: &lt;a href="http://2016springbg11-40323245.rhcloud.com/bg11/scrum1_task40323245"&gt;bg11藍圖&lt;/a&gt; 

個人畫布 : &lt;a href="http://2016springbg11-40323245.rhcloud.com/bg11/scrum1_task40323245"&gt;scrum1_50_ABCD&lt;/a&gt;

字母完成，繪圖部分在旋轉零件時較為複雜，與組員的座標定位也要精確，否則會導致圖形組不起來

繪圖要注意自己的圖形的起始位置，以及複製圖形的旋轉中心，能夠掌握這兩點就能減少繪圖的出錯概率。



</t>
<t tx="leo.20160414134149.2"></t>
</tnodes>
</leo_file>
