### HW7

1.(1)用程式碼<br/>
<pre><code># curl -O 網址</code></pre>
下載日誌檔<br/>
![01](HW7/01.png)<br/>
(2)用程式碼<br/>
<pre><code># cat web.log</code></pre>
顯示error的原因<br/>
![02](HW7/02.png)<br/>
2.(1)用程式碼<br/>
<pre><code># tar -cvf var.tar /var 2> tar-err.log</code></pre>
製成壓縮檔<br/>
![03](HW7/03.png)<br/>
檢查是否成功<br/>
![04](HW7/04.png)<br/>
用程式碼<br/>
<pre><code># cat tar-err.log</code></pre>
抓出檔案中的錯誤，並且輸出<br/>
![05](HW7/05.png)<br/>