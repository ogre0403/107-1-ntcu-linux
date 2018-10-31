第一題:
(1)用groupadd mygroup;groupadd nogroup建立群組。

(2)用useradd -G mygroup myuser1;useradd -G mygroup myuser2;useradd -G mygroup myuser3建立帳號，並加入mygroup，然後用passwd myuser1;passwd myuser2;passwd myuser3(密碼都是MyPassWord)。

(3)用useradd -G nogroup nouser1;useradd -G nogroup nouser2;useradd -G nogroup nouser3建立帳號，並加入nogroup，然後用passwd nouser1;passwd nouser2;passwd nouser3(密碼都是MyPassWord)。

(4)用mkdir /srv/myproject建立目錄，然後用chgrp mygroup /srv/myproject更改目錄的群組，接著用chmod 770 /srv/myproject讓 mygroup 群組內的使用者完整使用，但其他人沒有任何權限。(可用ls -ld /srv/myproject檢查是否有更改正確)。

(5)改用myuser1登入，然後cd /srv/myproject前往目錄，接著用touch myuser1.data建立檔案，完成後登出myuser1。

(6)用root登入後，用cp /usr/bin/ls /usr/local/bin/myls，接著改用nouser1登入，用sudo chmod u+s /usr/local/bin/myls讓root的x權限變成s，接著切換成nouser1登入，執行myls /srv/myproject，然後就可以查閱到該目錄內的檔名資訊(myuser1.data)。


第二題:
用ps |grep rsyslog找到rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊，接著ps aux | grep rsyslog > /root/process_syslog.txt將檔案轉存過去(可用vi process_syslog.txt檢查是否有儲存)。


第三題:
用find /usr/bin /usr/sbin -perm /4000找出含有 SUID 的特殊檔案檔名，接著用find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \;找出權限，最後用find /usr/bin /usr/sbin -perm/4000 -exec ls -l {} \; > /root/findsuidsgid.txt將資料轉存到 /root/findsuidsgid.txt(可用vi findsuidsgid.txt檢查是否有儲存)。