## 1
+ 1.使用groupadd指令，建立mygroup和nogroup兩個群組
+ 2.用useradd指令創建帳號名稱為myuser1，myuser2，myuser3的3個帳號，再用-g mygroup指令讓這三個user加入mygroup這個群組
+ 3.用passwd [myuser1，myuser2，myuser3]設定密碼為MyPassWord
+ 4.再用上述步驟建立建立帳號名稱為：nouser1，nouser2，nouser3的3個帳號
+ 5.先用useradd創建帳號，再用-g mygroup指令讓這三個user加入nogroup這個群組
+ 6.用passwd [myuser1，myuser2，myuser3]設定密碼為MyPassWord
+ 7.接著可以用id指令確定使用者是否存在以及群組所屬
+ 8.利用mkdir指令在srv/下建立名為myproject的目錄
+ 9.再利用chgrp改變myproject的擁有群組為mygroup，再用ll指令確定資料夾屬性以及是否存在
+ 10.用su nouser1登入nouser1，在用myls /srv/myproject去查看myproject目錄下的myuser1.data檔案
***
## 2
+ 1.用ps aux | grep rsyslog，找到rsyslog 相關的程序的 PID，PRI，NI，COMMAND
+ 2.用ps aux | grep rsyslog > /root/process_syslog.txt將資訊轉存到 /root/process_syslog.txt 檔案中
+ 3.再利用cat指令列出朗案內容確定以複製成功
+ 4.最後用top列出相關程序資料，找到的 rsyslog 相關的程序的 PID，PRI，NI，COMMAND
***
## 3
+ 1.使用find /usr/bin /usr/sbin -perm /4000 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名
+ 2.使用ls -l指令列出檔案相關權限後，將資料轉存至 findsuidsgid.txt檔案中。並使用vi findsuidsgid.txt可以發現資料已經儲存到檔案中