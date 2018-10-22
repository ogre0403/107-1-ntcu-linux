#linux檔案權限與基礎帳號管理

* (1-1)登入管理者root的帳號，使用"useradd 帳號名稱"建立用戶、"passwd 帳號名稱"給與該帳號自訂的密碼。
 > <分別新增examuser1、examuser2、examuser3，password都是"ItIsExam">
* (1-2)可以利用"id 帳號名稱"觀察帳號的情況(UID、GID、groups)。
* (1-3)利用"userdel -r 帳號名稱"刪除examuser3，且同步刪除家目錄和郵件檔案。(*"-r"的意思是同步刪除家目錄和郵件檔案。)
 > <再用id查看帳號就會發現"no such user"了>
* (1-4)利用"userdel 帳號名稱"刪除examuser1。由於指令沒有輸入"-r"，所以家目錄和郵件檔案都還在。
 > 檢查:<雖然用id查看帳號會發現"no such user"，但其實進入"/home"再使用"ll"查看詳細資訊會發現examuser1的家目錄和郵件檔案都還是存在的>
* (1-5)參考examuser1家目錄保留的UID和GID重建帳號，"useradd -u 1001 -U examuser1"。
 > *"-u"後面接的一組數字為UID，也就是直接指定特定的UID給帳號(examuser1)。*"-U"將/etc/shadow密碼欄的拿掉。
* (1-6)切換進入"/home"，使用"ll"查看詳細資訊，就會發現examuser1重建成功。
 > <記得要給與帳號password:"ItIsExam">
* (2-1)建立新用戶為examuser4，給與其自訂密碼。
 > <"useradd 帳號名稱"、"passwd 帳號名稱">
* (2-2)利用"ls -l"列出原本/etc/securetty的詳細檔案資訊查看原始權限，為"-rw-------"。
 > 再來將/etc/securetty複製給examuser4。(一開始複製給examuser4的時候權限尚未改變，依舊為"-rw-------")
* (2-3)在root為管理者的狀態下修改/etc/securetty的權限。
 > 使用chmod搭配符號修改權限:"chmod u=rwx,g=rwx,o=rwx 絕對路徑"就修改權限完成了。再來切換帳號至examuser4("su - examuser4")，進入/home/examuser4使用"ll"查看權限資訊，就能發現權限已修改完成，為"-rwxrwxrwx"。
* (2-4)回到root，進入"/"，新增資料夾名為examdata("mkdir examdata")，再進入examdata(cd examdata)。
     1. 利用"touch"建立一個名為"change.txt"的空檔案("touch change.txt")，再使用"ls"察看就會再examdata裡看到"change.txt"。
        先使用"ll"查看修改前的權限，為"-rw-r--r--"。
        **"touch"這個指令，我們可以輕易的修訂檔案的日期與時間，並且也可以建立一個空的檔案。**
     2. 修改此檔案的用有者(user)為"sshd"<chown sshd change.txt>、擁有群組(group)為"users"<chgrp users change.txt>。
     3. 更改檔案的權限<chmod u=rw,g=r,o= change.txt>
        **再利用"ll"查看，權限已修改完成。**
     4. 修改檔案的日期為2012年12月21日(時間任意)。( *"-t"的意思是修改時間排序。)
        **<touch -t 201212211234 change.txt>(再使用"ll"查看更改後的權限和時間，就會發現已經修改OK了。)**
* (3-1)使用root進入/>dev>shm，建立資料夾unit05(mkdir unit05)，並修改權限(chmod u=rwx,g=rwx,o=rx unit05)，再使用"ll"查看，權限已修改完成。
* (3-2)進入unit05，分別新增dir1、dir2、dir3、dir4(EX:mkdir dir1)，再修改各個權限(EX:chmod u=rwx,g=rx,o=r dir1)，再使用"ll"查看，權限就修改完成了。
 > <dir1、dir2、dir3、dir4皆是一樣的步驟>
* (3-3)複製/etc/hosts到/dev/shm/unit05/dir1/file1(其他類推)。
 > <EX:cp /etc/hosts /dev/shm/unit05/dir1/file1>
* (3-4)切換進入dir1，先利用"ll"查看初始權限，再利用"ls"查看file1是否存在，再修改其權限，最後再用"ll"檢查權限是否更改成功。(其他類推，但要記得回unit05進入各個資料夾修改及檢查)
* (3-5)切換帳號，使用一般使用者登入(我使用的一般使用者為examuser2登入)。
* (3-6)使用 ls -l /dev/shm/unit05/dir[1-4] 輸入，產生結果為examuser2(身分為Other)對於dir1(o=r--)和dir2(o=--x)"Permission denied"(沒有權限)，dir3(o=r-x)和dir4(o=rwx)有權限能夠任意使用。
* (3-7)使用 ls -l /dev/shm/unit05/dir1/file1 ，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，產生結果為examuser2(身分為Other)對於file1(o=r--)、file2(o=r--)、file4(o=---)"Permission denied"(沒有權限)，file3(o=rw-)有權限能夠任意使用。
* (3-8)使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，會出現"command not found"，代表examuser2沒有執行"vim"指令的權限，所以不能儲存和強制儲存。
