#關於連結檔案的建置行為:

## 1.在 /etc/hosts 檔案，請找出

## (1)該檔案的 inode 號碼為幾號？
## 尋找inode(輸入 ls -ail /etc/hosts)→最前面的一列數字就是這個檔案的inode→為16796072
## (2)這個 inode 共有幾個檔名在使用？
## 可由權限後面個數字看出只有一個檔名在使用
## 2.建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出
## (1)/srv/hosts.hard的 inode 號碼為幾號？
## 建立實體連結(輸入 ln /etc/hosts /srv/hosts.hard)→進入 /srv(輸入 cd /srv)→查看hosts.hard的inode(輸入 ls -ail)尋找檔名為hosts.hard→inode為1678194
## (2)這個 inode 共有幾個檔名在使用？
## 可由權限後面個數字看出有兩個檔名在使用
## (3)說明原因
## 因為他們其實是同一個檔案
##  3.建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出
## (1)/srv/hosts.soft的 inode 號碼為幾號？
## 建立符號連結(輸入 ln -s /etc/hosts /srv/hosts.soft)→查看hosts.soft的inode(輸入 ls -ail /srv/hosts.soft)→inode為50777406
## (2)這個 inode 共有幾個檔名在使用？
## 可由權限後面個數字看出只有一個檔名在使用
## (3)說明原因
## 因為這是一個獨立的檔案