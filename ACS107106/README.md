#第一題
(1)uname -r看到3.xx為3.10，接著用echo $ver設定變數，用ver="my kernel version is 3.10，然後再用一次echo $ver就可以顯示出變數的值。

(2)用echo $PATH可顯示出/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin，其功用為讓系統透過 PATH 這個變數裡面的內容所記錄的路徑順序來搜尋指令。

#第二題
(1)mail/這個檔案的連結數為3，該檔案的擁有者為root(有rwx的權限)，所屬群組為mail(有rws的權限)，其他人則只有rx的權限，檔案大小為4096，最後一次修改的日期為2017/02/16

(2)數字法:用chmod 777 script.sh
   符號法:chmod u=rwx,g=rwx,o=rwx script.sh

#第三題

(1)實體連結與符號連結的差異:
使用實體連結，磁碟的空間與inode的數目都不會改變，只是在目錄裡加一筆inode與檔名的對應。
使用符號連結，就是在建立一個獨立的新的檔案，所以會佔用調inode與block。

(2)用touch hosts.real建立檔案，用ln ~/etc/hosts ~/hosts.real 在家目錄建立實體連結。

(3)用touch hosts.symbo建立檔案，用ln -s ~/etc/hosts ~/hosts.symbo在家目錄建立符號連結。

#第四題

(1)fdisk /dev/sdb建立1GB的檔案，用mkfs.xfs /dev/sdb1建立xfs檔案系統，用mount /dev/sdb1 /srv/maildir，用df -T /srv/maildir顯示有1GB的檔案系統正掛載到`/srv/maildir`。

(2)用cat /etc/fstab將所顯示的UUID那一行寫到vi /etc/fstab中，重新開機後就會自動掛載。

(3)用chgrp mailgroup /srv/maildir，用chmod 770 /srv/maildir，用ls -ld /srv/maildir。

(4)用groupadd mailgroup，用useradd -G mailgroup mailuser，用id mailuser可看到使用者有在`mailgroup`。

(5)用/etc/passwd | grep mailuser。