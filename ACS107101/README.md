### HW5
 # 1
 +輸入"ls -ali /etc/hosts"最前面的那段數字就是inode。共有1個檔名在使用
 ![GITHUB](https://imgur.com/GhlrYDQ.jpg "git圖示")
 # 2
 +因為沒有切換成root,所以沒有權限hard link
 ![GITHUB](https://imgur.com/zlE1jye.jpg "git圖示")
 +輸入"ln /etc/hosts /srv/hosts.hard"建立實體連結，然後輸入"ls -ali /srv/hosts.hard"最前面的數字就是inode。共有2個檔名在使用。
 ![GITHUB](https://imgur.com/KlHQsvg.jpg "git圖示")
 ![GITHUB](https://imgur.com/S3GFrxW.jpg "git圖示")
 # 3
 +輸入"ln -s /etc/hosts /srv/hosts.soft"建立符號連結，然後輸入"ls -ali /srv/hosts.soft"最前面的數字就是inode。共有1個檔名在使用。
 ![GITHUB](https://imgur.com/idT4imY.jpg "git圖示")
 ![GITHUB](https://imgur.com/9fxBT5n.jpg "git圖示")

 。

