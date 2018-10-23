+ (I)  ![GITHUB](https://i.imgur.com/Is80iRv.jpg "git圖示")
 
+ 建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3

+ 密碼設定為ItIsExam

![GITHUB](https://i.imgur.com/96uHFZx.jpg "git圖示")

+ 使用「userdel -r examuser3」刪除系統中的examuser3帳號(包含家目錄.郵件檔案)

+ 使用「userdel examuser1」刪除 examuser1 ,此時發現家目錄.郵件檔案仍然留存

+ 利用UID/GID重建 examuser1相關帳號資料 密碼設定為ItIsExam

![GITHUB](https://i.imgur.com/jtF8FtJ.jpg "git圖示")
![GITHUB](https://i.imgur.com/Is80iRv.jpg "git圖示")

+ (II)

+ 建立examuser4

![GITHUB](https://i.imgur.com/t0kKm5S.jpg "git圖示")

+ 使用 root 將 /etc/securetty 複製給 examuser4

![GITHUB](https://i.imgur.com/kFdrXbl.jpg "git圖示")

+ 利用ROOT狀態,修改/etc/securetty之權限

![GITHUB](https://i.imgur.com/96uHFZx.jpg "git圖示")

+ 建立一個名為 /examdata/change.txt 的空檔案，擁有者:sshd，群組:users，sshd可讀可寫，users 群組成員可讀，其他人沒權限。
+ 將修改日期請調整成 2012 年 12 月 21 日 

[Imgur](https://i.imgur.com/dgM7LGH.jpg)

[Imgur](https://i.imgur.com/QgixQej.jpg)

+ (III)

+ 使用root進入/>/dev/shm，建立資料夾unit05,並修改其權限

+ 進去unit05新增dir1.dir2.dir3.dir4.dir5,並修改其權限

+ 將/etc/hosts複製至/dev/shm/unit05/dir1/file1 (同理做到file4)

[Imgur](https://i.imgur.com/VO7HBy4.jpg)

+ 進入dir1，先利用"ll"查看初始權限，再利用"ls"查看file1是否存在，並修改原先的權限。 (同理進入其他資料夾做修改) 

[Imgur](https://i.imgur.com/xzwa9V3.jpg)

+ 我將帳號切換為examuser1

+ 使用指令 ls -l /dev/shm/unit05/dir[1-4] 
+ examuser1對於dir1和dir2沒有權限，dir3(o=r-x)和dir4(o=rwx)有權限能夠任意使用。 

[Imgur](https://i.imgur.com/S6XQhv0.jpg)

+ 使用指令 ls -l /dev/shm/unit05/dir1/file1 ，
依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，
結果為examuser1對於file1(沒有權限)、file2(o=r--)、file3(o=rw-)有權限能夠任意使用、file4(o=---)

[Imgur](https://i.imgur.com/wKns2PE.jpg)

+ 使用 vim /dev/shm/unit05/dir1/file1 ~ file4
+ 嘗試儲存結果出現"command not found"
+ 表示examuser1不具有執行"vim"指令的權限，所以不能儲存

[Imgur](https://i.imgur.com/VEw9sSy.jpg)









