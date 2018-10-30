# ADT105137_HW4
1.管理群組共用資料的權限設計：

建立群組名稱為： mygroup, nogroup
a.利用groupadd建立

建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord
建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord
b.將使用者加入某群組使用:usermod -a -G grp_name user_name
![image](https://github.com/Yubo0826/1030/blob/master/1-1.PNG)

建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
c.mkdir -p  /srv/myproject ， chgrp更改mygroup，chmod 2770 ，讓目錄加入SGID然後others並沒有任何權限。
*-p:幫助你直接將上面的目錄遞迴建立起來*
![image](https://github.com/Yubo0826/1030/blob/master/1-2.PNG)
![image](https://github.com/Yubo0826/1030/blob/master/1-3.PNG)

暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。
d.su 指令切換使用者，然後前往目錄用touch指令建立 myuser1.data
![image](https://github.com/Yubo0826/1030/blob/master/1-4.PNG)

復制/usr/bin/ls至/usr/local/bin/myls後，完成下列操作:
雖然 nogroup 群組內的用戶對於 /srv/myproject 應該沒有任何權限，但當 nogroup 內的用戶執行 /usr/local/bin/myls 時，可以產生與 ls 相同的資訊，且暫時擁有 mygroup 群組的權限，因此可以查詢到 /srv/myproject 目錄內的檔名資訊。 也就是說，當你使用 nouser1 的身分執行【myls /srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊。
e.用cp指令複製檔案，之後給myls SUID
![image](https://github.com/Yubo0826/1030/blob/master/1-5.PNG)
![image](https://github.com/Yubo0826/1030/blob/master/1-6.PNG)

2.用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)
a.用ps aux查詢 +|grep 查詢，用> 輸出到/root/process_syslog.txt
![image](https://github.com/Yubo0826/1030/blob/master/2-1.PNG)
![image](https://github.com/Yubo0826/1030/blob/master/2-2.PNG)

3.使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)
![image](https://github.com/Yubo0826/1030/blob/master/3-1.PNG)
![image](https://github.com/Yubo0826/1030/blob/master/3-2.PNG)



