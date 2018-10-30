# 1.管理群組共用資料的權限設計：

## 建立群組名稱為： mygroup, nogroup

-  用groupadd <群組>新增群組
-  再用grep <群組> /etc/group確認群組是否設立成功

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/1.PNG?raw=true)

## 建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord

-  用useradd -G <群組> <帳號>新增帳號並把帳號加入指定的群組
-  用passwd <帳號>新增密碼

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/2.PNG?raw=true)

## 建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord

-  同上步驟

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/3.PNG?raw=true)

## 建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限

-  先用cd進入srv這個目錄
-  用mkdir <目錄>創建myproject
-  用ll確認是否存在和確認權限
-  用chgrp <群組> <目錄>把myproject的群組改變成mygroup
-  用chmod把群組的使用者權限改成rwx,把其他人改成沒有權限
-  用ll確認權限是否改變成功

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/4.PNG?raw=true)

## 暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。

-  用su <帳號>把使用者切換成myuser1
-  用cd進入myproject,再用touch <檔案>創建myuser1.data
-  用su root把myuser1登出並登入root

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/5.PNG?raw=true)

# 2.使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)

-  用ps aux |grep rsyslog找尋與rsyslog相關的程序
-  第二個顯示的結果通常是搜尋與rsyslog相關的程序這個動作所產生的程序,故只需記住第一個搜尋到的程序PID號碼

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/6.PNG?raw=true)

-  用top -p 所查程序的PID號碼
-  就會跑出rsyslog 相關的程序的資訊

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/7.PNG?raw=true)

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/8.PNG?raw=true)

-  用top -p PID號碼 > /root/process_syslog.txt轉存入檔案中
-  (註:如果要轉存入的檔案不存在,系統會製造一個空檔案;若存在,系統會清空檔案的內容再存入資料)
-  用cat確認檔案內容

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/9.PNG?raw=true)

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/10.PNG?raw=true)

# 3.使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)


-  用find <目錄> -perm /u=s找尋含有SUID的特殊檔案檔名

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/11.PNG?raw=true)

-  第一個用ll <檔案> > /root/findsuidsgid.txt存資料,其他的用ll <檔案> >> /root/findsuidsgid.txt
-  因為用>時會把之前的資料先清除再存,而用>>不會清除資料
-  用cat確認檔案內容

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/12.PNG?raw=true)

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-4/ACS107150/13.PNG?raw=true)


