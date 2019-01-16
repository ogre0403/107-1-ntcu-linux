#yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。

##請閱讀 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，依照其作法，啟用epel repo?isitory，並安裝htop

*輸入yum install epel-release

>在Centos 7上安裝epel-release軟件包

![image](https://github.com/ACS107104/107-1-ntcu-linux/blob/HW-9/ACS107104/(0).PNG)

*輸入yum repolist

>安裝repolist查看epel repo

![image](https://github.com/ACS107104/107-1-ntcu-linux/blob/HW-9/ACS107104/(1).PNG)

*輸入yum  --disablerepo="*" --enablerepo="epel" list available

>在CentOS / RHEL / Fedora Linux上列出EPEL Repo下的所有可用軟件包

![image](https://github.com/ACS107104/107-1-ntcu-linux/blob/HW-9/ACS107104/(2).PNG)

*輸入yum search htop

>search it

![image](https://github.com/ACS107104/107-1-ntcu-linux/blob/HW-9/ACS107104/(3).PNG)

*輸入yum info htop

>get more info, if found 

![image](https://github.com/ACS107104/107-1-ntcu-linux/blob/HW-9/ACS107104/(4).PNG)

*輸入yum install htop

>install it

![image](https://github.com/ACS107104/107-1-ntcu-linux/blob/HW-9/ACS107104/(5).PNG)
