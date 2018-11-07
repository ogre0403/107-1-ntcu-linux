# 1.管理群組共用資料的權限設計:
* 建立群組名稱為： mygroup, nogroup
![](https://i.imgur.com/WtiVbbh.png)
* 建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord
* 建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord
![](https://i.imgur.com/krsLKWB.png)
![](https://i.imgur.com/jNcXgYL.png)
因為上面指令打錯導致沒成功加入群組,所以這裡用usermod處理
![](https://i.imgur.com/iMJnfiZ.png)
* 建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
![](https://i.imgur.com/IIJLDLp.png)
* 暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。
![](https://i.imgur.com/vKZiWRS.png)
* 復制/usr/bin/ls至/usr/local/bin/myls
![](https://i.imgur.com/nx6gVMu.png)
![](https://i.imgur.com/V5zIz41.png)
# 2.使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/pr![](https://i.imgur.com/HgjDUTu.png)
圖中可找到 rsyslog的PID,PRI,NI,COMMAND
# 3.使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)
* 使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名
![](https://i.imgur.com/5nVsMjG.png)
* 使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中
![](https://i.imgur.com/w417wYd.png)
