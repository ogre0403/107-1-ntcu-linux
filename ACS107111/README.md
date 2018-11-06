![GITHUB](https://imgur.com/Vr6TbQA.jpg"git圖示")

+ 使用ll -i hosts可知其inode為2132776，一個檔名在使用

![GITHUB](https://imgur.com/kLcrQcD.jpg"git圖示")

+ 建立hard link於/etc/hosts叫hosts.hard

![GITHUB](https://imgur.com/lKUwEhN.jpg"git圖示")

+ 在/srv/使用ll -i hosts.hard可知其inode和hosts一樣，但變成兩個檔名在使用
+ 因為harc link為inode不變，增加檔名使用數

![GITHUB](https://imgur.com/oVzYSNW.jpg"git圖示")

+ 建立soft link於//etc/hosts叫hosts.sort，用ll -i hosts.soft，可知其inode為2121577，與hosts不同且只有一個檔名在使用
+ 因為soft link會改變inode而不會增加檔名使用數



