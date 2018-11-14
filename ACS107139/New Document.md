#1.1
uname -r找到3.13<br >
ver = my kernel version is 3.13<br >
echo ${ver} 得 my kernel version is 3.13
#1.2
echo ${PATH}顯示PATH，得/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/dmtsai/.local/bin:/home/dmtsai/bin<br >
用途:透過PATH變數裡面的內容所記錄的路徑順序來搜尋指令
#2.1
使用者可讀可寫可執行，群組可讀可寫可執行，其他人可讀可執行。
#2.2
數字法:chmod 777 script.sh<br > 
符號法:chmod a=rwx script.sh
#3.1
實體連結是在某個目錄下新增一筆檔名連結到某 inode 號碼的關連記錄<br >
符號連結是建立一個獨立的檔案，而這個檔案會讓資料的讀取指向他連結的那個檔案的檔名
#3.2
mkdir HOME/hosts.real<br >
ln hosts.real /etc/hosts
#3.3
mkdir HOME/hosts.real<br >
ln -s hosts.symbo /etc/hosts
#4.1
mkfs.xfs [-b 1g] /srv/maildir<br >
chmod 770<br >
groupadd mailgroup<br >
chgrp mailgroup /srv/maildir<br >
useradd -g mailgroup mailuser<br >
chsh -s /sbin/nologin; grep mailuser mailgroup
#4.2
df /srv/maildir顯示有1G
#4.3
mount | grep /srv/maildir驗證掛載
#4.4
ls -lid /srv/maildir確認
#4.5
id mailuser檢查
#4.6
grep -a mailuser /srv/maildir驗證