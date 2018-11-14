### 期中考

## 第一大題
 1. 設定ver變數 
    *  `uname -r`
         `3.10.0-862.e17.x86_64`
    *  `3.xx=3.10.0-862.e17.x86_64`
    *  `ver="my kernel version is $3.xx"`
    *  `echo $ver`
    *    `my kernel version is 3.10.0-862.e17.x86_64`

 2. 顯示PATH環境變數的值
    
    ```
    /usr/local.sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin
    ```

   *  PATH的功能: 為環境變數，指定環境目錄，以執行可執行檔

=============================================================================

## 第二大題
 1. `drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/`
    *  檔案類型:目錄檔
    *  檔案權限:
         -  user: 可讀可修改可執行
         -  group: 可讀可修改可執行  ( 權限為s表示權限旗標到與群組相同，因此在此群組內的人皆可變更內容 )
         -  others: 可讀可執行，但不可修改
    *  檔案連結數:3 (inode數)
    *  檔案擁有者:root
    *  檔案群組:mail
    *  檔案容量:4096
    *  檔案日期:2月 16 2017
    *  檔名: mail/

 2. script.sh檔案的權限為`-rw-r--r--`
    * `chmod a+x script.sh`
    * `chmod 755 script.sh`

=============================================================================

## 第三大題
 1.實體連結:
    *  inode不變，和來源檔相同
    *  任黨名刪除，inode和block皆存在，直到連結數為0為止
    *  連結數改變: 當建立新的目錄時，連結數為2，而上層目錄為1
    *  `ln 來源檔 目的檔`
   符號連結:
    *  inode改變，建立獨立的檔案
    *  來源檔或目的檔刪除，即無法開啟檔案
    *  連結數檔案大小為路徑長度
    *  `ln -s 來源檔 目的檔`

 2. 建立實體連結  `hosts.real`
    *  `ln /etc/hosts ~hosts.real`
    *  `ll`
         `-rw-r--r--. 3 root root 158 Jun 7 2013 ~hosts.real`
    *  `ls -ali`
         `16820904 -rw-r--r--. 3 root root 158 Jun 7 2013 ~hosts.real`
    *  `ls -ali /etc/hosts`
         `16820904 -rw-r--r--. 3 root root 158 Jun 7 2013 /etc/hosts`

 3. 建立符號連結  `hosts.symbo`
    *  `ln -s /etc/hosts ~hosts.symbo`
    *  `ll`
         `lrwxrwxrwx. 1 root root 10 Nov 14 15:17 ~hosts.symbo -> /etc/hosts`
    *  `ls -ali`
         `25628245 lrwxrwxrwx. 1 root root 10 Nov 14 15:17 ~hosts.symbo -> /etc/hosts`

=============================================================================

## 第四大題
 1.  建立檔案系統
    *  `fdisk /dev/sdb`
         `command (m for help):n` 建立分割/dev/sdb1
         `Last sectors: +1GB`
         `command (m for help):p`
         `Device     Boot   Start     End        Block      Id    System`
         `/dev/sdb1         2048     1955839     976896     83     Linux`
         `command (m for help):w`
         `mkds.xfs /dev/sdb1`
  2.  建立新目錄
       * `mkdir /srv/maildir`
  3.  建立新帳號
       * `groupadd mailgroup`
       * `useradd -G mailgroup mailuser`
       * `chgrp mailgroup /srv/maildir`
       * `chmod o-rw /srv/maildir`
       * `ll /srv/maildir`
           `drwxr-x---. 2 root mailgroup 6 Nov 14 16:16 maildir`
  4.  掛載
       * `blkid`
           `UUID="c758211a-52d1-41a7-810d-7d362f0089e9",TYPE="xfs"`
       * `mount /dev/sdb1 /srv/maildir`
       * `cat /etc/fstab`
       * `vi /etc/fstab`
           新增UUID="c758211a-52d1-41a7-810d-7d362f0089e9" /srv/maildir xfs default 0 0`
       * `mount -a`
  5.  檢視
       * `df -T`
          `/dev/sdb1    xfs    973476   32944  940532  4%  /srv/maildir`
       * `/etc/passwd | grep /dev/sdb1`
           
       * `ls -al /srv/maildir`
           `drwxr-x---. 2 root mailgroup 6 Nov 14 16:16 maildir`
       * `id mailuser`
            `uid=101(mailuser) gid=1013(mailuser) groups=1013(mailuser),1012(mailgroup)`
       * `/etc/passwd | grep /srv/maildir`
           `/srv/maildir:/sbin/nologin`

(老師對不起，我的電腦不知為何不能截圖，所以我無法附圖)