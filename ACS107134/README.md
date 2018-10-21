1.
### Q:建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。(請參考書上passwd --stdin的說明) 
  注意useradd的指令要由root來執行哦，如果一開始沒有用-p的話。事後設密碼要用passwd+username。
![1](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/1.JPG)

---------------------------------------分隔線-----------------------------------------

### Q:請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。 
  若要將家目錄、郵件檔案刪除的話要記得要加 "-r" 不然會很麻煩。
![2](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/2.JPG)

---------------------------------------分隔線-----------------------------------------

### Q:examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄，所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。而這個帳號的密碼請給予ItIsExam的樣式。(相關建置帳號的指令，請參考 man useradd 等線上文件的說明) 
  使用"useradd -u (uid) 帳號名" 可以將新帳號與舊有的uid做連結。
![3](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/3.JPG)

---------------------------------------分隔線-----------------------------------------

2.
### Q:建立examuser4使用者帳號，密碼任意。 
### Q:使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。 
  這裡，我將/etc/securetty檔案權限增加給examuser4，以下是我的方式，有點迂迴。
![4](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/4.JPG)

---------------------------------------分隔線-----------------------------------------

### Q:建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便) 
  使用touch新增一個文件，並更改擁有者為sshd，群組改成users。 用chmod來更改檔案權限。
  更改修改日期的方式有:
	1.只改日期時間變為00:00 	touch -d 20150101 (filename)
	2.改日期&時間		touch -t 201501150821.32 (filename)

![5](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/5.JPG)

---------------------------------------分隔線-----------------------------------------

3.
### Q:請使用 root 的身份建立底下的檔案與權限： 
#### drwxrwxr-x  root root /dev/shm/unit05/ 
#### drwxr-xr--  root root /dev/shm/unit05/dir1/ 
#### -rw-r--r--  root root /dev/shm/unit05/dir1/file1 (複製來自 /etc/hosts) 
#### drwxr-x--x  root root /dev/shm/unit05/dir2/ 
#### -rw-r--r--  root root /dev/shm/unit05/dir2/file2 (複製來自 /etc/hosts) 
#### drwxr-xr-x  root root /dev/shm/unit05/dir3/
#### -rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (複製來自 /etc/hosts) 
#### drwxrwxrwx  root root /dev/shm/unit05/dir4/ 
#### -rw-------  root root /dev/shm/unit05/dir4/file4 (複製來自 /etc/hosts) 
  建立檔案用touch、建立目錄用mkdir。	複製用"cp (欲複製的檔案) (覆寫的檔案)" 
  更改權限用chmod哦，chmod的用法是 chmod (ugoa)(+-=)(rwx-)(,) filename or chmod ??? filename(?是獨立的數字)
![6](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/6.JPG)
![7](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/7.JPG)

---------------------------------------分隔線-----------------------------------------

### Q:使用一般使用者 的身份進行各項工作： 
  我切換到自己的帳號用"su username" 
### Q:請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？ 
  依照要求執行指令 
![8](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/8.JPG)

---------------------------------------分隔線-----------------------------------------

### Q:請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？ 
  依照一開始< 權限 >設定的不同造就的結果也就不一樣。 
![9](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/9.JPG)

---------------------------------------分隔線-----------------------------------------

### Q:請使用 vim(or vi) /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？ 
  file1顯示 -> (Permission Denied) 不可讀不可編輯 
  file2顯示 -> 無法用tab鍵按出來(唯讀檔不可更改) 
  file3顯示 -> 可被編輯 
  file4顯示 -> (Permission Denied) 不可讀不可編輯 
![10](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/10.JPG)
![11](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/11.JPG)
![12](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/12.JPG)
![13](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/13.JPG)

