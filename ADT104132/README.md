# HW5
### 使用ubuntu

1</br>
* 查閱檔案</br>
<pre><code>ls -ali /etc/hosts</code></pre>
![1](img/1.png)</br>
incode 為 664，共一個使用者</br>
* 實體連結
<pre><code>ln etc/hosts srv/host.hard</code></pre>
![2](img/2.png)</br>
incode 為 664，共3名使用者</br>
是完全連結，屬於同一個檔案，資料相同</br>
* 符號連結
<pre><code>ln -s etc/hosts srv/host.soft</code></pre>
![3](img/3.png)</br>
incode 為 302187，共3名使用者</br>
像是捷徑一樣，抓取檔案，但屬於個體，若原檔刪除，符號連結的檔案就無法開啟</br>
