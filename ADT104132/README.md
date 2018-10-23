# HW3
### 使用ubuntu
一</br>
* 先建立三個用戶，密碼皆為ItLsExam</br>
<pre><code>adduser examuser1
密碼 : ItLsExam</code></pre>
![01](img/01.png)</br>
2,3以此類推</br>
![02](img/02.png)</br>
* 刪除系統中的 examuser3 這個帳號，使用[-r]將這個帳號的家目錄同步刪除</br>
<pre><code>userdel -r examuser3</code></pre>
![03](img/03.png)</br>
* 誤刪examuser3，在ubuntu下，若未完全刪除，再次使用[adduser]會重建該帳號</br>
<pre><code>userdel examuser1</code></pre>
![04](img/04.png)</br>
<pre><code>adduser examuser1
密碼 : ItLsExam</code></pre>
![05](img/05.png)</br>

二</br>
* 創建examuser4如同前面所敘</br>
更改使用者&權限以及group</br>
<pre><code>chown examuser4 securetty
chmod 777 securetty
charp 1004 securetty</code></pre>
![07](img/07.png)</br>
![08](img/08.png)</br>
* 建立 /examdata/change.txt，擁有者為sshd，擁有群組為users，sshd 可讀可寫，users 群組成員可讀，其他人沒權限。
<pre><code>mkdir examdata
cd examdata
touch change.txt</code></pre>
![09](img/09.png)</br>
更改使用者、group以及日期</br>
<pre><code>chown sshd change.txt
charp users change.txt
touch -t 201212211200 change.txt</code></pre>
![010](img/10.png)</br>

三</br>
* 建立檔案 & 複製 & 更改使用權限/etc/hosts
<pre><code>cp /etc/hosts ./dir1/file1</code></pre>
![011](img/11.png)</br>
![012](img/12.png)</br>
![013](img/13.png)</br>
<pre><code>cp /etc/hosts ./dir1/file1</code></pre>
* 使用 ls -l /dev/shm/unit05/dir[1-4]</br>
![014](img/14.png)</br>
fire1 可讀不可執行，所以只到有甚麼東西</br>
file2 可執行但不可讀，無法知道內容</br>
file3、file4 皆可讀可執行，可知道內容</br>
* 使用 ls -l /dev/shm/unit05/dir1/file[1~4]</br>
![015](img/15.png)</br>
file1因dir1無法執行，所以看不到</br>
file2、file3、file4因各個dir都能執行，皆能再往裡面探勘</br>
* vim /dev/shm/unit05/dir[1~4]/file[1~4]</br>
![016](img/16.png)</br>
![017](img/17.png)</br>
![018](img/18.png)</br>
