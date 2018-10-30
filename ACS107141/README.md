##1 
<ol>
<li>登入CentOS</li>
#建立帳戶 
<li>輸入useradd examuser1</li>
<li>輸入passwd examuser1</li>
<li>顯示New Password:並輸入ItIsExam</li>
<li>系統會再確認一遍密碼，再次輸入即可完成設定</li>
<li>根據2~6的步驟，依序設定兩個user，分別為examuser2和examuser3，密碼皆為ItIsExam</li>
<li>完成後輸入ll /home/檢查</li>
<li>應會顯示
	drwx------. 2 examuser1		examuser1	日期	時間	examuser1 
	drwx------. 2 examuser2		examuser2	日期	時間	examuser2 
	drwx------. 2 examuser3		examuser3	日期	時間	examuser3	</li> 
#刪除examuser3	
<li>輸入userdel -r examuser3</li>
<li>輸入$ll /home/檢查</li>
<li>應會顯示
	drwx------. 2 examuser1		examuser1	日期	時間	examuser1 
	drwx------. 2 examuser2		examuser2	日期	時間	examuser2 </li>
#恢復examuser1 
<li>輸入userdel examuser1模擬情形</li>
<li>輸入ll /home/檢查</li>
<li>應會顯示
	drwx------. 2 1001			1001		日期	時間	examuser1 
	drwx------. 2 examuser2		examuser2	日期	時間	examuser2 </li>
<li>輸入sudo useradd -u 1001 -m examuser1</li>
<li>輸入sudo passwd examuser1</li>
<li>顯示New Password:並輸入ItIsExam</li></li>
<li>輸入id examuser1</li>
<li>顯示
	uid=1001(examuser1) gid=1001(examuser1) groups=1001(examuser1)</li>
</ol>

##2
<ol>
#建立examuser4 
<li>輸入useradd examuser4</li>
<li>輸入passwd examuser4</li>
<li>顯示New Password:設定密碼</li></li>
#複製檔案並更改權限 
<li>輸入cp /etc/securetty /home/examuser4</li>
<li>輸入ls /home/examuser4檢查是否有securetty</li>
<li>輸入chmod u=rwx,g=rwx,o=rwx /home/examuser4/securetty</li>
#CHECK 
<li>輸入su - examuser4切換使用者</li>
<li>輸入ll檢查是否更改權限</li>
#新建檔案 
<li>輸入cd /home/examuser4/進入目錄</li>
<li>輸入mkdir examdata建立資料夾</li>
<li>輸入ls</li>
<li>如顯示
	examdata	securetty 代表成功</li>
<li>輸入cd examdata進入</li>
<li>輸入touch change.txt建立檔案</li>
<li>輸入ll檢查</li>
<li>應會顯示
	-rw-rw-r--. 1	examuser4 examuser4 0	日期	時間	change.txt</li>
#改權限 
<li>切回ROOT</li>
<li>輸入cd /home/examuser4/examdata/</li>
<li>輸入chown sshd change.txt更改擁有者為sshd</li>
<li>輸入chgrp users change.txt更改群組為users</li>
<li>輸入chmod u=rw,g=r,o= change.txt更改權限為-rw-r-----</li>
<li>輸入ll檢查</li>
<li>應會顯示
	-rw-r-----. 1	sshd users 0	日期	時間	change.txt</li></li>
#改時間 
<li>輸入touch -t 201212210807 change.txt</li>
</ol>

##3

#root身分建立檔案與權限 
<li>輸入cd /dev/shm/進入資料夾</li>
<li>輸入mkdir unit05建立檔案</li>
<li>輸入chmod u=rwx,g=rwx,o=rx unit05</li>
<li>輸入cd unit05進入</li>
<li>輸入mkdir 分別加上建立四個資料夾 </li>
<li>修改dir1,dir2,dir3,dir4權限如下
	dir1→chmod u=rwx,g=rx,o=r dir1
	dir2→chmod u=rwx,g=rx,o=x dir2 
	dir3→chmod u=rwx,g=rx,o=rx dir3
	dir4→chmod u=rwx,g=rwx,o=rwx dir4 </li>
<li>複製/etc/hosts至 dir1,dir2,dir3,dir4，將檔名改為 file1,file2,file3,file4
	dir1→cp /etc/hosts /dev/shm/unit05/dir1/file1
	dir2→cp /etc/hosts /dev/shm/unit05/dir2/file2
	dir3→cp /etc/hosts /dev/shm/unit05/dir3/file3
	dir4→cp /etc/hosts /dev/shm/unit05/dir4/file4 </li>
#修改file1權限
<li>輸入cd unit05/dir1/</li>
<li>輸入chmod u=rw,g=r,o=r file1</li>
#修改file2權限
<li>輸入cd unit05/dir2/</li>
<li>輸入chmod u=rw,g=r,o=r file2</li>
#修改file3權限
<li>輸入cd unit05/dir3/</li>
<li>輸入chmod u=rw,g=rw,o=rw file3</li>
#修改file4權限
<li>輸入cd unit05/dir4/</li>
<li>輸入chmod u=rwx,g=rwx,o=rwx file4</li>
#請使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
<li>dir1唯讀</li>
<li>dir2是只能執行，無法讀</li>
<li>dir3無法修改</li>
<li>dir4可以任意執行</li>
#用 ls -l /dev/shm/unit05/dir1/file1，依序將上述的檔名由 dir1/file1 ~ dir4/file4 執行，依據產生的結果說明為何會如此？
<li>dir1,dir2唯讀</li>
<li>dir3可讀可修改</li>
<li>dir4無法使用</li>
#用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4，嘗試儲存 (或強制儲存)，說明為何可以/不可以儲存？
<li>other沒有改動unit05內4個資料夾的修改權限</li>
</ol> 
