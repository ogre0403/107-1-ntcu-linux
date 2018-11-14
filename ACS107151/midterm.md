### 一.
+ 1.輸入 **uname -r** 看版本資訊
+ 2.輸入 **ver=my kernel version is 4.17.0
+ 3.輸入 **echo $PATH "可以看到PATH的值文為 /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
+ 4.PATH的功用:作業系統會依照PATH環境變數中所設定的路徑順序，喔續尋找個路徑下是否有要使用的指令，若找不到，就會顯示command not found 若多個目錄下都有指令，已優先找到的為主。
***
### 二.
+ 1.d: 代表後面的檔名為目錄檔。
+ 2.擁有者為 root，root 具有 rwx 的權限 (第一組權限)，群組設定為 mail，則所有加入 mail 這個群組的帳號可以具有 rwx 的權限 (第二組權限)，不是 root 也沒有加入 mail 的其，只有 rx 的權限 (第三組權限)，不是 root 也沒有加入 mail 的其，只有 rx 的權限 (第三組權限)
+ 3.擁有者可以可以讀.寫.執行，群組亦是，其他使用者只能讀和執行。
+ 4.有3個連結檔案
+ 5.檔案的容量為4096
+ 6.該檔案最後一次被修改/修訂的日期時間為 2017/02/16
+ 7.檔名為mail
+ 8.輸入 **chmod 777 script.sh** 或 **chmod u=rwx.g=rwx,o=rwx script.sh**
***
### 三.
+ 1.符號連結就是在建立一個獨立的檔案，而這個檔案會讓資料的讀取指向他 link 的那個檔案的檔名，而實體連結 只是在某個目錄下新增一筆檔名連結到某 inode 號碼的關連記錄而已。
+ 2.使用 **cd~** 到家目錄，輸入 **ln /etc/hosts hosts.real** 建立實體連結
+ 3.使用 **cd~** 到家目錄，輸入 **ln -s /etc/hosts hosts.symbo** 建立符號連結
***
### 四.
+ 1.新增一個磁碟
![image](https://imgur.com/a/KKhtXzR.png)
+ 2.用 **fdisk /dev/sdd** 分割出1G的磁碟
+ 3.再用 **mkfs.xfs /dev/sdd1** 建立一個容量為1GB的xfs檔案系統
![image](https://imgur.com/a/IVo9z6V.png)
+ 4.輸入 **mkdir /srv/maildir** 用 **mount /dev/sdd1 /srv/maildir**掛載
+ 5.修改 /etc/fstab，輸入 **/etc/fstab**
+ 6.用 **blkid** 看/dev/sdd1的 UUID及其他資料
+ 7.輸入 **vim /etc/fstab**輸入新增/dev/sdd1的資料
![image](https://imgur.com/K87NV6G.png)
+ 8.輸入 **df -T** 可以檢查有1GB的檔案系統正掛載到/srv/maildir
~[image](https://imgur.com/fXGd6Cp.png)
+ 9.先用 **groupoadd mailgroup** 建立mailgroup這個群組
+ 10.用 **useradd -G mailgroup mailuser** 新增mailuser使用者並加入mailgroup
+ 11.用 **id mailuser** 使用者有在mailgroup
![image](https://imgur.com/czYLvd1.png)
+ 12.輸入 **cat /etc/fstab | grep mailuser** 驗證有設定開機自動掛載
+ 13.用 **chgrp mailgroup /srv/maildur** 更改群組
+ 14.輸入 **ls -ali /srv/maildir** 查詢檔案的屬性
![image](https://imgur.com/cdJrXUi.png)
