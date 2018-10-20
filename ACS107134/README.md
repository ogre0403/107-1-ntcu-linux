1.
◆建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。(請參考書上passwd --stdin的說明)
注意useradd的指令要由root來執行，接者設密碼要用passwd+user名 

![1](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/1.JPG)


◆請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。
注意若要將家目錄、郵件檔案刪除的話要記得用"-r"


![2](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/2.JPG)

◆examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄
所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。
而這個帳號的密碼請給予ItIsExam的樣式。(相關建置帳號的指令，請參考 man useradd 等線上文件的說明)

![3](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/3.JPG)

2.
◆建立examuser4使用者帳號，密碼任意。

◆使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。

![4](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/4.JPG)

◆建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，
users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)

只改日期時間變為00:00 	touch -d 20150101 (filename)
改日期&時間		touch -t 201501150821.32 (filename)

![5](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/5.JPG)

3.
◆請使用 root 的身份建立底下的檔案與權限：
drwxrwxr-x  root root /dev/shm/unit05/
drwxr-xr--  root root /dev/shm/unit05/dir1/
-rw-r--r--  root root /dev/shm/unit05/dir1/file1 (複製來自 /etc/hosts)
drwxr-x--x  root root /dev/shm/unit05/dir2/
-rw-r--r--  root root /dev/shm/unit05/dir2/file2 (複製來自 /etc/hosts)
drwxr-xr-x  root root /dev/shm/unit05/dir3/
-rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (複製來自 /etc/hosts)
drwxrwxrwx  root root /dev/shm/unit05/dir4/
-rw-------  root root /dev/shm/unit05/dir4/file4 (複製來自 /etc/hosts)

![6](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/6.JPG)

![7](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/7.JPG)



複製用cp (欲複製的檔案) (覆寫的檔案)


◆使用一般使用者 的身份進行各項工作：

◆請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？

![8](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/8.JPG)

◆請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行
，依據產生的結果說明為何會如此？

![9](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/9.JPG)

◆請使用 vim(or vi) /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4
，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？
file1(Permission Denied) 不可讀不可編輯
file2 無法用tab鍵按出來(唯讀檔不可更改)
file3 可被編輯
file4 (Permission Denied) 不可讀不可編輯

![10](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/10.JPG)
![11](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/11.JPG)
![12](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/12.JPG)
![13](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/13.JPG)


