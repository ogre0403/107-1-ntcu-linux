1.
(1).
ver="my kernel version is 3.10.0-862.e17.x86_64"
echo $ver
echo ${ver}

(2).
PATH=/myhome/bin:$PATH
當我們在執行一個指令時，系統會依照PATH的設定去每個PATH定義的路徑下搜尋檔案，先搜尋到的先執行，如果該指令無法執行在這個路徑無法執行，代表該路徑的環境變數沒有該令。

2.
(1).
這是一個名為mail的資料夾，root 的權限可讀可寫可執行，group的權限可讀可寫可執行，而其他人的權限可讀可執行不可寫，這個檔案的連結數為2，root 是這個檔案的擁有者，這個檔案所屬於mail這個群組，個檔案大小為4096，最後一次被修給的時間為2017/2/16。
(2).
如果以數字呈現:
可以使用(chmod XXX script.sh) 第一個x為root的權限，第二個x為該檔案所屬群組的權限，第3個x為其他人的權限，如果要讓其他人可寫可執行將x改為7，可讀可執行不可寫改為5，可寫可執行不可讀改為3，只可執行改為1。
如果以符號呈現:
可以使用 (chmod u=rwx,g=rwx,o= 檔名) 前面代表指定對象(o代表其他人，r代表root，g代表group，a代表全部)，後面表示指定權限(x代表執行，r代表讀，w代表寫，沒寫代表什麼不行做)。
3.(1).
實體連結(hard link):
實體連結的每個檔案會占用一個inode，檔案內容由inode的紀錄來指向。
想要讀取該檔案，必須要經過目錄紀錄的檔名來指向正確的inode才可執行。
多個檔名可以對應1個inode。
使用hard link設定連結檔時，磁碟與inode，的數目不會改變。
將任何一個檔名刪除，inode和block仍然存在。
不論用哪個檔名編輯，最終都會寫入相同的inode和block。

符號連結(soft link):
soft link是建立一個獨立的檔案，他會指向目的檔案，當資料讀取時他會指向所link的檔案。
soft link為獨立的新檔案，會占用inode和block。
當目的檔案被刪除，link會變成死link，無法再開啟該檔案。
(2).
ll -i /etc/hosts
ln /etc/hosts .
ll -i/etc/hosts hosts.real
(3).
ll -s /erc/hosts hosts.symbo
ll -i /etc/hosts /root/hosts.symbo
4.
(1).
mount /dev/vda1 /sev/maildir
vim /etc/fstab
mount -a
swapon -a
df -T /dev/sda2
swapon -s
(2).

(3).
cd /srv
mkdir maildir
ll
chgrp mailgroup
chmod o= maildir
![](https://i.imgur.com/uCDgybl.png)

(4).
useradd mailuser
id mailuser
usermod -a -G mialgroup mailuser
![](https://i.imgur.com/AFV909b.png)
(5).