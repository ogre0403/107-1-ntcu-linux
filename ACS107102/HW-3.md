#### Linux檔案權限和基礎帳號管理

## 建立帳號
1.登入root身分
2.建立三個帳號examuser1,examuser2,examuser3，密碼皆為ItIsExam
  * useradd examuser 建立
  * passwd examuser 修改密碼
3.檢查帳號(UID/GID)
  * id examuser1
     wid=1001  gid=1001  groups=1001
  * id examuser2
     wid=1002  gid=1002  groups=1002
  * id examuser3
     wid=1003  gid=1003  groups=1003
  * id         (root身分)
     wid=0  gid=0  groups=0
----------------------------------------------------

## 刪除帳號
1.userdel examuser3 -r
  * -r 連同家目錄刪除
2.userdel examuser1
  * 只刪除使用者
3.檢查使用者
  * ll -d /home/examuser
  * 檔案權限:
   (1)drwx------. 2 1001 1001 62 Oct 15:50 /home/examuser1
   (2)drwx------. 2 examuser2 examuser2 62 Oct 15:51 /home/examuser2
   (3)No such file or directory
----------------------------------------------------

## 重建帳號
1.useradd -u 1001 -U examuser1
2.檢查使用者(ll -d /home/examuser)
  * drwx------. 2 examuser1 examuser1 62 Oct 15:50 /home/examuser1
3.passwd examuser1 修改密碼
----------------------------------------------------

## 建立修改身分及檔案
1.建立examuser4
2.使用root將/etc/securetty複製給examuser4
  * cp /etc/securetty /home/examuser4
3.檢查是否有複製
  (1)su examuser4 進入examuser4帳號
  (2)cd /home/examuser4 切換目錄
  (3)ll 檢查securetty是否存在
4.修改權限
  (1)回到root帳號
  (2)chmod u+x,g+rwx,o+rwx securetty
  (3)ll 檢查是否修改成功
5.建立及修改/examdata/change.txt
  (1)mkdir examdata
  (2)cd examdata
  (3)vi change.txt
  (4)[Esc]，:wq
  (5)修改擁有者 chown sshd change.txt
  (6)修改群組 chgrp users change.txt
  (7)修改權限 chmod (sshd可寫可讀，users可讀，其他人沒權限)
  (8)修改時間 touch -t 201212210829[YYYYMMDDhhmm]
----------------------------------------------------


## root身分建檔案與權限
1.建立目錄   mkdir + 目錄名稱
2.切換目錄   cd + 目錄名稱
3.建立檔名     vi + 檔名
  * 進入檔案中，使用[esc]，:w(儲存)q(離開)
4.切換回上層目錄  cd ..
5.修改權限   chmod + u/g/o/a + +/-/= + 檔名
  最後改為
drwxrwxr-x  root root /dev/shm/unit05/
drwxr-xr--  root root /dev/shm/unit05/dir1/
-rw-r--r--  root root /dev/shm/unit05/dir1/file1
drwxr-x--x  root root /dev/shm/unit05/dir2/
-rw-r--r--  root root /dev/shm/unit05/dir2/file2
drwxr-xr-x  root root /dev/shm/unit05/dir3/
-rw-rw-rw-  root root /dev/shm/unit05/dir3/file3
drwxrwxrwx  root root /dev/shm/unit05/dir4/
-rw-------  root root /dev/shm/unit05/dir4/file4
----------------------------------------------------

## 一般使用者身分
1.root切換成一般使用者
  * su + 用戶名
2.ls -l /dev/shm/unit05/dir[1-4]檢查輸出結果
  無法使用此方法，所以利用cd切換目錄
  (1)先使用cd ~
  (2)再用cd .. (home)
  (3)cd .. (/)
  (4)cd dev
  (5)cd shm
  (6)cd unit05
  (7)cd dir[1~4]
   - dir1 不行
   - dir2 行
   - dir3 行
   - dir4 行
    * 猜測可能是other的權限沒有x(執行)而無法開啟
3.ls -l /dev/shm/unit05/dir[1~4]/file[1~4]檢查輸出結果
  方法同上，再多切一次到file[1~4]
  - dir1/file1 不行
  - dir2/file2 不行
  - dir3/file3 不行
  - dir4/file4 不行
    * 猜測可能是other的權限沒有x(執行)而無法開啟
4.vi /dev/shm/unit05/dir1/file1 ~ vi /dev/shm/unit05/dir4/file4嘗試儲存
  - vi /dev/shm/unit05/dir1/file1 無法儲存
  - vi /dev/shm/unit05/dir2/file2 無法儲存
  - vi /dev/shm/unit05/dir3/file3 無法儲存
  - vi /dev/shm/unit05/dir4/file4 無法儲存
    * 猜測可能是other的權限沒有w(編輯)而無法開啟