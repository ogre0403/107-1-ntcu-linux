1.啟動之前安裝的虛擬器，登入root帳號，輸入密碼，
以root的身分輸入useradd examuser1來建立examuser1這個用戶，
再輸入passwd examuser1，用ltlsExam作為examuser1的密碼，
其他examuser2及examuser3也都按照上面的步驟來建立。
2.輸入userdel -r examuser3刪除examuser3的帳號和目錄。
3.輸入 id examuser1，查看examuser1的UID和GID，是1001，再輸入adduser -u 1001 examuser1，重新建立examuser1的帳號。
------------------------------------------------------------------------
1.依上面的方式，登入root，然後輸入useradd examuser4來建立examuser4這個帳號，再輸入passwd examuser1，設定密碼。
2.接著輸入cp/etc/securetty/home/examuser4/，把/etc/securetty/複製給examuser4，利用chomd更改權限，
輸入chmod u=rwx, g=rwx, o=rwx更改。
3.先輸入cd回到家目錄，輸入mkdir examdata來建立examdata，
輸入cd examdata/進入該資料夾，輸入touch change.txt建立檔案，
輸入chown sshd change.txt，把擁有者名稱改成sshd，
再輸入chgrp users change.txt，把群組名稱改成users，
要更改權限，所以輸入chmod u=rw, g=r, o= change.txt，讓擁有者可以讀寫，讓群組可以讀，而其他使用者沒有權限，
輸入touch -t 20121221xxxx.txt更改時間。
------------------------------------------------------------------------
1.回到家目錄，輸入mkdir dev來建立dev這個資料夾，輸入cd dev/進入dev資料夾，
輸入mkdir shm，在dev的資料夾裡再設一個叫作shm的子資料夾，輸入cd shm/進入，
輸入mkdir unit05，創立unit05這個資料夾，輸入cd unit05/以進入資料夾，
輸入chmod u=rwx, g=rwx, o=rx更改unit05的資料夾權限，之後接著建立dir1-4的資料夾，
一樣前面的方式輸入chmod去更改權限。
2.輸入ls -1/dev/shm/unit05/dir[1-4]，
dir1的結果是可讀，dir2的結果是可執行，dir3的結果是可讀可執行，dir4的結果是可讀可修改可執行。
3.輸入ls -1/dev/shm/unit05/dir1/file[1-4]，
file1的結果是可讀，file2的結果是可讀，file3的結果是可讀可改寫，file4的結果是沒有權限。
