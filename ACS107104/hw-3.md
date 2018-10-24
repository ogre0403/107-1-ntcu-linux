1.登錄帳號
2.切換成root
3.打useradd examuser1建立帳號，依你所需重複第三點建立檔案
4.打passwd examuser1更改密碼為ItIsExam
5.打cd /home→ll→即可查看有無成功
刪除系統中的 examuser3 這個帳號，同時將這個帳號的家目錄與郵件檔案同步刪除。
1.打userdel -r examuser3
2.打cd /home→ll→即可查看有無成功
examuser1 不小心被管理員刪除了，但是這個帳號的家目錄與相關郵件都還存在。
1.先打id examuser1查看examuser1的GID和UID
2.打userdel examuser1→cd /home→ll→即可查看有無成功
重建examuser1
1.打useradd -u 剛剛記下的GID和UID examuser1→passwd examuser1→cd /home→ll→即可查看有無成功
用 root 將 /etc/securetty 複製給 examuser4，且這個帳號要能夠完整使用該檔案才行，(即有所有的權限)。
1.建立examuser4
2.打cp /etc/securetty /home/examuser4→chmod u=rwx,g=rwx,o=rwx /home/examuser4/securetty→su - examuser4→cd /home/examuser4→ll→即可完成
建立一個名為 /examdata/change.txt 的空檔案，這個檔案的擁有者為 sshd，擁有群組為 users，sshd 可讀可寫，users 群組成員可讀， 其他人沒權限。且這個檔案的修改日期請調整成 2012 年 12 月 21 日 (日期正確即可，時間隨便)
轉換成root→建立examdata→cd examdata→vi change.txt→chown sshd change.txt(更改擁有者)→chdrp users change.txt(更改群組)→chmod u=rw,g=r,o= change.txt(更改權限)→ll查看有無成功→touch -t 年月日時間 change.txt→ll -l→完成
請使用 root 的身份建立底下的檔案與權限
1.前面是d代表是目錄
2.打mkdir 目錄名稱→cd 目錄名稱，進入目錄裡→依題目所需重複上面兩個動作
3.前面-代表是檔案
4.打vi 檔案名稱→跳出畫面→按esc→:wq→即可建立檔案
使用一般使用者 的身份進入
su 帳號
使用 ls -l /dev/shm/unit05/dir[1-4] 依據輸出的結果說明為何會產生這些問題？
打ls -l /dev/shm/unit05/dir1結果不行，因為前面是r--，所以沒有權限
打ls -l /dev/shm/unit05/dir2結果可以，因為前面是--x，所以有權限
打ls -l /dev/shm/unit05/dir3結果可以，因為前面是r-x，所以有權限
打ls -l /dev/shm/unit05/dir4結果可以，因為前面是rwx，所以有權限
打ls -l /dev/shm/unit05/dir1/file1，結果不行，因為examuser對file1的權限為r--
打ls -l /dev/shm/unit05/dir1/file2，結果不行，因為examuser對file2的權限為r--
打ls -l /dev/shm/unit05/dir1/file3，結果可以，因為examuser對file3的權限為rw-
打ls -l /dev/shm/unit05/dir1/file4，結果可以，因為examuser對file1的權限為---
打vim /dev/shm/unit05/dir1/file1，結果無法儲存，因為權限為r--
打vim /dev/shm/unit05/dir2/file2，結果無法儲存，因為權限為r--
打vim /dev/shm/unit05/dir3/file3，結果可以儲存，因為權限為rw-
打vim /dev/shm/unit05/dir4/file4，結果不可儲存，因為權限為---