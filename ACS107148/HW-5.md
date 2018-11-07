# HW-5
* 第一步：輸入"ll -i /etc/hosts"，即可顯示出下圖，紅線部分為inode，黃線部分表示此inode為1個檔名使用。

![](https://i.imgur.com/F1qBbnr.png)

* 第二步：輸入"ln /etc/hosts /srv/hosts.hard"，建立實體連結，再來輸入"ls -ail /etc/hosts /srv/hosts.hard"即可顯示檔案權限，最前面紅線為inode，黃線則表示有2個檔名在使用。
* 原因：原本的/etc/hosts和後來建立的實體連結/srv/hosts.hard都在使用，所以有兩個檔名(綠線)

![](https://i.imgur.com/5H9P7xP.png)

* 第三步：輸入"in -s /etc/hosts /srv/hosts.soft"建立符號連結，然後輸入"ll -ail /srv/hosts,soft"即會顯示出下圖所示，紅線部分表示inode，黃線部分表示共有1個檔命使用。
* 原因：建立出來的符號連結是一個獨立的檔案，所以不會像實體連結一樣共用同一個inode。

![](https://i.imgur.com/IJ1fLXp.png)
