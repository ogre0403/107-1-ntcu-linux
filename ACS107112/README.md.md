### 第一題
+ 用 ls -ali  查看/etc/hosts檔案
+ 可以發現inode為16820904
+ 目前有一個檔名共用此碼![](https://i.imgur.com/Uxrxp0b.jpg)
### 第二題
+ 透過 Root 建立實體連結
+ 經過 ls -ali 查看
+ 可以發現inode碼仍然為16820904
+ 這次有兩個檔名共用此碼
![](https://i.imgur.com/KrR8O23.jpg)
### 第三題
- 使用 ls -s 指令
- 建立符號連結(/etc/hosts至/srv/hosts.soft)
- 可以發現inode碼為25226989
- 目前有一個檔名共用此碼
![](https://i.imgur.com/H2D3RK6.jpg)




