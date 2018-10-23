第一題
#examuser1.2.3
輸入useradd examuser1
輸入passwd examuser1
顯示New Password:並輸入新密碼
我設定為ItIsExam
系統會再確認一遍密碼
然後重複一樣的動作新增examuser2和examuser3，密碼皆為ItIsExam
 
#刪除examuser3	
輸入userdel -r examuser3刪除使用者
檢查是否成功刪除
#恢復examuser1 
輸入userdel examuser1

輸入sudo useradd -u 1001 -m examuser1</li>
輸入sudo passwd examuser1</li>
顯示New Password:並輸入ItIsExam</li></li>
輸入id examuser1</li>
顯示
	uid=1001(examuser1) gid=1001(examuser1) groups=1001(examuser1)</li>
第二題
#建立examuser4 
輸入useradd examuser4
顯示New Password:並輸入新密碼
我設定為sotired
#複製檔案並更改權限 
輸入cp /etc/securetty /home/examuser4
輸入ls /home/examuser4檢查是否有securetty
輸入chmod u=rwx,g=rwx,o=rwx /home/examuser4/securetty
#檢查
輸入su - examuser4切換使用者
輸入ll檢查是否更改權限
#新建檔案 
輸入cd /home/examuser4/進入目錄
輸入mkdir examdata建立資料夾
輸入ls
會顯示
examdata	securetty 
輸入cd examdata進入
再輸入touch change.txt建立檔案
輸入ll檢查
#更改權限 
用回ROOT
輸入cd /home/examuser4/examdata/
輸入chown sshd change.txt更改擁有者為sshd
輸入chgrp users change.txt更改群組為users
輸入chmod u=rw,g=r,o= change.txt更改權限為-rw-r
輸入ll檢查
應會顯示
	-rw-r. 1	sshd users 0	日期	時間	change.txt
#更改時間 
輸入touch -t 20121231 change.txt

第三題
 #root身分建立檔案與權限 
輸入cd /dev/進入dev
再輸入cd shm/進入shm
輸入mkdir unit05/ 建立unit05目錄檔
輸入chmod u=rwx,g=rwx,o=rx unit05 修改unit05的權限
輸入mkdir 分別加上建立四個資料夾
修改dir1,dir2,dir3,dir4權限
	chmod u=rwx,g=rx,o=r dir1
	chmod u=rwx,g=rx,o=x dir2 
	chmod u=rwx,g=rx,o=rx dir3
	chmod u=rwx,g=rwx,o=rwx dir4 </li>
複製/etc/hosts至 dir1,dir2,dir3,dir4，將檔名改為 file1,file2,file3,file4
	cp /etc/hosts /dev/shm/unit05/dir1/file1
	cp /etc/hosts /dev/shm/unit05/dir2/file2
	cp /etc/hosts /dev/shm/unit05/dir3/file3
	cp /etc/hosts /dev/shm/unit05/dir4/file4 
#進入dir1修改file1權限
輸入cd dir1/
再輸入chmod u=rw,g=r,o=r file1</li>
#修改file2權限
輸入cd dir2/
輸入chmod u=rw,g=r,o=r file2
#修改file3權限
輸入cd dir3/
輸入chmod u=rw,g=r,o=r file3
#修改file4權限
輸入cd dir4/
輸入chmod u=rw,g=r,o=r file4
#請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
全部都不能執行因為都沒有執行的權限
#使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)
說明為何可以/不可以儲存？
只有file3可以儲存 因為other有file3的修改權限