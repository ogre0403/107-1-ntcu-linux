# 1-1：建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。    
登入使用者帳號後，用"su -"指令切換為管理者root    
用"useradd (username)"建立新帳號、"passwd (username)"設定密碼    

# 1-2：請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。    
用"userdel -r (username)"刪除使用者的家目錄及資料    
注意!!! 沒有加上-r家目錄不會刪除    

# 1-3：examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。    
用"useradd -u (原帳號的UID) (username)"重建帳號    

# 2-1：建立examuser4使用者帳號，密碼任意。    
登入使用者帳號後，用"su -"指令切換為管理者root    
用"useradd (username)"建立新帳號、"passwd (username)"設定密碼    

# 2-2：使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。    
先用"cp"複製檔案，然後用"chgrp"修改群組，最後用"chmod"修改權限    
[數字法：r=4,w=2,x=1 把要給的權限數字相加]   

# 2-3：建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)。    
先用"mkdir"建立資料夾，再用"touch"建立檔案    
隨後用"chown"更改擁有者，"chgrp"更改群組，"chmod"修改權限    
最後再用"touch -d (time) (檔案名稱)"修改時間，這樣就可以了    

# 3-1：請使用 root 的身份建立底下的檔案與權限：    
drwxrwxr-x  root root /dev/shm/unit05/    
drwxr-xr--  root root /dev/shm/unit05/dir1/    
-rw-r--r--  root root /dev/shm/unit05/dir1/file1 (複製來自 /etc/hosts)    
drwxr-x--x  root root /dev/shm/unit05/dir2/    
-rw-r--r--  root root /dev/shm/unit05/dir2/file2 (複製來自 /etc/hosts)    
drwxr-xr-x  root root /dev/shm/unit05/dir3/    
-rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (複製來自 /etc/hosts)    
drwxrwxrwx  root root /dev/shm/unit05/dir4/    
-rw-------  root root /dev/shm/unit05/dir4/file4 (複製來自 /etc/hosts)    

用"mkdir"建立資料夾，"touch"建立檔案，"cp"複製，"chmod"修改權限    

#使用一般使用者 的身份進行各項工作：    
用"su (username)"換回使用者    

# 3-2：請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？    
dir1的其他人使用權限為 r--，雖然可以閱讀，但缺乏x權限，故不能執行    
dir2的其他人使用權限為 --x，雖然可以執行，但缺乏r權限，故不能查看    
dir3的其他人使用權限為 r-x，同時擁有閱讀及執行權限，可以正常執行    
dir4的其他人使用權限為 rwx，同時擁有閱讀及執行權限，可以正常執行    

# 3-3：請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？    
file1的權限缺乏x，因此無法執行    
file2-4有x權限，因此可以正常執行    

# 3-4：請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？   
dir1  r--    
file1 r-- 因dir1缺乏x權限，故無法執行    

dir2  --x    
file2 r-- 雖然dir2有執行權限，但file2只有讀取的權限，因此不能開啟和修改    

dir3  r-x    
file3 rw- 因dir3有閱讀、執行權限，而file3有r及w權限，故能正常讀取和修改        

dir4  rwx    
file4 --- 雖然dir4有全權限，但file4沒有任何權限，因此不能做任何事