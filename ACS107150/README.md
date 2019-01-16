### 1.yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。

#### 請閱讀<https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/>後，依照其作法，啟用EPEL repository，並安裝`htop`

- yum install epel-release

> ![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-9/ACS107150/1.PNG?raw=true)

- yum install epel-release-latest-7.noarch.rpm

> ![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-9/ACS107150/2.PNG?raw=true)

- yum repolist

> ![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-9/ACS107150/3.PNG?raw=true)

- yum --disablerepo="*" --enablerepo="epel" list availabl

> ![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-9/ACS107150/4.PNG?raw=true)

- yum install htop

> ![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-9/ACS107150/5.PNG?raw=true)

