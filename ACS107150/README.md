# 1.

## 建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。

> 用useradd 帳號名稱 新增用戶

> 用passwd 帳號名稱 新增用戶密碼

> 出現new password就輸入密碼

> 出現retype new password再輸入一次密碼

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/1.PNG?raw=true)

> 用ll /home確認是否新增成功

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/2.PNG?raw=true)

## 請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。

> 用userdel -r examuser3刪除帳號(加-r能把家目錄和郵件檔案同步刪除)

> 用ll /home確認是否刪除

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/3.PNG?raw=true)

## examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。而這個帳號的密碼請給予 ItIsExam 的樣式。

> 用userdel examuser1刪除帳號

> 用ll /home確認是否刪除

> 發現原本examuser1變成1001,可知1001是examuser1的id

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/4.PNG?raw=true)

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/5.PNG?raw=true)

> 用useradd -u 1001 -U examuser1新增帳戶

> 用ll /home確認是否復原

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/6.PNG?raw=true)

# 2.

## 建立examuser4使用者帳號，密碼任意。

> 用useradd examuser4和passwd examuser4新增帳戶

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/7.PNG?raw=true)

## 使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。
 
> 用cd /etc/securetty /home/examuser4把檔案複製過去

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/8.PNG?raw=true)

> 用ll /etc/securetty和ll /home/examuser4確認是否複製成功

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/9.PNG?raw=true)

> 因為examuser4不是root也不在root的群組裡,所以examuser4屬於other

> 用chmod o=rwx /home/examuser4/securetty開放other的權限

> 用ll /home/examuser4/securetty確認是否成功改變權限

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/10.PNG?raw=true)

## 建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)

> 用cd /進入根目錄

> 用mkdir examdata創建目錄

> 再cd examdata進入examdata這個目錄

> touch change.txt創建檔案

> 用ll確認是否成功

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/11.PNG?raw=true)

> 用chown sshd change.txt把這個檔案的擁有者改為sshd

> 用chgrp users change.txt把這個檔案的群組改為users

> 用ll測試是否改成功

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/12.PNG?raw=true)

> 用chmod u=rw,g=r,o-r change.txt把這個檔案的權限改成rw-r-----

> 用ll確認

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/13.PNG?raw=true)

> 用touch -t 時間(ex.201212211715) change.txt改變最新更改日期

> 用ll確認

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/14.PNG?raw=true)

# 3.

## 請使用 root 的身份建立底下的檔案與權限：

drwxrwxr-x  root root /dev/shm/unit05/
drwxr-xr--  root root /dev/shm/unit05/dir1/
-rw-r--r--  root root /dev/shm/unit05/dir1/file1 (複製來自 /etc/hosts)
drwxr-x--x  root root /dev/shm/unit05/dir2/
-rw-r--r--  root root /dev/shm/unit05/dir2/file2 (複製來自 /etc/hosts)
drwxr-xr-x  root root /dev/shm/unit05/dir3/
-rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (複製來自 /etc/hosts)
drwxrwxrwx  root root /dev/shm/unit05/dir4/
-rw-------  root root /dev/shm/unit05/dir4/file4 (複製來自 /etc/hosts)

> 用cd /進入根目錄

> 用cd shm進入shm

> 用mkdir unit05創建目錄

> 用cd unit05進入unit05

> 用mkdir dir[1-4]創建目錄dir[1-4]

> 用chmod 數字 dir[1-4]改變dir[1-4]的權限

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/15.PNG?raw=true)

> 用touch /dev/shm/unit05/dir1/file1創新檔案

> file[2-4]也是相同作法

> 用cp /etc/hosts /dev/shm/unit05/dir1/file1複製檔案到file1

> file[2-4]也是相同作法

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/16.PNG?raw=true)

> 用cd dir1進入dir1

> 用chmod 數字 file1改變權限

> 用cd -退回上一個目錄

> file[2-4]也是相同作法

> 用ll 檔案位址 確認權限是否改變成功

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/17.PNG?raw=true)

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/18.PNG?raw=true)

## 使用一般使用者 的身份進行各項工作：

> 用su examuser4把登入帳戶改成examuser4

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/19.PNG?raw=true)

## 請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？

> 對dir[1-4]來說examuser4是other

> dir1只能讀不能執行,所以能顯示出來但會出現一堆問號

> dir2不能讀,所以不能顯示

> dir3和dir4能讀也能執行,所以可以完整呈現資訊

> 執行結果如下圖

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/20.PNG?raw=true)

## 請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？

> 對dir[1-4]來說examuser4是other

> 看file[1-4]的資訊需要有dir[1-4]執行(x)的權限

> 只有dir1沒給other執行的權限,所以沒辦法顯示;dir[2-4]則有給執行權限,所以能看到

> 執行結果如下圖

![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-3/ACS107150/21.PNG?raw=true)

## 請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？

> 存檔需要dir的執行(x)權限,還有file的修改(w)權限

> 而dir1沒有給other執行權限,所以沒辦法執行

> dir[2-4]則有給執行權限,所以能執行

> 對file[2-4],examuser4是other,file2只給r的權限,故只讀,不能儲存(修改)

> file3給other的權限是rw-,所以能讀也能儲存(修改)

> file4給other的權限是---,所以能不能讀也不能儲存(修改)
