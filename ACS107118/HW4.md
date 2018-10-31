1.流程一  

(1)使用groupadd 建立群組mygroup與nogroup並使用gpasswd mygroup與gpasswd nogroup設定密碼MyPassWord  

(2)建立使用者myuser1 myuser2 myuser3 nouser1 nouser2 nouser3  

(3)使用gpasswd -M username groupname 將使用者加入群組  

(4)使用mkdir先建立 srv再建立srv/myproject,使用chgrp mygroup srv/myproject 把srv/myproject移動到mygroup裡,再使用chmod 770 srv/myproject 更改權限  

(5)使用exit登出root暫時切換成為myuser1的身分，並且使用 cd /srv/myproject 這個指令前往檔案/ srv / myproject目錄,建立一個名為myuser1.data的檔案

(6)之後登出myuser1,接下來用su - root登入root帳號  

(7)用 cp 這隻指令來複製題目要求的東西到要求的區域  

(8)題目要求的動作記得要執行,確認 nouser1 這隻帳號的權限能不能使用  

2.流程二

(1)使用 ps aux | grep rsyslog>/root/process_syslog.txt 找到跟 rsyslog 相關的東西,並且存取

3.流程三

(1)用 find/usr/bin -prem /u=s -exec is -l {} \ ; > /root/findsuidsgid.txt 找出包含suid檔名的檔案,列出之後轉存到指令上的路徑  

(2)用 find/usr/bin -prem /u=s -exec is -l {} \ ; >> /root/findsuidsgid.txt 找出包含suid檔名的檔案,列出之後轉存到指令上的路徑  

(3)最後用 cat /root/findsuidsgid.txt 檢查成功與否

