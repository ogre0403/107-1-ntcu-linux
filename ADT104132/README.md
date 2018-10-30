# HW4
### 使用ubuntu

1</br>

* 建立群組 mygroup、nogroup，grep查看group是否存在</br>
<pre><code>groupadd mygroup
grep mygroup /etc/group</code></pre>
![1](img/1.png)</br>
* 建立帳號 myuser1~3，加入 mygroup，密碼為 MyPassWord，2、3以此類推</br>
<pre><code>useradd -m -G mygroup myuser1
passwd myuser1</code></pre>
![2](img/2.png)</br>
* 建立帳號 nouser1~3，加入 nogroup，密碼為 MyPassWord，2、3以此類推</br>
<pre><code>useradd -m -G nogroup myuser1
passwd nouser1</code></pre>
![3](img/3.png)</br> 
* 切換至myuser1 前往 /srv/myproject 建 myproject.data</br>
先更改權限</br>
<pre>chgrp mygroup myproject
chmod 770 myproject</pre>
![4](img/4.png)</br>
再進入 myuser1</br>
<pre>touch myproject.data</pre>
![5](img/5.png)</br>
* 復制/usr/bin/ls至/usr/local/bin/myls...</br>
<pre>cp -r /usr/bin/ls /local/bin/myls
chmod 4755 myls</pre>
![6](img/6.png)</br>

2</br>
<pre>ps aux | grep rsyslog
ps aux | grep rsyslog > /root/preocess_syslog.txt
cat /root/process_syslog.txt</pre>
grep 分類查詢</br>
>重新導向至後面內容</br>
cat 查看後面檔案內容</br>
![7](img/7.png)</br>

3</br>
<pre>find /usr/bin -perm /u=s</pre>
find 是主要使用的搜尋指令 後面加查詢事物</br>
-perm 是指定檔案權限</br>
/u=s 即為 含有SUID的特殊檔案</br>
![8](img/8.png)</br>
<pre>find /usr/bin -perm /u=s -ok ls -l > findsuidsgid.txt
find /usr/bin -perm /u=s -ok ls -l 1>> findsuidsgid.txt</pre>
兩句差別在 > 1>></br>
上面是顯示每筆，下面則是顯示一筆</br>
![9](img/9.png)</br>
<pre>cat findsuidsgid.txt</pre>
![10](img/10.png)</br>
