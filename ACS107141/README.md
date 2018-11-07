##HW-3

<ol>
<li>輸入"ls -ali /etc/hosts"</li>
![](https://i.imgur.com/u03xGHq.png)
<p>最前面的數字為inode</p>
<p>1個檔名在使用</p>
</ol>

<ol>
<li>輸入"ln /etc/hosts /srv/hosts.hard"建立實體連結</li>
<li>輸入"ls -ali /srv/hosts.hard"</li>
![](https://i.imgur.com/AAzOcjO.png)
<p>最前面的數字為inode</p>
<p>2個檔名在使用</p>
*/etc/hosts和建立的實體連結/srv/hosts.hard都在使用，所以有兩個檔名
</ol>

<ol>
<li>輸入"ln -s /etc/hosts /srv/hosts.soft"建立符號連結</li>
<li>輸入"ls -ali /srv/hosts.soft"</li>
![](https://i.imgur.com/n2NKr6b.png)
<p>最前面的數字為inode</p>
*符號連結為獨立的檔案，所以不會像實體連結一樣共用同一個inode
</ol> 
