# HW4
#### 第一題
+ 1.建立群組： mygroup, nogroup
![GITHUB](https://imgur.com/h1FKkwT.jpg"git圖示")
+ 2.建立帳號名稱為： myuser1, myuser2, myuser3, nouser1, nouser2, nouser3 
![GITHUB](https://imgur.com/WvKD2fO.jpg"git圖示")
+ 3.建立帳號的密碼，皆為MyPassWord
![GITHUB](https://imgur.com/rzz5iAR.jpg"git圖示")
+ 4.將myuser1, myuser2, myuser3分別加入mygroup，再將nouser1, nouser2, nouser3 加到nogroup
![GITHUB](https://imgur.com/JKO33Wm.jpg"git圖示")
+ 5.建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
![GITHUB](https://imgur.com/HhAO7i5.jpg"git圖示")
+ 6.切換成myuser1，建立myuser1.data的檔案
+ 7.復制/usr/bin/ls至/usr/local/bin/myls後，完成下列操作
![GITHUB](https://imgur.com/FQim1ji.jpg"git圖示")
+ 輸入cp /usr/bin/ls /usr/ocal/bin/myls
+ 再輸入ll /usr/local/bin/myls，檢視是否成功
####第二題
+ 使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)
+ 輸入ps aux | grep rsyslog檢視
![GITHUB](https://imgur.com/epFemVv.jpg"git圖示")
+ 輸入ps -l，檢視PID、PRI、NI、CMD
+ 利用top、ps aux找出PR跟NI的資料
![GITHUB](https://imgur.com/dSMSVK3.jpg"git圖示")
+ 輸入ps aux | grep rsyslog > /root/process_syslog.txt
#### 第三題
+ 使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)
![GITHUB](https://imgur.com/dSMSVK3.jpg"git圖示")
+ 輸入find /usr/bin /usr/sbin -perm /4000，列出檔名
![GITHUB](https://imgur.com/tSHEcDC.jpg"git圖示")
+ find /usr/bin /usr/bin | ls -1 ，列出權限
![GITHUB](https://imgur.com/S6AWRhZ.jpg"git圖示")
+ find /usr/bin /usr/sbin | ls -1 ，列出權限
![GITHUB](https://imgur.com/AnbqSXb.jpg"git圖示")
+ find /usr/bin /usr/bin | ls -1 > /root/findsuidsgid.txt，將檔案存到findsuidsgid.txt