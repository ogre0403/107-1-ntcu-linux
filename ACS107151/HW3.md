## 1

+ 先用root登入，建立examuser1,examuser2,examuser3
+ 輸入useradd examuser1來建立examuser1這個用戶
+ 輸入passwd examuser1，examuser1的密碼為ltlsExam
+ examuser2及examuser3也用同樣步驟建立
+ 2.輸入userdel -r examuser3刪除examuser3的帳號和目錄
+ 3.輸入 id examuser1，查看examuser1的UID和GID，是1001，再輸入adduser -u 1001 examuser1，重新建立examuser1的帳號
+ # 完成
***
+ 1.先登入root，輸入useradd examuser4來建立examuser4這個用戶
+ 2.輸入passwd examuser4，設定密碼  
+ 3.接著輸入cp/etc/securetty/home/examuser4/，把/etc/securetty/複製給examuser4 
+ 4.再用chown examuser4 securetty再用chmod u=rwx, g=rwx, o=rwx examuser4使此帳號擁有完整使用檔 
+ 5.用mkdir examdata，接著cd進去examdata裡面 
+ 6.輸入touch change.txt建立空檔案，用chown sshd change.txt將擁有者改為sshd 
+ 7.再輸入chgrp users change.txt將群組改為users，用chmod u=rw,g=r,o= change.txt將sshd可讀可寫 
+ 8.最後用touch -t 20121221 change.txt將檔案的修改日期調整成 2012 年 12 月 21 日 
+ # 完成 
***
+ 1.回到家目錄，輸入mkdir dev來建立dev這個資料夾，輸入cd dev/進入dev資料夾
+ 2.輸入mkdir shm，在dev的資料夾裡再設一個叫作shm的子資料夾，輸入cd shm，進入shm
+ 3.輸入mkdir unit05，創立unit05這個資料夾，輸入cd unit05，進入unit05
+ 4.輸入chmod u=rwx, g=rwx, o=rx更改unit05的資料夾權限，之後接著建立dir1-4的資料夾
+ 5.輸入ls -1/dev/shm/unit05/dir[1-4]，可以發現dir1的結果是可讀，dir2的結果是可執行，dir3的結果是可讀可執行，dir4的結果是可讀可修改可執行
+ 6.再輸入ls -1/dev/shm/unit05/dir1/file[1-4]，可以發現file1的結果是可讀，file2的結果是可讀，file3的結果是可讀可改寫，file4的結果是沒有權限
+ # 完成
