<strong>第一大題</strong><br><br>


<strong>1.</strong><br>
先在virtual box 設定host only<br>
![0](1.png)<br><br>


進到linux後，用ifconfig -a檢查一下網路資訊，找到正確網路代號，然後下指令：ifconfig enp0s8 192.168.200.100 。 最後再用ifconfig檢查一次是否正確。<br>

![0](2.png)<br><br>




<strong>2.</strong><br>
安裝完後，透過指令：service nginx start chkconfig nginx on 啟動。 <br>

![0](3.png)<br>


透過指令：netstat -nlp | grep 80  驗證。 <br>

![0](4.png)<br><br>






<strong>3.</strong><br>
啟動網頁輸入 http://192.168.200.100 。 連線成功。<br>

![0](5.png)<br><br>






<strong>3.</strong><br>
使用指令curl http://192.168.200.100。 連線成功<br>

![0](6.jpg)<br>








<strong>4.</strong><br>
先訪問錯誤網站：curl 192.168.0.1

使用指令cat /var/log/nginx/access.log 看連線結果<br>
![0](7.png)<br>

再用指令 cat /var/log/nginx/error.log ｜ sort 





