用ls -ali 查看/etc/hosts檔案。
可看到inode為4216200
有一檔名共用

![1](https://user-images.githubusercontent.com/43788227/51440899-bed2b500-1d06-11e9-80b7-b1c3042352ca.PNG)

透過使用者(sammy)使用 ln 指令。
建立連結使原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard。
可發現不行。

![2](https://user-images.githubusercontent.com/43788227/51440960-5506db00-1d07-11e9-8cab-36516cd22891.PNG)

透過 Root 再次建立實體連結。
經過 ls -ali 查看。
可以發現inode碼仍然為4216200但是這次有兩個檔名共用此碼

![3](https://user-images.githubusercontent.com/43788227/51440985-c777bb00-1d07-11e9-9f34-a6400820f602.PNG)

使用 ls -s 指令。
建立符號連結(/etc/hosts至/srv/hosts.soft)。
可以發現inode碼為13031735且目前有一個檔名共用此碼。

![4](https://user-images.githubusercontent.com/43788227/51441021-3b19c800-1d08-11e9-997c-4d1683d25ee8.PNG)
