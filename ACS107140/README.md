# HW3
## 第一題
1. 使用指令"useradd"，建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，使用指令"passwd (username)"設定三個用戶的密碼都是『 ItIsExam 』。
![](https://i.imgur.com/W5zltn8.png)
2. 使用指令"userdel -r (username) 請刪除系統中的 examuser3 這個帳號，-r 會將這個帳號的家目錄(/home)與郵件檔案(/var/mail)同步刪除。
![](https://i.imgur.com/ggv5te8.png)
![](https://i.imgur.com/tx1dX4o.png)
![](https://i.imgur.com/tC5oyPD.png)
3. examuser1 不小心被管理員刪除了，但是這個帳號的家目錄(/home)與相關郵件(/var/mail)都還存在。請嘗試以該帳號原有的 UID/GID (useradd -u 1001 -U examuser1)資訊來重建該帳號。而這個帳號的密碼(passwd username)ItIsExam
![](https://i.imgur.com/mhiPiMX.png)
![](https://i.imgur.com/3E8sryl.png)
## 第二題
1. 建立examuser4使用者帳號，密碼任意。
![](https://i.imgur.com/pBltE3P.png)
2. 使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。
![](https://i.imgur.com/u63lza8.png)
![](https://i.imgur.com/fTpDyjL.png)
3. 建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)
![](https://i.imgur.com/PakSawl.png)
![](https://i.imgur.com/W8Xnq9f.png)
## 第三題
