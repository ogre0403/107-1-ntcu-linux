## HW9

### 第一題

#### 1.yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。

###### 詳細閱讀https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，依照其作法，啟用epel repo isitory，並安裝htop
* 先使用`su` 升級權限到管理者 再使用`sudo yum install epel-release` 啟用**epel-release**

![](https://i.imgur.com/ojFbgMb.png)

![](https://i.imgur.com/hz6Ksu2.png)


* 接著使用`sudo yum repolist`

![](https://i.imgur.com/LXvyKQA.png)


* 再使用`sudo yum search htop` 搜尋出**htop**

![](https://i.imgur.com/W0ubQlD.png)

* 使用`sudo yum info htop` 即顯示出**htop**的詳細資料

![](https://i.imgur.com/GPEGV08.png)

* 最後輸入`sudo yum install htop` 即可安裝**htop**

![](https://i.imgur.com/TPxhElP.png)

![](https://i.imgur.com/AogQyTh.png)
