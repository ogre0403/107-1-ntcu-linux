1.輸入groupadd mygroup，再輸入groupsdd nogroup以建立mygroup和nogroup這兩個群組，
再輸入useradd -g mygroup myuser1, myuser2, myuser3來建立這三個帳號，
再輸入passwd myuser1，然後輸入MyPassWord，設定成為這個帳號的密碼，myuser2跟myuser3的密碼也依此設定。
2.接著換在nogroup建立nouser1, nouser2, nouser3這三個帳號，
依上述的方法，輸入usersdd -g nogroup nouser1 nouser2 nouser3，
輸入passwd nouser1來設定此帳號密碼，輸入MyPassWord作為此帳號的密碼，將nouser2, nouser3的密碼也依照此步驟改成MyPassWord。
3.輸入指令mkdir/srv/myproject來建立目錄，再輸入chmod 770修改權限，讓群組裡的人可讀可寫可執行，而其他使用者則沒有權限。
4.輸入su myuser1來切換成myuser1這個用戶，再輸入cd/srv/myproject，進去/srv/myproject這個目錄，輸入vi myuser1.data來建立檔案，
然後按下Esc輸入:wq來離開，再輸入exit就可以登出。
5.輸入cp /usr/bin/LS將此複製到/user/local/bin/myls，再輸入su nouser1，切換成nouser1的用戶，
輸入ll/usr/local/bin/myls來查看該目錄的檔名資訊。

----------------------------------------------------------------------------------------------------------------------------------
1.輸入ps aux | grep rsyslog，來找rsyslog的PID是990，然後輸入ps -1 990找到PRI是80，NI是0，CMD是usr/bin/rsyslog -n，
再接著輸入ps aux | grep rsyslog > /root/process_syslog.txt，再輸入vi process_syslog.txt，
將資訊轉存到/root/process_syslog.txt中。

----------------------------------------------------------------------------------------------------------------------------------
1.輸入find/usr/bin usr/bin/usr/sbin -perm/4000，可以找到目錄中含有SUID的特殊檔名，
有mount change gpass newgrp su sudo pkexe cronyab passwd pam_time_check unix_chkpwd usernetctl，
然後輸入find /usr/bin/usr/sbin -perm/4000 -exec is -1 {} \; > /root/findsuidsgid.txt，找到權限，
輸入vi findsuidsgid.txt，將資料轉存到/ root /findsuidsgid.txt檔案中。
