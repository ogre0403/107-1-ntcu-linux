#第一題
##  1.關於連結檔案的建置行為:
##  在 /etc/hosts 檔案，請找出該檔案的 inode 號碼為幾號？
##  ![](https://i.imgur.com/2m5uLfQ.jpg)
##  這個 inode 共有幾個檔名在使用？
##  ![](https://i.imgur.com/vZ5exZT.jpg)
##  2.建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出
##  /srv/hosts.hard的 inode 號碼為幾號？
##  ![](https://i.imgur.com/AMIJUKQ.jpg)
##  這個 inode 共有幾個檔名在使用？
##  ![](https://i.imgur.com/HJVYuN5.jpg)
##  說明原因:hard link 在某個目錄下新增一筆檔名連結到某 inode 號碼的關連記錄
##  ![](https://i.imgur.com/Na5GJ8N.jpg)
##  3.建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出
##  /srv/hosts.soft的 inode 號碼為幾號？
##  ![](https://i.imgur.com/Z71rXDR.jpg)
##  這個 inode 共有幾個檔名在使用?
##  如上圖中只有一個
##  說明原因
##  跟hard link不一樣的是soft link是另外建立一個獨立的檔案，所以只有一個檔名在使用
##  ![](https://i.imgur.com/Aeygb2J.jpg)
