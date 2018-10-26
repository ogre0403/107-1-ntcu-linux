#1
1.輸入#useradd examuser1依序建立三個帳號:examuser1, examuser2, examuser3。再輸入#passwd examuser1然後會冒出new password:，再輸入ItIsExam，會出現Retype new password:再輸入一次密碼然後重複此動作直到設定完三個帳號。

2.使用# userdel -r examuser3刪除examuser3帳號和家目錄,因為刪除後未出現敘述，故無法確定是否刪除，為確定是否刪除此帳號與目錄,故輸入一樣指令,其顯示examuser3不存在，才確定examuser3已刪除。

3.輸入# id examuser1查examuser1的id,發現UID與GID和groups皆為1000,然後再輸入# userdel examuser1刪除此帳號。

4.輸入#adduser -u 1000 examuser1，建立帳號，再輸入passwd examuser1並更改密碼為qwe1234。

#2
1.輸入#useradd examuser4，再輸入#passwd examuser4，我輸入的密碼為vivi1234，它顯示BAD PASSWORD可能是因為我的密碼太過於簡單。

2.要將securetty複製到examuser4，，用cd指令移動回etc資料夾下，所以輸入指令cp /etc/securetty /home/examuser4 ，就完成了複製securetty。

3.然後要修改他的權限故依序輸入指令charp examuser4 /home/examuser4/securetty。

4.再輸入chmod g=rwx /home/examuser4/securetty。

5.最後再輸入ll /home/examuser4/securetty看是否完成,此步驟因只應不熟把ll看成11害我思考許久,故先跳過,直至下一題才發現問題所在。

6用ls -l查看一次securetty的權限，可以發現已經變為examuser4所擁有，但對自己的權限仍是rw-，只能讀和寫，但不能執行。

7.因為原本沒有examdata資料夾，所以要先創建一個，輸入指令mkdir examdata，然後touch /examdata/change.txt,創建change.txt。

8.為了更改examuser4對securetty的權限，讓examuser4可以執行securetty，輸入chmod 640 change.txt，其中6代表使用者可讀取、可寫入檔案，4代表群組的人和其他人可讀取但不可寫入、執行檔案。其中1代表執行,2代表寫入,4代表讀取。輸入完指令後用ls -l確認權限是否更改正確，可以看到權限已經更改為640，使用者可讀取、可寫入。

9.雖然擁有者已經更改為sshd，但擁有群組依然是root，輸入指令chgrp users change.txt，更改群組擁有者為users。

10.輸入chown sshd change.txt，發現檔案的擁有者已經變為sshd。

11.更改時間輸入touch -d 20121231 /examdata/ change.txt，再輸入ll /examdata/change.txt查看時間，時間變為Dec 31 2012，這樣就修改成功了。

#3
請使用 root 的身份建立底下的檔案與權限,前面是d代表是目錄,打mkdir 目錄名稱是cd的目錄名稱，進入目錄裡再依題目所需重複上面兩個動作,前面-代表是檔案,打vi 檔案名稱然後會跳出畫面再按esc然後:wq即可建立檔案。

使用一般使用者的身份進入su帳號

使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？

1.打ls -l /dev/shm/unit05/dir1結果不行,因為前面是r--，所以沒有權限

2.打ls -l /dev/shm/unit05/dir2結果可以,因為前面是--x，所以有權限

3.打ls -l /dev/shm/unit05/dir3結果可以,因為前面是r-x，所以有權限

4.打ls -l /dev/shm/unit05/dir4結果可以,因為前面是rwx，所以有權限

5.打ls -l /dev/shm/unit05/dir1/file1,結果不行,因為examuser對file1的權限為r--

6.打ls -l /dev/shm/unit05/dir1/file2,結果不行,因為examuser對file2的權限為r--

7.打ls -l /dev/shm/unit05/dir1/file3,結果可以,因為examuser對file3的權限為rw-

8.打ls -l /dev/shm/unit05/dir1/file4,結果可以,因為examuser對file1的權限為---

9.打vim /dev/shm/unit05/dir1/file1,結果無法儲存,因為權限為r--

10.打vim /dev/shm/unit05/dir2/file2,結果無法儲存,因為權限為r--

11.打vim /dev/shm/unit05/dir3/file3,結果可以儲存,因為權限為rw-

12.打vim /dev/shm/unit05/dir4/file4,結果不可儲存,因為權限為---


![](https://ppt.cc/f4feQx@.png)

![](https://ppt.cc/fdt59x@.png)

![](https://ppt.cc/f2xnYx@.png)




