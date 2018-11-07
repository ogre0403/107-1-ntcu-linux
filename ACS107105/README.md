# (I)

![GITHUB](https://imgur.com/PV6rITZ.jpg "git圖示")
#
+ 使用 *ls -ali* 指令 查看/etc/hosts檔案。
+ 可以發現inode為16795976且目前有一個檔名共用此碼。

# (II)

![GITHUB](https://imgur.com/2i1Himf.jpg "git圖示")
#
+ 透過使用者(acs107105)使用 *ln* 指令。
+ 建立實體連結(/etc/hosts至/srv/hosts.hard)。
+ 可以發現使用者(acs107105)不具有權限。
+ 之後,透過 Root 再次建立實體連結。
+ 經過 *ls -ali* 查看。
+ 可以發現inode碼仍然為16795976但是這次有兩個檔名共用此碼。

# (III)

![GITHUB](https://imgur.com/hewHX98.jpg "git圖示")
# 
+ 使用 *ls -s* 指令。
+ 建立符號連結(/etc/hosts至/srv/hosts.soft)。
+ 可以發現inode碼為50776214且目前有一個檔名共用此碼。
