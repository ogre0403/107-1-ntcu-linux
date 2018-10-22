## 1.

# 先使用root登入
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-01.jpeg)
# 建立 examuser1、examuser2、examuser3
* useradd 檔名
* passwd 檔名
* 輸入密碼：ItIsExam
* 再次確認密碼： ItIsExam
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-02.jpeg)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-03.jpeg)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-04.jpeg)

# 刪除系統中的 examuser3 帳號，同時將這個帳號的家目錄與郵件檔案同步刪除
* userdel -r examuser3
 > 一定要加 -r 才能將加目錄與郵件檔案同步刪除
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-05.jpeg)
* 用 id examuser3 檢查帳號是否刪除
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-06.jpeg)

# examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。參考UID/GID重建帳號。
* 先刪除 examuser1，刪除指令：userdel examuser1 
  > (不需要加-r，因為我們要保留他在家目錄與相關郵件的資料)
* 進入家目錄，指令：cd /home
* 查看家目錄內帳號的資料，指令：ll 
* 進入郵件資料，指令：cd /var/spool/mail
* 查看郵件中帳號資料，指令：ll
 > 發現兩者皆有1001的資料，可知這是帳號名稱遭刪除之 examuser1 在目錄與相關郵件中未遭移除的資料
* 利用1001重建資料，指令：user add -u 1001 -U examuser1
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-07.jpeg)
* 重新設定 examuser1 的密碼，指令：passwd examuser1
 2. 輸入密碼：ItIsExam
 1. 再次確認密碼： ItIsExam
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-08.png)
* 再次回到家目錄，指令：cd /home
* 查看家目錄內帳號的資料，指令：ll 
 > 發現examuser1已成功重建
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-09.jpeg)
* 關機後，重新開機，使用 examuser1 登入，確認修改成功。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-1-10.jpeg)

## 2.

# 建立 examuser4
* useradd 檔名
* passwd 檔名
* 輸入密碼：自訂
* 再次確認密碼： 自訂
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-2-01.png)
# 使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有. 的權限)。
* 複製 /etc/securetty 至 /home/examuser4，指令：cp /etc/securetty /home/examuser4
* 進到 examuser4 裡，指令：cd examuser4
* 檢查是否成功複製檔案給 examuser4，指令：ls
 > 成功的話會出現標註黃色底線的那排字
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-2-02.jpeg)
* 使用root身份改檔案權限
* 更改檔案權限，指令：chmod u=rwx,g=rwx,o=rwx /home/examuser4/securetty
* 切換帳號至examuser4 ，指令：su - examuser4
* 查看帳號權限，指令：ll
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-2-03.png)

# 建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)
* 進到主目錄，指令：cd /
* 建立新的資料，指令：mkdir examdata 
* 確認資料夾新增成功，指令：ls
* 進入examdata資料夾，指令：cd examdata
* 新增檔案change.txt，指令：touch change.txt
* 確認檔案新增成功，指令：ls
* 查看檔案的擁有者與權限，指令：ll
* 更改檔案擁有者為sshd，指令：chown sshd change.txt
* 更改檔案的群組為users，指令：chgrp users change.txt
* 更改檔案權限為-rw-r-----，指令：chmod u=rw,q=r,0= change.txt
* 檢查檔案權限及擁有者是否修改成功，指令：ll
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-2-04.jpeg)
* 更改時間，指令：touch -t 201212211200 change.txt
 > 年月日時分之間不需要空格
* 檢查時間是否修正成功，指令：ll
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-2-05.png)



## 3.

# 使用 root 的身份建立底下的檔案與權限：
1. drwxrwxr-x  root root /dev/shm/unit05/
2. drwxr-xr--  root root /dev/shm/unit05/dir1/
3. -rw-r--r--  root root /dev/shm/unit05/dir1/file1 (複製來自 /etc/hosts)
4. drwxr-x--x  root root /dev/shm/unit05/dir2/
5. -rw-r--r--  root root /dev/shm/unit05/dir2/file2 (複製來自 /etc/hosts)
6. drwxr-xr-x  root root /dev/shm/unit05/dir3/
7. -rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (複製來自 /etc/hosts)
8. drwxrwxrwx  root root /dev/shm/unit05/dir4/
9. -rw-------  root root /dev/shm/unit05/dir4/file4 (複製來自 /etc/hosts)
 > 以下圖文部分對不上，因為在寫完指令後，我想到更有效率的寫法，因此文字敘述為較有效率的做法，圖則為我在寫時的紀錄。
* 進入主枝幹，指令：cd /
* 進入dev，指令：cd dev/
* 進入shm，指令：cd shm/
* 建立unit05目錄檔，指令：mkdir unit05/
* 修改unit05的權限，指令：chmod u=rwx,g=rwx,o=rx unit05
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-3-05.png)
* 進入unit05，指令： cd unit05/
* 建立 dir1,dir2,dir3,dir4 資料夾
 > 指令
2. mkdir dir1/
3. mkdir dir2/
4. mkdir dir3/
5. mkdir dir4/
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-3-01.jpeg)
* 修改 dir1,dir2,dir3,dir4 的權限
 > 指令
 1. chmod u=rwx,g=rx,o=r dir1
 2. chmod u=rwx,g=rx,o=x dir2
 3. chmod u=rwx,g=rx,o=rx dir3
 4. chmod u=rwx,g=rwx,o=rwx dir4
* 複製/etc/hosts至 dir1,dir2,dir3,dir4，檔名改為 file1,file2,file3,file4。
 > 指令
1. cp /etc/hosts /dev/shm/unit05/dir1/file1
2. cp /etc/hosts /dev/shm/unit05/dir2/file2
3. cp /etc/hosts /dev/shm/unit05/dir3/file3
4. cp /etc/hosts /dev/shm/unit05/dir4/file4
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-3-02.png)
* 進入 dir1，修改 file1 權限，
 > 指令：
1. cd dir1/
2. chmod u=rw,g=r,o=r file1
* 回上頁，指令：..
* 進入 dir2，修改 file2 權限，
 > 指令：
1. cd dir2/
2. chmod u=rw,g=r,o=r file2
* 回上頁，指令：..
* 進入 dir3，修改 file3 權限，
 > 指令：
1. cd dir3/
2. chmod u=rw,g=rw,o=rw file3
* 回上頁，指令：..
* 進入 dir4，修改 file4 權限，
 > 指令：
1. cd dir4/
2. chmod u=rwx,g=rwx,o=rwx file4
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-3-06.png)
# 請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
* 因為examuser1是other 
1. dir1 的結果只能讀。
2. dir2 只能執行，所以看不到任何東西。
3. dir3 全部都能顯示，只是無法修改。
4. dir4 所有的權限都開放了，所以能任意使用。
 > 執行狀況如圖
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-3-07.png)

# 用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？
* 因為examuser1是other 
1. dir1 的結果只能讀。
2. dir2 的結果只能讀。
3. dir3 可讀可改。
4. dir4 所有的權限都鎖起來了。
 > 執行狀況如圖
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-3/ACS107144/3-3-08.png)

# 用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？
* 因為examuser1是other 
1. vim /dev/shm/unit05/dir1/file1，無法用w:儲存，因為other沒有file1的修改權限
2. vim /dev/shm/unit05/dir2/file2，無法用w:儲存，因為other沒有file2的修改權限
3. vim /dev/shm/unit05/dir3/file3，可用w:儲存，因為other有file3的修改權限
4. vim /dev/shm/unit05/dir4/file4，無法用w:儲存，因為other沒有file4的修改權限





