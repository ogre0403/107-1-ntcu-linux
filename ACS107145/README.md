# 1</br>
##一.建立群組名稱為：mygroup, nogroup
##二.建立帳號名稱為：myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 mypassword</br>
##三.建立帳號名稱為：myuser1, myuser2, myuser3 ，通通加入 nogroup，且密碼為 mypassword</br>
##四.建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup.並暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1.</br>
##五.複製/usr/bin/ls至/usr/local/bin/myls後，用"cp -r A B"將A完全複製到B上</br>
##六.雖然 nogroup 群組內的用戶對於 /srv/myproject 應該沒有任何權限，但當 nogroup 內的用戶執行 /usr/local/bin/myls 時，可以產生與 ls 相同的資訊，且暫時擁有 mygroup 群組的權限，因此可以查詢到 /srv/myproject 目錄內的檔名資訊. 也就是說，當你使用 nouser1 的身分執行【myls /srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊.</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-1.PNG)</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-2.PNG)</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-3.PNG)</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-4.PNG)</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-5.PNG)</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-6.PNG)</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-7.PNG)</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-8.PNG)</br>
# 2</br>
## 使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)</br>
用"ps aux |grep rsyslog"觀察系統全部程序，並將有rsyslog關鍵字的程序找出。</br>
再用">"將資料移轉到指定檔案，最後搭配"cat (檔案名)"檢視檔案內容</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-9.PNG)</br>
# 3</br>
##使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-10.PNG)</br>
![image](https://github.com/percy890713/107-1-ntcu-linux/blob/HW-4/ACS107145/HW4-11.PNG)</br>

