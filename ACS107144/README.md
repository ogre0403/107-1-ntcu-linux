## yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。

### 請閱讀 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，依照其作法，啟用epel repoisitory，並安裝htop

* 安裝 epel repo
 * 輸入`yum install epel-release`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-9/ACS107144/9-01.png)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-9/ACS107144/9-02.png)

* 查看是否安裝成功
 * 輸入`yum repolist` 
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-9/ACS107144/9-03.png)

* 查看 htop 是否存在於目前所擁有的 repos 裡
 * 輸入`yum search htop`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-9/ACS107144/9-04.png)

* 查看 htop 的資訊
 * 輸入`yum info htop`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-9/ACS107144/9-05.png)

* 安裝 htop
 * 輸入`yum install htop`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-9/ACS107144/9-06.png)

