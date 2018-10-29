1.輸入groupadd mygroup和nogroup建立群組，再輸入gpasswd mygroup可以設定密碼，不過我上網查說通常都不會將群組設定密碼。
2.輸入useradd myuser1建立帳號，再輸入passwd myuser1設定密碼為MyPassWord。
3.輸入useradd myuser2建立第二個帳號，再輸入passwd myuser2設定密碼為MyPassWord。
3.輸入useradd myuser3建立第三個帳號，再輸入passwd myuser3設定密碼為MyPassWord
4.我本來是輸入useradd -G mygroup myuser1，但會無法成功，所以改成輸入usermod -g mygroup myuser1改變此帳號的所屬群組，再輸入id myuser1查看，可發現變為mygroup
5.輸入usermod -g mygroup myuser2改變此帳號的所屬群組，再輸入id myuser2查看，可發現變為mygroup
6.輸入usermod -g mygroup myuser3改變此帳號的所屬群組，再輸入id myuser3查看，可發現變為mygroup
7.輸入useradd nouser1建立帳號，再輸入passwd nouser1設定密碼為MyPassWord。
8.輸入useradd nouser2建立帳號，再輸入passwd nouser2設定密碼為MyPassWord。
9.輸入useradd nouser3建立帳號，再輸入passwd nouser3設定密碼為MyPassWord。
10.輸入usermod -g nogroup nouser1改變此帳號的所屬群組，再輸入id nouser1查看，可發現變為nogroup
11.輸入usermod -g nogroup nouser2改變此帳號的所屬群組，再輸入id nouser2查看，可發現變為nogroup
12.輸入usermod -g nogroup nouser3改變此帳號的所屬群組，再輸入id nouser3查看，可發現變為nogroup
13.輸入 mkdir srv建立目錄，再輸入cd srv進入，在srv目錄下輸入mkdir myproject建立目錄。
14.輸入cd ..退回srv，再輸入cd ..退回~，輸入chgrp mygroup srv，以及輸入chmod 770 srv，讓群組的所有人可讀可寫可執行，其他人則都不行，在輸入ls -l，可發現srv的群組和權限已更改
15.輸入cd srv進入目錄，再輸入cdgrp mygroup myproject，和輸入chmod 770 myproject，再輸入ls -l查看可發現群組已變更為mygroup且權限為drwxrwx---
16.輸入cd ~退回去，再輸入su myuser1登入帳號
17.輸入cd /srv/myproject進入目錄，輸入vi myuser1.data建立檔案，他會要你編輯檔案，按下ESC鍵退出，我原本輸入:wq但無法退出改成:q就可以了。
18.輸入cp /from/usr/bin/ls /to/usr/local/bin/myls，可將目錄從/usr/bin/ls複製至/usr/local/bin/myls，加上-R參數可複製全部內容。

1.我原本輸入ps -l觀察程序，但都找不到rsyslog，後來發現要輸入ps aux才能找到，因為ps -l只能觀察到自己的process，要使用ps aux才能看到所有的process。
2.一開始使我用grep 'rsyslog' ps aux，想找rsyslog的結果，但他說找不到叫做aux的檔案，所以不能這樣做，因此我將ps aux的結果輸出成一個txt檔案，用指令ps aux > test.txt，接著使用vi test.txt，觀察test.txt裡的內容的確是ps aux的結果，在按下ESC再輸入:q退出。
3.使用grep 'rsyslog' test.txt，結果成功的查詢了rsyslog的結果。因此我最後使用指令grep 'rsyslog' test.txt > process_syslog.txt 將查詢的結果輸出。

1.輸入find /usr/bin -prem /7000 可查看/usr/bin這個目錄中含有SUID的特殊檔案檔名，其中有一個叫做wall。
2.輸入cd /usr/bin進入目錄，再輸入ls -l wall，可查看權限為-r-xr-sr-x，出現了s，可證明其為SUID的特殊檔案檔名。
3.接著輸入find /usr/bin -prem /7000 > /root/findsuidsgid.txt，將螢幕資料轉存到此檔案。
4.輸入vi findsuidsgid.txt 編輯檔案，可發現已存在SUID的特殊檔案檔名。
5.繼續輸入find /usr/sbin -prem /7000，查看/usr/sbin這個目錄中含有SUID的特殊檔案檔名，其中有一個叫做postdrop。
6.輸入cd /usr/sbin進入，輸入ls -l postdrop查看權限為-rwxr-sr-x，發現有s權限，證明其為SUID的特殊檔案檔名。
7.接著輸入find /usr/sbin -prem /7000 > /root/findsuidsgid.txt，將資料轉存到此檔案。
8.輸入vi findsuidsgid.txt 編輯檔案，可發現又增加了SUID的特殊檔案檔名。


