### HW5

1.<br/>
1.(1)用程式碼<br/>
<pre><code># ls -ali 檔案位置</code></pre>
查看/etc/hosts檔案的inode<br/>
inode號碼為 131237<br/>
(2)目前共有一個檔名在使用<br/>
![01](HW5/01.png)<br/>
2.(1)用程式碼<br/>
<pre><code># ln 原本檔案位置 複製檔案位置</code></pre>
做實體連結，/srv/hosts.hard的inode為 131237<br/>
(2)目前共有兩個檔名在使用<br/>
(3)因為hard link是把原本檔案、複製檔案都連結到同一個inode<br/>
所以兩個檔案的資料會相同，你刪掉任何一個檔名，inode及block還是存在<br/>
![02](HW5/02.png)<br/>
3.(1)用程式碼<br/>
<pre><code># ln -s 原本檔案位置 複製檔案位置</code></pre>
做符號連結，/srv/hosts.soft的inode為134058<br/>
(2)目前共有一個檔名在使用<br/>
(3)因為soft link是利用檔案做指向動作，所以inode會不同<br/>
如果指向地原本檔案刪除，那麼複製的檔案就打不開<br/>
![03](HW5/03.png)<br/>