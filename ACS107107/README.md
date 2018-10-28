#  第一題
##  1.建立群組名稱為： mygroup, nogroup,利用groupadd mygroup來建立
##  ![](https://i.imgur.com/zw1Eni8.jpg)
##  2.建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord(先加入群組)
##  ![](https://i.imgur.com/VIUCEqg.jpg)
##  ![](https://i.imgur.com/YKGbBzY.jpg)
##  3.建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord
##  ![](https://i.imgur.com/D4fEhfr.jpg)
##  4.建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
##  ![](https://i.imgur.com/gXddIvA.jpg)
##  5.暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1
##  ![](https://i.imgur.com/G82Q7AD.jpg)
##  6.複製/usr/bin/ls至/usr/local/bin/myls後，完成下列操作(當你使用 nouser1 的身分執行【myls /srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊。) 
##  ![](https://i.imgur.com/hMtVvZM.jpg)
##  ![](https://i.imgur.com/r27155B.jpg)
#  第二題
##  1.使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)
##  2.按照指令來完成
##  ![](https://i.imgur.com/RnxHFNR.jpg)
##  ![](https://i.imgur.com/ysYAMIy.jpg)
##  3.最後確認一下
##  ![](https://i.imgur.com/SSgSUSE.jpg)
#  第三題
##  1.使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)
##  2.利用find的指令找出檔案檔名(find /-perm/4000)之後就會跑出所有符合的檔名
##  ![](https://i.imgur.com/e0A966X.jpg)
##  3.轉存到目標檔案,之後用cat /root/findsuidgid.txt確認一下就ok了
##  ![](https://i.imgur.com/i8StM4m.jpg)