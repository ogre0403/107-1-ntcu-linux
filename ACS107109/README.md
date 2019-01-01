# HW9
-----------------------------------------
## yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。
### 請閱讀https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，依照其作法，啟用epel repoisitory，並安裝` htop `。

* 安裝epel:` yum install epel-release `。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-9/ACS107109/img/01.PNG)


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-9/ACS107109/img/02.PNG)


* 檢查epel有無成功安裝:` sudo yum repolist `。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-9/ACS107109/img/03.png)


* 檢查htop package有無存在epel repo:` yum search htop `。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-9/ACS107109/img/04.png)


* 查看更多htop package的資訊:` yum info htop `。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-9/ACS107109/img/05.PNG)


* 安裝htop:` yum install htop `。


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-9/ACS107109/img/06.PNG)


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-9/ACS107109/img/07.PNG)
