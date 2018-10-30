#1-1建立三個用戶，帳號名稱分別為： examuser1, examuser2, examuser3 ，同時三個用戶的密碼都是『 ItIsExam 』。
*1.切換root帳號
*2.利用"useradd"指令建立examuser1/examuser2/examuser3帳號
*3.利用"passwd"指令設定examuser1/examuser2/examuser3的密碼為**ItIsExam **

#1-2請刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。
*1."userdel -r examuser3"
*2."id examuser3"→"no such user"

#1-3examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。請參考這個帳號可能的家目錄所保留的 UID 與 GID， 並嘗試以該帳號原有的 UID/GID 資訊來重建該帳號。
**1."id examuser1"查看examuser1的UID和GID，並記下。
**"userdel examuser1"刪除examuser1。由於指令沒有輸入"-r"，所以家目錄和相關郵件都還存在。(但"id examuser1"還是會"no such user")**
*1."useradd -u 剛剛查看的UID -g 剛剛查看的GID examuser1"
*2."passwd examuser1"密碼ItIsExam

#2-1建立examuser4使用者帳號，密碼任意。
*1."useradd examuser4"→"passwd examuser4"

#2-2使用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。
*1.建立/etc/securetty
*2."chown examuser4 /etc/securetty"→"chmod u=rwx,g=rw,o=r /etc/securetty"

#2-3建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)
*1."mkdir examdata"→"cd examdata"→"vi change.txt"
*2."chown sshd change.txt"→"chdrp users change.txt"→"chmod u=rw,g=r,o=0 change.txt"
*3."touch -t 201212211357 change.txt"

#3-1請使用 root 的身份建立底下的檔案與權限：
**建立/dev/shm/unit05**
*1."cd dev"→"cd shm"→"chmod u=rwx,g=rwx,o=rx unit05"
*2."cd unit05"→"mkdir dir1"→"chmod u=rwx,g=rx,o=r dir1"
*3."cd dir1"→"mkdir file1"→"cp /etc/hosts /dev/shm/unit05/dir1/file1"→"chmod u=rw,g=r,o=r file1"
*4."cd unit05"→"mkdir dir2"→"chmod u=rwx,g=rx,o=x dir2"
*5."cd dir2"→"mkdir file2"→"cp /etc/hosts /dev/shm/unit05/dir1/file2"→"chmod u=rw,g=r,o=r file2"
*6."cd unit05"→"mkdir dir3"→"chmod u=rwx,g=rx,o=rx dir3"
*7."cd dir3"→"mkdir file3"→"cp /etc/hosts /dev/shm/unit05/dir1/file3"→"chmod u=rw,g=rw,o=rw file3"
*8."cd unit05"→"mkdir dir4"→"chmod u=rwx,g=rwx,o=rwx dir4"
*9."cd dir4"→"mkdir file4"→"cp /etc/hosts /dev/shm/unit05/dir1/file4"→"chmod u=rw,g=0,o=0 file4"

#3-2使用一般使用者 的身份進行各項工作


#3-3請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
*1.輸入"ls -l /dev/shm/unit05/dir[1-4]"
**dir1權限為u=rwx,g=rx,o=r→root使用者可讀可寫可執行，root群組可讀可執行，一般使用者可讀
**dir2權限為u=rwx,g=rx,o=x→root使用者可讀可寫可執行，root群組可讀可執行，一般使用者可執行
**dir3權限為u=rwx,g=rx,o=rx→root使用者可讀可寫可執行，root群組可讀可執行，一般使用者可讀可執行
**dir4權限為u=rwx,g=rwx,o=rwx→root使用者可讀可寫可執行，root群組可讀可寫可執行，一般使用者可讀可寫可執行

#3-4請使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？
*1.輸入"ls -l /dev/shm/unit05/dir1/[dir1/file1 ~ dir4/file4]"
**dir1/file1權限為u=rw,g=r,o=r→root使用者可讀可寫，root群組可讀，一般使用者可讀
**dir2/file2權限為u=rw,g=r,o=r→root使用者可讀可寫，root群組可讀，一般使用者可讀
**dir3/file3權限為u=rw,g=rw,o=rw→root使用者可讀可寫，root群組可讀可寫，一般使用者可讀可寫
**dir4/file4權限為u=rw,g=0,o=0→root使用者可讀可寫，root群組沒有權限，一般使用者沒有權限

#3-5請使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？
*1."vim /dev/shm/unit05/[dir1/file1 ~ dir4/file4]"→"command not found"
**vim /dev/shm/unit05/dir1/file1，結果無法儲存，因為權限為r--
**vim /dev/shm/unit05/dir2/file2，結果無法儲存，因為權限為r--
**vim /dev/shm/unit05/dir3/file3，結果可以儲存，因為權限為rw-
**vim /dev/shm/unit05/dir4/file4，結果不可儲存，因為權限為---