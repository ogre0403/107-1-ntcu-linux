****關於連結檔案的建置行為
1.在/etc/hosts檔案，請找出
#該檔案的 inode 號碼為幾號？
--ls -ali /etc/hosts
→16809512 -rw-r--r-- 1 root root 158 Jun 7 2013 /etc/hosts
#這個 inode 共有幾個檔名在使用？
從權限後面知道有1個檔名在使用

****建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出
#/srv/hosts.hard的 inode 號碼為幾號？
--ln /etc/hosts /srv/hosts.hard
--cd /srv
--ls
→hosts.hard
--ls -ali hosts.hard
→16809512 -rw-r--r-- 2 root root 158 Jun 7 2013 hosts.hard
--ls -ld hosts.hard
目錄本身跟其打案對應到同個inode號碼所以有2個名稱在使用
****建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出
#/srv/hosts.soft的 inode 號碼為幾號？
--ln -s /etc/hosts /srv/hosts.soft
--ls -ali /srv/host.soft
→16809512 -rw-r--r-- 3 root root 158 Jun 7 2013 /srv/host.soft
因為新建立檔案所以讀取時直接讀取資料，inode的號碼只有一個檔案在使用