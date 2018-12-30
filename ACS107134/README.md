* 的使用
">" 的使用
![]()
`的用法
空四個有另一種用法

### yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。

### Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。

### 請閱讀 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，

### 依照其作法，啟用epel repository，並安裝htop。

透過yum這個指令，user可以在網路上連接到預設的repo，去裡面尋找想要下載的軟體。然而預設的repo僅限於起初官方的軟體而已。
非官方的就不一定找得到，htop就是其中一個。想當然直接` yum `去找一定找不到 htop 這個軟體，因為htop在epel這個repo裡。

因此想要下載htop就要先下載epel這個repo，下載指令是
> yum -y install epel-release

![1]()

找到之後可以使用
> yum repolist < 來看看epel有沒有安裝成功
用 > yum search htop < 可以查看htop 是否在目前所擁有的repos裡
> yum info htop < 可以看看htop的資訊
最後用
> yum install htop > 
就可以安裝囉



sudo yum --disablerepo="*" --enablerepo="epel" list available