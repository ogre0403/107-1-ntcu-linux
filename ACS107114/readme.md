# 第一題

## 1. 在 /etc/hosts 檔案，請找出該檔案的 inode 號碼為幾號？ inode 共有幾個檔名在使用？
* 以**ls -ali /etc/hosts**顯示出/etc/hosts該檔案的詳細資料 
* 開頭的7個號碼即為inode號碼
* 權限後顯示之數字即為inode共有幾個檔名在使用
* inode 為 4220520
* 共有1個檔名在使用
![](https://i.imgur.com/dvPogFl.png)

## 2. 建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出/srv/hosts.hard的 inode 號碼為幾號？  這個 inode 共有幾個檔名在使用？ 並且說明原因。
* 先以**ln**建立連結，輸入**ln /etc/hosts /srv/hosts.hard**建立新連結
* 再以**cd /srv**進入該資料夾中，以**ls -ali hosts.hard**顯示該檔案詳細資料
* inode 為 4220520
* 共有2個檔名在使用
![](https://i.imgur.com/q9T0sed.png)
* **說明原因:** 因原始檔案經**ln**建立實體連結後，和原始文件共享相同inode所造成

## 3. 建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出/srv/hosts.soft的 inode 號碼為幾號？  這個 inode 共有幾個檔名在使用? 並且說明原因。
* 以**ln -s /etc/hosts /srv/hosts.soft** 先建立符號連結
* 再輸入**ls -ali hosts.hard** 顯示出該檔案資料
* inode 為 6291536
* 共有1個檔名在使用
![](https://i.imgur.com/LjwSvld.png)
* **說明原因:**使用符號連結的話 建立的會是獨立連結之檔案 因此inode只會有1個(只有自己在使用)