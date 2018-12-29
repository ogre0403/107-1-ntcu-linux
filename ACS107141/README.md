# HW9

## 請閱讀 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，依照其作法，啟用`epel repo isitory`，並安裝`htop`。
    yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名
    為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額
    外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在
    預設的設定檔內。

+ 輸入`yum install epel-release`安裝 <b>EPEL repo</b>
![](https://i.imgur.com/7uCNcoU.png)

+ 輸入`yum repolist`查看
![](https://i.imgur.com/WHe7FXU.png)

+ 輸入`yum --disablerepo="*" --enablerepo="epel" list available`列出名為`epel`的repo之所有可用安裝包

+ 輸入`yum search htop`搜尋`htop`安裝包
![](https://i.imgur.com/bI8kN4d.png)

+ 輸入`yum info htop`列出`htop`相關訊息
![](https://i.imgur.com/ZE1psap.png)

+ 輸入`yum install htop`安裝`htop`
![](https://i.imgur.com/fpMSnVh.png)

## <b>安裝成功！！</b>

