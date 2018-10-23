#1.1
useradd examuser1
passwd examuser1
再輸入新密碼:ItIsExam 然後再驗證一次就行了(忘了截圖，sor)
#1.2
userdel -r examuser3
![](https://ppt.cc/fnrc9x@.png)
(上面打成5了)
#1.3
查看UID跟GID，如果在後一個就直接useradd，不在最後就adduser -u UID examuser1
#2.1
同1.1
#2.2
cp /etc/securetty ~examuser4再
chown examuser4.examuser4 ~examuser4/securetty
![](https://ppt.cc/f60u4x@.png)
#2.3
mkdir /examdata然後mkdir /examdata/change.txt
chgrp users /examdata/change.txt
chmod 740 /examdata/change.txt
chown sshd /examdata/change.txt
最後touch -t 20121221就行了
![](https://ppt.cc/fTxlWx@.png)
#3.1
dir1為r--
dir2為--x
dir3為r-x
dir4為rwx
#3.2
file1為r--
file2為r--
file3為rw-
file4為---
#3.3
不行，因為權限不足