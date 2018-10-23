###Q1-1:建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。(請參考書上passwd --stdin的說明)    
先把使用者切換為root權限，然後用useradd建立帳號、用passwd設定密碼    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/1.PNG)    
--------------------------------------    
###Q1-2:請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。    
利用userdel -r (username)同時刪除帳號的家目錄與郵件檔案    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/2.PNG)    
--------------------------------------    
###Q1-3:examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。而這個帳號的密碼請給予 ItIsExam 的樣式。(相關建置帳號的指令，請參考 man useradd 等線上文件的說明)    
用useradd -u (原帳號的uid) (username) 重建examuser1的帳號    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/3.PNG)    
--------------------------------------    
###Q2-1:建立examuser4使用者帳號，密碼任意。    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/4.PNG)    
--------------------------------------    
###Q2-2:使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。    
用cp指令複製檔案，再用chmod指令修改權限    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/4.5.PNG)    
--------------------------------------    
###Q2-3:建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)    
先用mkdir建立資料夾，再用touch建立檔案，然後修改權限。最後用touch -d (time) (username) 修改時間    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/5.PNG)    
--------------------------------------    
###Q3-1:請使用 root 的身份建立底下的檔案與權限：    
###drwxrwxr-x  root root /dev/shm/unit05/    
###drwxr-xr--  root root /dev/shm/unit05/dir1/    
###-rw-r--r--  root root /dev/shm/unit05/dir1/file1 (複製來自 /etc/hosts)    
###drwxr-x--x  root root /dev/shm/unit05/dir2/    
###-rw-r--r--  root root /dev/shm/unit05/dir2/file2 (複製來自 /etc/hosts)    
###drwxr-xr-x  root root /dev/shm/unit05/dir3/    
###-rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (複製來自 /etc/hosts)    
###drwxrwxrwx  root root /dev/shm/unit05/dir4/     
###-rw-------  root root /dev/shm/unit05/dir4/file4 (複製來自 /etc/hosts)    
mkdir建立目錄、touch建立檔案、cp複製、chmod更改權限    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/6.PNG)    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/7.PNG)    
--------------------------------------    
###Q3-2:請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？    
1.dir1的其他人權限為r--。雖擁有r(閱讀)權限卻未擁有x(執行)權限，所以導致file1出現許多??的狀況。    
2.dir2的其他人權限為--x。因為缺乏了r(閱讀)權限，所以無法查看其內容。    
3.dir3的其他人權限為r-x。同時擁有r、x權限，輸出正常。    
4.dir4的其他人權限為rwx。同時擁有r、x權限，輸出正常。    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/8.PNG)    
--------------------------------------    
###Q3-3:請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？    
1.因為dir1的其他人權限為r--，缺乏x權限導致其下的file1無法執行。    
2.dir[2-4]的其他人權限皆擁有x權限，所以其下file[2-4]的指令皆為正常    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/9.PNG)    
--------------------------------------    
###Q3-4:請使用 vim(or vi) /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？    
file1->因其上的dir1的其他人權限缺乏x(執行)權限，所以無法開啟    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/10.PNG)    
file2(其他人權限為r--)->唯讀檔，可以查看但不能修改存檔    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/11.5.PNG)    
file3(其他人權限rw-)->擁有r(閱讀)、w(修改)權限，可以查看也能修改存檔    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/12.PNG)    
file4(其他人權限rwx)->擁有r(閱讀)、w(修改)權限，可以查看也能修改存檔    
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-3/ACS107135/photo/13.PNG)    