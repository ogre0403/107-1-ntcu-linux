### 連結檔案建置
## 在 /etc/hosts 檔案，請找出
 - 16820904 -rw-r--r--. 1 root root 158 Jun 7 2013 /etc/hosts
1.該檔案的 inode 號碼為幾號？
  * 16820904
2.這個 inode 共有幾個檔名在使用？
  * 一個

## 建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出
 - 16820904 -rw-r--r--. 2 root root 158 Jun 7 2013 /srv/hosts.hard
1. /srv/hosts.hard的 inode 號碼為幾號？
  * 16820904
2.這個 inode 共有幾個檔名在使用？
  * 兩個
3.原因:新目錄的連結數為 2 ，而上層目錄的連結數則會增加 1，也就是/etc/hosts也會多新增一個連結數

## 建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出
 - 25245103 lrwxrwxrwx. 1 root root 10 Nov 3 19:48 /srv/hosts.soft -> /etc/hosts
1. /srv/hosts.soft的 inode 號碼為幾號？
  * 25245103
2. 這個 inode 共有幾個檔名在使用
  * 一個
3.原因:因為跟/etc/hosts的inode名稱不同，所以會重新建立新的inode