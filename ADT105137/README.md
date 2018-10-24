# ADT105137_HW3
第一題

1.建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。

a.用useradd指令創造帳號，用passwd設定的密碼。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%80%E9%A1%8C/hw3-1-1.PNG)

2.刪除examuser3帳號，連同家目錄和郵件目錄一同刪除。

b.用userdel指令，options為 –r 可以刪除家目錄和郵件檔案。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%80%E9%A1%8C/hw3-1-2.PNG)

3.examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。而這個帳號的密碼請給予 ItIsExam 的樣式。

c.用userdel指令刪除examuser1但不要-r 以保留家目錄。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%80%E9%A1%8C/hw3-1-3.PNG)

d.用useradd重建examuser1 加入-u的options以指定帳號id，接著重設密碼。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%80%E9%A1%8C/hw3-1-4.PNG)

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%80%E9%A1%8C/hw3-1-5.PNG)

第二題:

1.建立examuser4使用者帳號，密碼任意。

a.用useradd指令創造帳號，用passwd設定examuser4的密碼。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%BA%8C%E9%A1%8C/hw3-2-1.PNG)

2.使用root將/etc/securetty複製給examuser4，並有所有權限。

a.使用複製指令cp ，將/etc/securetty複製到examuser4帳號目錄下。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%BA%8C%E9%A1%8C/hw3-2-2.PNG)

b.再用chown、chgrp改成examuser4，用chmod 777。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%BA%8C%E9%A1%8C/hw3-2-3.PNG)

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%BA%8C%E9%A1%8C/hw3-2-4.PNG)

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%BA%8C%E9%A1%8C/hw3-2-5.PNG)

3.建立一個名為/examdata/change.txt的空檔案，這個檔案的擁有者為sshd，擁有權組為users，sshd可讀可寫，users群組可讀，其他人沒權限，檔案修改日期2012/12/21，時間隨便。

a.使用vi 指令創建檔案。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%BA%8C%E9%A1%8C/%E7%AC%AC%E4%BA%8C%E5%B0%8F%E9%A1%8C/hw3-2-6.PNG)

b.再用chown、chgrp改成sshd、users，用chmod 640  。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%BA%8C%E9%A1%8C/%E7%AC%AC%E4%BA%8C%E5%B0%8F%E9%A1%8C/hw3-2-7.PNG)

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%BA%8C%E9%A1%8C/%E7%AC%AC%E4%BA%8C%E5%B0%8F%E9%A1%8C/hw3-2-8.PNG)

c.用touch指令修改時間 ，option使用-t ，可以自訂修改時間 (如果不加-t是修改成現在時間)。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%BA%8C%E9%A1%8C/%E7%AC%AC%E4%BA%8C%E5%B0%8F%E9%A1%8C/hw3-2-9.PNG)


第三題

1.請使用 ls –l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為啥會產生這些問題?

a.創建unit05目錄，使用mkdir指令，options使用-m可以設定權限。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%89%E9%A1%8C/hw3-3-1.PNG)

b.使用 root 的身份建立的檔案與權限。使用一般者帳號，然後移到/dev/shm目錄，使用mkdir創建目錄檔，options使用 -m 設定rxe權限。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%89%E9%A1%8C/hw3-3-3.PNG)

c.請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%89%E9%A1%8C/hw3-3-4%20%E7%AC%AC%E4%B8%80%E9%A1%8C.PNG)

Ans:
dir1會這樣顯示是因為dir1這個目錄檔的x(others)沒有權限，為甚麼有問號我並不清楚(下面圖片為dir1有無x(others)的差別)。dir2是因為dir2的r(others)沒有權限，所以不能看目錄下的檔名資料。dir3、dir4因為都有r、x(others)所以都可以看其檔案資料。

![image](https://github.com/Yubo0826/1017/blob/master/3-1%E5%AF%A6%E9%A9%97.PNG)

c.請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？

Ans:
File1: 因為該檔案目錄上一層dir1沒有給予others X權限，所以無法進入，看到file1檔案。
File2: 上一層目錄dir2有x(others)權限，所以可以進入，又因為file2有r(others)權限，因而看的到file2檔案資料。
File3: dir3有x (others)權限，file3有r (others)權限 ，因而看的到。
File4: 同File3。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%89%E9%A1%8C/hw3-3-5%20%E7%AC%AC%E4%BA%8C%E9%A1%8C.PNG)

d.	請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？
File1: 不可以，因為files1 others只有讀取(r)的權限。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%89%E9%A1%8C/hw3-3-6%20%E7%AC%AC%E4%B8%89%E9%A1%8C.PNG)

File2: 同上。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%89%E9%A1%8C/hw3-3-7%20%E7%AC%AC%E4%B8%89%E9%A1%8Cdir2.PNG)

File3: 可以。因為files3 other 有寫入(w)的權限。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%89%E9%A1%8C/hw3-3-7%20%E7%AC%AC%E4%B8%89%E9%A1%8Cdir3%20%E5%8F%AF%E4%BB%A5%E5%84%B2%E5%AD%98.PNG)

File4: 不可以。File4 others完全沒有權限。

![image](https://github.com/Yubo0826/1017/blob/master/HW3_LINUX/%E7%AC%AC%E4%B8%89%E9%A1%8C/hw3-3-7%20%E7%AC%AC%E4%B8%89%E9%A1%8Cdir4%20%E5%AE%8C%E5%85%A8%E6%B2%92%E6%AC%8A%E9%99%90.PNG)

