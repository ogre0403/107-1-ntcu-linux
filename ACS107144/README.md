# 1.管理群組共用資料的權限設計：
 * 使用root登入
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-1.jpeg)

> ## 建立群組名稱為： mygroup, nogroup
> * 輸入`groupadd mygroup`
>    > 建立名為 mygroup 的新群組
> * 輸入`grep mygroup /etc/group` 
>    > 確定有 mygroup 在設定檔中
> * 輸入`groupadd nogroup`
>    > 建立名為 mygroup 的新群組
> * 輸入`grep nogroup /etc/group` 
>    > 確定有 nogroup 在設定檔中

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-2.jpeg)

> ## 建立帳號名稱為： myuser1, myuser2, myuser3 ，通通加入 mygroup，且密碼為 MyPassWord
>
> 1.  輸入 `useradd -G mygroup myuser1`
>    > 建立名為 myuser1 帳號，要記得加-G指定加入 mygroup
> 2.  輸入 `passwd myuser1`
>    > 設定 myuser1 密碼
> 3.  給予myuser1密碼：MyPassWord
>    > 密碼欄的密碼不顯示
> 4.  使用 `id myuser1` 來確認是否成功建置，且成功加入 mygroup
>    > 若成功加入，最後面會出現 mygroup 字樣（黃線部分）
>  
>      myuser2、myuser3 的建置步驟和 myuser1 相同，只需將帳號名稱修改即可。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-3.png)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-4.jpeg)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-5.png)


> ## 建立帳號名稱為： nouser1, nouser2, nouser3 ，通通加入 nogroup，且密碼為 MyPassWord
>
> 1.  輸入 `useradd -G nogroup nouser1`
>    > 建立名為 nouser1 帳號，要記得加-G指定加入 nogroup
> 2.  輸入 `passwd nouser1`
>    > 設定 nouser1 密碼
> 3.  給予myuser1密碼：MyPassWord
>    > 密碼欄的密碼不顯示
> 4.  使用 `id nouser1` 來確認是否成功建置，且成功加入 nogroup
>    > 若成功加入，最後面會出現 nogroup 字樣（黃線部分）
>  
>      nouser2、nouser3 的建置步驟和 nouser1 相同，只需將帳號名稱修改即可。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-6.png)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-7.png)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-8.png)

> ## 建立一個名為 /srv/myproject 的目錄，這個目錄可以讓 mygroup 群組內的使用者完整使用，且【新建的檔案擁有群組】為 mygroup 。不過其他人不能有任何權限
>
> 1.  輸入 `cd /`
>    > 進入 / 主分支
> 2.  輸入 `cd srv/`
>    > 進入 srv 分支
> 3.  輸入 `mkdir myproject`
>    > 建立 myproject 目錄
> 4.  輸入 `ll`
>    > 查看 myproject 的權限和擁有者 
> 5.  輸入 `chmod u=rwx,g-rwx,o= myproject`
>    > 更改 myproject 權限
> 6.  輸入 `ll`
>    > 查看 myproject 的權限和擁有者 
> 7.  輸入 `chgrp mygroup myproject`
>    > 更改 myproject 的擁有群組為 mygroup
> 8.  輸入 `ll`
>    > 查看 myproject 的權限和擁有者 
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-9.png)

