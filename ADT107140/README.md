#閱讀 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/

#yum install epel-release
![](./1.PNG)

#yum repolist 
![](./2.PNG)

#列出所有安裝包    yum --disablerepo="*" --enablerepo="epel" list available
![](./3.PNG)  ![](./4.PNG)

#搜尋安裝包   yum search htop
![](./5.PNG)

#yum info htop
![](./6.PNG)

#安裝   yum install htop
![](./7.PNG)  ![](./8.PNG)
