##1 
#建立群組
	<ol>
	<li>輸入groupadd mygroup</li>
	<li>輸入groupadd nogroup</li>
	<li>輸入grep group /etc/group確認有沒有成功加入</li>
	<li><p>輸入useradd -g mygroup myuser1</p>
		<p>輸入useradd -g mygroup myuser2</p>
		<p>輸入useradd -g mygroup myuser3</p>
		<p>輸入useradd -g nogroup nouser1</p>
		<p>輸入useradd -g nogroup nouser1</p>
		<p>輸入useradd -g nogroup nouser1</p></li>
	</ol>	
#設定密碼(皆為MyPassWord)	
	<ol>
	<li><p>輸入passwd myuser1</p>
		<p>輸入passwd myuser2</p>
		<p>輸入passwd myuser3</p>
		<p>輸入passwd nouser1</p>
		<p>輸入passwd nouser1</p>
		<p>輸入passwd nouser1</p></li>
	</ol>	
#檢查使用者是否在正確的群組內 
	<ol>
	<li><p>輸入ll /home/</p>
		<p>應顯示</p>
		<p>drwx------. 2	myuser1	mygroup	62 日期	時間	myuser1</p> 
		<p>drwx------. 2	myuser2	mygroup	62 日期	時間	myuser2</p>
		<p>drwx------. 2	myuser3	mygroup	62 日期	時間	myuser3</p> 
		<p>drwx------. 2	nouser1	nogroup	62 日期	時間	nouser1</p> 
		<p>drwx------. 2	nouser2	nogroup	62 日期	時間	nouser2</p> 
		<p>drwx------. 2	nouser3	nogroup	62 日期	時間	nouser3</p></li>
	</ol>	
#建立目錄	 
	<ol>
	<li>輸入mkdir -m 070 /srv/myproject</li>
	<li>輸入chgrp mygroup /srv/myproject</li>
	<li><p>輸入ll /srv</p>
		<p>應會顯示</p>
		<p>d---rwx---. 2	root	mygroup 6	日期	時間	myproject</p></li>
	</ol>
#登入myuser1並建檔 
	<ol>
	<li>輸入su myuser1</li>
	<li>輸入cd /srv/myproject</li>
	<li>輸入touch myuser1.data</li>
	<li><p>輸入ll /srv/myproject</p>
		<p>應顯示</p>
		<p>-rw-r--r--. 1	myuser1	mygroup	0	日期	時間	myuser1.data</li>
	<li>切回root輸入cp /usr/bin/ls /user/local/bin/myls複製檔案</li>
	<li><p>輸入ll /usr/local/bin</p>
		<p>應顯示</p>
		<p>-rwxr-xr-x. 1	root	root	117672	日期	時間	myls</v></li>
	</ol>	
#修改u權限令nouser1可使用/srv/myproject		
	<ol>
	<li>輸入chmod u+s /usr/local/bin/myls</li>
	<li><p>輸入ll /usr/local/bin/myls</p>
		<p>應顯示</p>
		<p>-rwsr-xr-x. 1	root	mygroup	117672	日期	時間	/usr/local/bin/myls</li>
	</ol>
#切換成nouser1測試		
	<ol>
	<li>輸入myls /srv/myproject出現myuser1.data即成功</li>
	</ol> 

##2
#使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。
	<ol>
	<li>輸入ps aux |grep rsyslog</li>	
	<li>輸入ps aux |grep rsyslog > /root/process_syslog.txt</li>
	<li>輸入cat/root/process_syslog.txt</li>
![](https://i.imgur.com/eJ0ngAA.png)
	</ol>
	
##3	
	<ol>
	<li>輸入top</li>
![](https://i.imgur.com/f9iqLnB.png)	