> ## 暫時切換成為 myuser1 的身分，並前往 /srv/myproject 目錄，嘗試建立一個名為 myuser1.data 的檔案，之後登出 myuser1。
>
> 1.  輸入 `su - myuser1`
>    > 切換使用者至myuser1
> 2.  輸入 `cd /`
>    > 進入 / 主分支
> 3.  輸入 `cd srv/`
>    > 進入 srv 分支
> 4.  輸入 `cd myproject`  
>    > 進入 myproject 目錄
> 5.  輸入 `touch myuser1.data 
>    > 建立名為 myuser1.data 的檔案
> 6.  輸入 `ls`
>    > 查看 myuser1.data 是否成功加入，若成功會出現黃色底線之字樣。
> 7.  輸入 `su - root`
>    > 登出 myuser1，回到root
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-10.png)

> ## 復制/usr/bin/ls至/usr/local/bin/myls後，完成下列操作
>
> 1.  輸入 `cp /usr/bin/ls /usr/local/bin/myls`
>    > 複製 /usr/bin/ls 至 /usr/local/bin/myls
> 2.  輸入 `ll /usr/local/bin/myls`  
>    > 查看 /usr/local/bin/myls 的權限
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-11.png) 
> * 切換成 nouser1 
> 1.  輸入 `ll /usr/local/bin/myls`  
>    > 查看權限
> 2.  輸入 `myls /srv/myproject`
>    > 執行後出現Permission denied   
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-12.png) 

> 1.  切換成 root
> 2.  輸入 `chgrp mygroup /usr/local/bin/myls`
>    > 修改 /usr/local/bin/myls 的擁有群組  
> 3.  輸入 `ll /usr/local/bin/myls`  
>    > 查看權限，發現擁有群組從 root 變成 mygroup
> 4.  切換回 nouser1
> 5.  輸入 `myls /srv/myproject`
>    > 執行後出現Permission denied，因為 nouser1 不是 mygroup 的一員   
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-13.png)

> * 切換成 root
> 1.  輸入 `chmod g+s /usr/local/bin/myls`
>    > 修改 g 的權限  
> 2.  輸入 `ll /usr/local/bin/myls`  
>    > 查看權限，發現 x 的地方變成 s，檔案變成橘色
> * 切換回 nouser1
> 3.  輸入 `myls /srv/myproject`
>    > 執行後出現 myuser.data，可成功執行
>
>    > s : 即為SUID的權限旗標，只要任何有 x 執行權的人，執行 myls /srv/myproject 時，就會透過SUID轉換身份為 owner   
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-1-14.png) 



# 2. 使用程序觀察的指令，搭配 grep 的關鍵字查詢功能，將找到的 rsyslog 相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到 /root/process_syslog.txt 檔案中。(搭配>重導向輸出)

> 1.  輸入 `ps aux | grep rsyslog ` 
>    > 找到的 rsyslog 相關的程序
> 2.  輸入 `ps aux | grep rsyslog > /root/process_syslog.txt `
>    
> 將 rsyslog 的相關資訊轉存到 /root/process_syslog.txt 檔案中
> 3.  輸入 `cat /root/process_syslog.txt`
>    > 確認存檔完成
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-2-1.png) 
> 輸入`top`
>    > 查看PID, PR, NI, COMMAND
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-2-2.png) 

> PID：930

> PR：20

> NI：0

> COMMAND：rsyslogd



# 3. 使用 find 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔案檔名，並使用 ls -l 去列出找到的檔案的相關權限後，將螢幕資料轉存到 /root/findsuidsgid.txt 檔案中。(自行查詢find指令用法，以及使透過重導向符號>輸出檔案)

> 1.  輸入 `find /usr/bin /usr/sbin -perm /4000`   
>    > 找出 /usr/bin 及 /usr/sbin 兩個目錄中，含有 SUID 的特殊檔名

>    > chfn
>
>    > chsh
>
>    > mount
>
>    > chage
>
>    > gpasswd
>
>    > newgrp
>
>    > su
>
>    > umount
>
>    > sudo
>
>    > pkexec
>
>    > crontab
>
>    > passwd
>
>    > pam_timestamp_check
>
>    > unix_chkpwd
>
>    > usernetct1

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-3-1.png) 

> 2.  輸入 `find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \; > /root/findsuidsgid.txt`  
>    > 將螢幕資料轉存到/root/findsuidsgid.txt中   

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-3-2.png) 

> 3.  輸入 `vi findsuidsgid.txt`
>    > 確認資料成功存入

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-4/ACS107144/4-3-3.png) 
