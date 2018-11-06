### HW5

# 1

<ol>輸入"ls -ali /etc/hosts"最前面的那段數字(紅線)就是inode。共有1個檔名在使用(黃線)
</ol>

![1](1.jpg)

<ol>輸入"ln /etc/hosts /srv/hosts.hard"建立實體連結，然後輸入"ls -ali /srv/hosts.hard"最前面的數字(紅線)就是inode。共有2個檔名在使用(黃線)。<\ol>

> 原因：原本的/etc/hosts和後來建立的實體連結/srv/hosts.hard都在使用，所以有兩個檔名(綠線)

![2](2.jpg)

<ol>輸入"ln -s /etc/hosts /srv/hosts.soft"建立符號連結，然後輸入"ls -ali /srv/hosts.soft"最前面的數字(紅線)就是inode。共有1個檔名在使用(黃線)。原因
<\ol>

> 原因：建立出來的符號連結是一個獨立的檔案，所以不會像實體連結一樣共用同一個inode。

![3](3.jpg)


