#1
1.使用groupadd指令依序增加mygroup和nogroup兩個群組。

2.並利用useradd指令創建myuser1 myuser2 myuser3並使用-g mygroup指令讓這三個user加入mygroup這個群組。

3.一樣利用useradd指令創建nouser1 nouser2 nouser3並使用-g nogroup指令讓這三個user加入mygroup這個群組。

4.接著利用passwd指令設定user的密碼為MyPassWord,依序設定完成myuser1 myuser2 myuser3 nouser1 nouser2 nouser3。

5.利用id指令查看使用者是否存在以及群組所屬。

6.利用mkdir指令在srv/下建立名為myproject的目錄,再利用chgrp改變myproject的擁有群組為mygroup,利用ll指令查看資料夾屬性以及是否存在。

7.利用su指令切換到myuser1,再利用cd指令切換到myproject的目錄之下用touch指令建立一個名為myuser1.data的檔案,最後利用ll指令查看資料夾屬性以及是否存在並登出myuser1。

8.利用cp指令復制/usr/bin/ls至/usr/local/bin/myl,用ll指令查看其屬性,並用chmod指令改變其屬性為-rwsr,再用ll指令查看是否改變成功。

9.利用su指令登入nouser1,在用myls指令去查看myproject目錄下的myuser1.data檔案。
#2
1.利用ps aux指令查詢關鍵字rsyslog,找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 並利用>轉存到 /root/process_syslog.txt 檔案中,再利用cat指令列出朗案內容確定以複製成功。

2.利用top列出相關程序資料,找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND。
#3
1.使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名,使用ls -l指令列出檔案相關權限後，將資料轉存至 findsuidsgid.txt檔案中。並使用vi findsuidsgid.txt可以發現資料已經儲存到檔案中。


![](https://ppt.cc/fkYmUx@.png)

![](https://ppt.cc/fnVI5x@.png)

![](https://ppt.cc/fIpqOx@.png)

![](https://ppt.cc/fh3iIx@.png)

![](https://ppt.cc/fS1EKx@.png)

![](https://ppt.cc/fnIIwx@.png)

![](https://ppt.cc/fnnk0x@.png)

![](https://ppt.cc/fQlsDx@.png)