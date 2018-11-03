#關於連結檔案的建置行為
第一題:
(1)用 ls -ali /etc/hosts*可找出/etc/hosts檔案的inode號碼為8427944。
(2)這個inode只有一個檔名在使用。

第二題:
(1)用ln /etc/hosts /srv/hosts.hard建立實體連結，接著用 ll -i /etc/hosts /srv/hosts.hard可找出/srv/hosts.hard的inode號碼為8427944
(2)這個inode現在有兩個檔名在使用。
(3)用hard link會在目錄裡增加一筆與inode號碼連結的檔名。

第三題:
(1)用 ln -s /etc/hosts /srv/hosts.soft建立符號連結，接著用ls -ali /srv/hosts.soft可找出/srv/hosts.soft的inode號碼為12625702。
(2)這個inode只有一個檔名在使用。
(3)用soft link會直接建立一個新的獨立檔案，因此會有另一個對應的inode號碼。