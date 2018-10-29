#  1.管理群組共用資料的權限設計：</br></br>

####  用"groupadd name"新增群組。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/1.png)</br></br>

##  *建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord </br>
####  用"useradd -g mygroup name "建立一個群組為"mygroup"的帳號。 </br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/2.png)</br></br>

##  *建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord </br>
####  用"useradd -g nogroup name "建立一個群組為"nogroup"的帳號。 </br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/3.png)</br></br>

##  *建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限</br>
####  用"mkdir"建立新目錄，用"chmod"更改權限，用"chgrp"更改群組，再用"ll"檢視。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/4.png)</br></br>

##  *暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。 </br>
####  用"cd"前往目錄，用"touch name"新增檔案，再用"exit"登出帳號。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/5.png)</br></br>

##  *複製/usr/bin/ls至/usr/local/bin/myls後，完成下列操作 </br>
####  用"cp -r A B"將A完全複製到B上(參數r有全部複製的功用)。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/6.png)</br></br>

##    *雖然 nogroup 群組內的用戶對於 /srv/myproject 應該沒有任何權限，但當 nogroup 內的用戶執行 /usr/local/bin/myls 時，可以產生與 ls 相同的資訊，且暫時擁有 mygroup 群組的權限，因此可以查詢到 /srv/myproject 目錄內的檔名資訊。 也就是說，當你使用 nouser1 的身分執行【myls /srv/myproject】時，應該是能夠查閱到該目錄內的檔名資訊。 </br> 
####  用nouser1執行【myls /srv/myproject】時，無法開啟檔案。
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/7.png)</br></br>

####  要用"chmod u+s"給予使用者SUID的權限(只要任何人有x的執行權，當用戶執行時，會自動透過SUID轉換身分為owner，亦變為root的身分)。</br>
####  執行【myls /srv/myproject】。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/8.png)</br></br>

#  2.使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出) </br>
####  用"ps aux |grep rsyslog"觀察程序，並用">"將資料移轉到指定檔案，再用"cat"檢視檔案內容。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/11.png)</br></br>

#  3.使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案) </br>

####  用"find / -perm /u=s"列出系統中所有 SUID 的檔案，並在後面加入"-exec ls -l {} \;"。</br>
####  用">"將資料移轉。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/14.png)</br>

####  用"cat"檢視檔案內容。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/raw/HW-4/ACS107127/screen4/15.png)</br>