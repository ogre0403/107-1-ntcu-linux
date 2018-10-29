# HW4
==================================
## 1.管理群組共用資料的權限設計:


* (1)建立群組名稱:
  * 利用**groupadd**建立群組:mygroup、nogroup。
> **grep**:了解系統中是否存在想要查詢的群組。

> 系統的群組都記錄在`` /etc/group ``檔案裡，所以查詢的時候要記得加上`` /etc/group ``的絕對路徑喔!


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-1.png)
----------------------------------
* (2)建立帳號名稱:
  * myuser1、myuser2、myuser3(**皆加入mygroup，且密碼皆為MyPassWord**)
> **useradd -G mygroup 帳號名稱**
> > **-G**:後面會接著群組名稱，最後再接著要加入群組的帳號。此外，它也會修改`` etc/group ``內的相關資料。

>利用**passwd 帳號名稱**幫帳號設立密碼。

>利用**id 帳號名稱**查看帳號最後是否有加入**mygroup**的群組中。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-200.png)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-201.png)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-202.png)
----------------------------------
* (3)建立帳號名稱:
  * nouser1、nouser2、nouser3(**皆加入nogroup，且密碼皆為MyPassWord**)
> **useradd -G nogroup 帳號名稱**
> > **-G**:後面會接著群組名稱，最後再接著要加入群組的帳號。此外，它也會修改`` etc/group ``內的相關資料。

> 利用**passwd 帳號名稱**幫帳號設立密碼。

> 利用**id 帳號名稱**查看帳號最後是否有加入**nogroup**的群組中。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-300.png)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-301.png)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-302.png)
----------------------------------
* (4)建立一個目錄`` /srv/myproject ``，此目錄可以讓**mygroup**群組內的使用者完整使用，且`` 新建的檔案擁有群組 ``為**mygroup**，*其他人沒有任何權限*。
  * 切換目錄進入srv，並在其中建立**myproject**資料夾。
> **mkdir 資料夾名稱**:建立資料夾。


  * 先用**ll**查看原始權限，為"drwxr-xr-x"。
  * 利用**chmod**修改權限，記得最後要加上資料夾名稱喔。
  * 再利用**ll**查看會發現權限修改成功囉，為"drwxrwx---"。
  * 利用**chgrp mygroup myproject**修改所屬的群組，再利用**ll**查看就會發現所屬群組已變成mygroup囉。
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-400.png)
----------------------------------
* (5)暫時切換成為**myuser1**的身分，並前往`` /srv/myproject ``目錄，嘗試建立一個名為`` myuser1.data ``的檔案，之後登出**myuser1**。
  * 切換帳號至**myuser1**。
  * 切換至`` /srv/myproject ``目錄。
  * 利用**touch myuser1.data**在其中建立新檔案。
> **touch**:修訂檔案的日期與時間，並且也可以建立一個空的檔案。

  * 最後登出**myuser1**。
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-500.png)
----------------------------------
* (6)複製`` /usr/bin/ls ``至`` /usr/local/bin/myls ``後，完成操作:
  * 利用**cp**將`` /usr/bin/ls ``複製到`` /usr/local/bin/myls ``。
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-600.png)
  * 登入**nogroup**中的其中一員(nouser1)，先利用**ll**查看`` /usr/bin/ls ``和`` /usr/local/bin/myls ``的資訊，會發現得到兩個一樣的資訊。
  * 但一開始還沒辦法查詢到`` myls /srv/myproject ``(Permission denied)。
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-601.png)
  * 切換回**root**修改權限(**chmod u+s 檔案名稱**)。
> **chmod u+s 檔案名稱**:符號法切換檔案執行權限(SUID)。
> > SUID的權限旗標為Linux傳統三個身分的權限外的第四個權限。
> > > 執行者對於該程式需要具有 x 的可執行權限時，可使用此方法讓執行者暫時擁有該程式mygroup群組的權限。

  * 先利用**ll**查看權限資訊，就會發現權限已修改成功囉，為-rw**s**r-xr-x。
  * 最後切換帳號至**nouser1**，查詢`` myls /srv/myproject ``，就可以查詢到裡面的檔案資訊(myuser1.data)了。
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/1-602.png)
=================================
## 2.使用程序觀察的指令，搭配**grep**的關鍵字查詢功能，將找到的**rsyslog**相關的程序的 PID, PRI, NI, COMMAND 等資訊轉存到`` /root/process_syslog.txt ``檔案中。(搭配`` > ``重導向輸出)


* 利用關鍵字查詢功能`` ps aux | grep rsyslog``做程序觀察。
> **ps aux**:檢視全部的process狀況。
> **grep 檔案名稱**:找尋並印出檔案中含有字串所在行內容。

* 使用`` ps aux | grep rsyslog > /root/process_syslog.txt ``將**rsyslog**相關程序的資訊轉存至**/root/process_syslog.txt**。
* 再利用`` cat /root/process syslog.txt ``使檔案的內容列出到螢幕上。
> **cat**:列出檔案內容至螢幕上(標準輸出)或合併多個檔案。

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/2-100.png)
* 輸入**top**找尋**rsyslog**的PID、PRI、NI、COMMAND等資訊。
> **top**:指示目前系統服務項目的動態資料。

  * PID為932。
  * PRI為20。
  * NI為0。
  * COMMAND為rsyslogd。
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/2-101.png)
=================================
## 3.使用**find**找出`` /usr/bin ``及`` /usr/sbin ``兩個目錄中，含有**SUID**的特殊檔案檔名，並使用**ls -l**去列出找到的檔案的相關權限後，將螢幕資料轉存到`` /root/findsuidsgid.txt ``檔案中。(自行查詢**find**指令用法，以及使透過重導向符號`` > ``輸出檔案)


* 使用`` find /usr/bin /usr/sbin -perm /4000 ``找出那兩個目錄中含有SUID的特殊檔案檔名(如圖)。
> `` find 檔案 -perm /u=s ``:列印出系統中所有SUID的檔案。
> > **find**:將想要尋找的檔案找出來。
> > **-perm**:可以指定檔案的權限。

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/3-100.png)
* `` find /usr/bin /usr/sbin -perm /4000 -exec ls -l {} \; > /root/findsuidsgid.txt ``，列出檔案的相關權限。
> **-exec 指令 {} \**:可以讓我們將搜尋出來的結果，使用其他的指令進行後續的處理動作。

![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/3-101.png)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/3-102.PNG)
![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-4/ACs107109/3-103.PNG)
