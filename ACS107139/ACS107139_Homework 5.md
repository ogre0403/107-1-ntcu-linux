#1
ls -ali /etc/hosts找出inode為4210056<br >
1個
![](https://ppt.cc/fBEzXx@.png)
#2
ln /etc/hosts /srvhosts.hard<br >
ll /etc/hosts /srvhosts.hard<br >
找出inode為4210056<br >
2個檔名<br >
多出來的一筆為我們剛剛加上去的/srvhosts.hard
![](https://ppt.cc/fI260x@.png)
#3
ln /etc/hosts /srv/hosts.soft<br >
ls -ali /etc/hosts /srvhosts.hard<br >
找出inode為13031723<br >
1個檔名<br >
建立的檔案與先前的不同，故inode不同。且soft link為獨立文件，故只有一個檔名
![](https://ppt.cc/fNqogx@.png)
