## HW5
#### 關於連結檔案的建置行為:

1. 在 /etc/hosts 檔案，請找出

    ![GITHUB]( https://imgur.com/ioSkh7A.jpg"git圖示")
+ 該檔案的 inode 號碼為幾號？
    + inode碼為4426572。 
+ 這個 inode 共有幾個檔名在使用？
    + 檔案連結數為1。

2. 建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出

    ![GITHUB]( https://imgur.com/e554Zkh.jpg"git圖示")
+ /srv/hosts.hard的 inode 號碼為幾號？
    + inode碼為4426572。
+ 這個 inode 共有幾個檔名在使用？
    + 檔案連結數為2。
    + 這是因為建立的連結為實體連結，所以會連結到同一個inode。
3. 建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出


    ![GITHUB]( https://imgur.com/0bN2JiX.jpg"git圖示")
+ /srv/hosts.soft的 inode 號碼為幾號？
    + inode碼為13006116。
+ 這個 inode 共有幾個檔名在使用 ?
    + 檔案連結數為1。
    + 這是因為建立的連結為符號連結，所以會建立一個新的inode。
