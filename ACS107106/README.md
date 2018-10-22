1.帳號管理任務:

(1)首先進入虛擬機器，使用root登入，接著分別用useradd examuser1，passwd examuser1;useradd examuser2，passwd examuser2;useradd examuser3，passwd examuser3來建立帳號(密碼都是:ItIsExam)。

(2)用userdel -r examuser3 將帳號的家目錄與郵件檔案同步刪除。

(3)用ls -al /home/可以看到不小心被刪除的examuser1的UID和GID，然後用useradd -u UID碼 -U examuser1就可以用UID重建帳號。


2.權限管理任務:

(1)用useradd examuser4，passwd examuser4建立帳號。

(2)用cp /etc/securetty /home/examuser4/，接著用chown examuser4 securetty再用chmod u=rwx, g=rwx, o=rwx examuser4使此帳號擁有完整使用檔案的權限。

(3)用mkdir examdata，接著cd進去examdata裡面，用touch change.txt建立空檔案，用chown sshd change.txt將擁有者改為sshd，接著用chgrp users change.txt將群組改為users，接著用chmod u=rw,g=r,o= change.txt將sshd可讀可寫，users 群組成員可讀， 其他人沒權限，最後用touch -t 20121221 change.txt將檔案的修改日期調整成 2012 年 12 月 21 日。


3.說明操作:
(1)使用 root 的身份登入，cd進去dev，接著打shm，然後用mkdir unit05，接著用chmod u=rwx,g=rwx,o=rx unit05來更改權限。再來cd進入unit05裡，用mkdir dir1，然後chmod u=rwx,g=rx,o=r dir1;再用mkdir dir2，然後chmod u=rwx,g=rx,o=x dir2;再用mkdir dir3，然後chmod u=rwx,g=rx,o=rx dir3;再用mkdir dir4，然後chmod u=rwx,g=rwx,o=rwx dir4。再來用cp /etc/hosts dev/shm/unit05/dir1/file1 進去dir1，然後chmod u=rw,g=r,o=r file1;再cd進入unit05，用cp /etc/hosts dev/shm/unit05/dir2/file2 進去dir2，然後chmod u=rw,g=r,o=r file2;再cd進入unit05，用cp /etc/hosts dev/shm/unit05/dir3/file3 進去dir3，然後chmod u=rw,g=rw,o=rw file3;再cd進入unit05，用cp /etc/hosts dev/shm/unit05/dir4/file4 進去dir4，然後chmod u=rw,g=,o= file4，這樣就建立好檔案與權限了。

(2)使用一般使用者的身份登入，使用 ls -l /dev/shm/unit05/dir1時，會被告知權限不足，但具有r的權限可以查詢檔名，因沒有x的權限，所以會出現問號;使用 ls -l /dev/shm/unit05/dir2時，因沒有r的權限，所以不能查詢檔名;使用 ls -l /dev/shm/unit05/dir3~4時，因都具有r和x的權限，所以可以執行。

(3)在執行dir1/file1 ~ dir4/file4時，因沒有x的權限，所以無法執行。

(4)使用 vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4 儲存時，因dir3有w的權限 所以可以儲存，但dir1,dir2,dir4沒有w的權限，所以不能儲存。
