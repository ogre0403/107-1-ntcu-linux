# 1</br>
## 建立群組名稱為：mygroup, nogroup</br>
用"groupadd (groupname)"建立新群組</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/1-1.PNG?raw=true)</br>
## 建立帳號名稱為：myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/1-2.PNG?raw=true)</br>
用"useradd -g mygroup (username)"建立一個群組為mygroup的使用者</br>
## 建立帳號名稱為：nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord</br>
用"useradd -g nogroup (username)"建立一個群組為nogroup的使用者</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/1-3.PNG?raw=true)</br>
## 建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。(不過其他人不能有任何權限)</br>
用"mkdir"建立目錄，用"chmod"更改權限，用"chgrp"改變群組，再用"ll"查看</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/1-4.PNG?raw=true)</br>
## 暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1</br>
用"su (username)"切換使用者，"cd (目錄名)"前往該目錄，"touch (檔案名)"建立檔案，最後用"exit"登出帳號</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/1-5.PNG?raw=true)</br>
## 複製/usr/bin/ls至/usr/local/bin/myls後，完成下列操作</br>
用"cp -r A B"將A完全複製到B上(-r有全部複製的功能)</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/1-6.PNG?raw=true)</br>
## 雖然 nogroup 群組內的用戶對於 /srv/myproject 應該沒有任何權限，但當 nogroup 內的用戶執行 /usr/local/bin/myls 時，可以產生與 ls 相同的資訊，且暫時擁有 mygroup 群組的權限，因此可以查詢到 /srv/myproject 目錄內的檔名資訊。 也就是說，當你使用 nouser1 的身分執行【myls /srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊。</br>
用nouser1執行myls /srv/myproject時，無法開啟檔案(權限不足)</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/1-7.1.PNG?raw=true)</br>
需要用"chmod u+s"給予使用者SUID的權限</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/1-7.2.PNG?raw=true)</br>
# 2</br>
## 使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)</br>
用"ps aux |grep rsyslog"觀察系統全部程序，並將有rsyslog關鍵字的程序找出。再用">"將資料移轉到指定檔案，最後搭配"cat"檢視檔案內容</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/2-1.PNG?raw=true)</br>
# 3</br>
## 使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)</br>
用"find / -perm /u=s"列出系統中所有 SUID 的檔案，並在後面加入"-exec ls -l {} \\;"找到檔案相關權限</br>
*附註:* "-exec"可以讓搜尋出來的結果，使用其他的指令進行後續的處理動作</br>
![image](https://github.com/bill0330/107-1-ntcu-linux/blob/HW-4/ACS107137/img/3-1.PNG?raw=true)</br>