### HW3

1.(1)用程式碼<br/>
<pre><code># adduser 名稱</code></pre>
來建立examuser1,examuser2,examuser3，三個帳號
![01](HW3/01.PNG)<br/>
![02](HW3/02.PNG)<br/>
![03](HW3/03.PNG)<br/>
(2)用程式碼<br/>
<pre><code># userdel -r 名稱</code></pre>
來刪掉examuser3這個帳號，且同時刪除家目錄與郵件檔案同步<br/>
如果不想把家目錄與郵件檔案同步刪除的話，不要打-r即可
![04](HW3/04.PNG)<br/>
(3)用程式碼<br/>
<pre><code># userdel 名稱</code></pre>
來刪除examuser1這個帳號，但是家目錄要保留，在直接用程式碼<br/>
<pre><code># adduser 名稱</code></pre>
就可以把原本的examuser1帳號建立回來，且UID、GID跟原本也一樣<br/>
![05](HW3/05.PNG)<br/>

2.(1)用程式碼<br/>
<pre><code># adduser 名稱</code></pre>
來建立examuser4這個帳號<br/>
![06](HW3/06.PNG)<br/>
(2)用程式碼<br/>
<pre><code># cp -r 原本位置 複製位置</code></pre>
將資料夾複製給examuser4帳號下的資料夾<br/>
![07](HW3/07.PNG)<br/>
用程式碼<br/>
<pre><code># chown 修改檔案擁有者 資料夾名稱</code></pre>
來改變資料夾的擁有者帳號<br/>
![08](HW3/08.PNG)<br/>
用grep判別有沒有這個group，再用程式碼<br/>
<pre><code># chgrp group名稱 資料夾名稱</code></pre>
去修改檔案擁有者的群組帳號
![09](HW3/09.PNG)<br/>
最後用程式碼<br/>
<pre><code># chmod 777 資料夾名稱</code></pre>
去改資料夾的權限<br/>
![10](HW3/10.PNG)<br/>
(3)用vim建立change.txt的空檔案，再把檔案擁有者修改為sshd<br/>
群組名稱改為users，sshd的權限為6代表可讀可寫<br/>
users的權限為4代表可讀而已，其他人為沒權限，最後用程式碼<br/>
<pre><code># userdel touch -t 時間 檔案名稱</code></pre>
去改變檔案的修改日期<br/>
![11](HW3/11.PNG)<br/>

3.先建立資料夾且給它權限、複製資料夾<br/>
![12](HW3/12.PNG)<br/>
![13](HW3/13.PNG)<br/>
(1)因為我們把使用者帳號換為examuser1，且不在群組內，所以為外人<br/>
dir1的權限是r--，只能看到裡面有檔案但是無法執行<br/>
dir2的權限是--r，可以執行但是無法閱覽<br/>
dir3的權限是r-x，為可讀可執行，所以可以看到資訊<br/>
dir4的權限是rwx，為可讀可寫可執行，也可以看到資訊<br/>
![14](HW3/14.PNG)<br/>
(2)dir1的目錄可讀但不可執行，所以沒辦法取得file1的檔案<br/>
file2、file3、file4因為目錄都是有x權限為可執行，所以都能夠取的檔案<br/>
![15](HW3/15.PNG)<br/>
(3)只有file4為rwx權限，所以才能改寫裡面的內容<br/>
![16](HW3/16.PNG)<br/>
![17](HW3/17.PNG)<br/>
![18](HW3/18.PNG)<br/>
![19](HW3/19.PNG)<br/>
