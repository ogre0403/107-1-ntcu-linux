## yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的CentOS 7 的設定檔的檔名為/etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。</br>
### <li>請閱讀https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/後，依照其作法，啟用epel repo isitory，並安裝htop</br></br>
#### 要安裝htop，就得先安裝eqel這個repoisitory<br>
#### 輸入`yum install epel-release`安裝epel。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-9/ACS107135/photo/1.PNG)<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-9/ACS107135/photo/2.PNG)<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-9/ACS107135/photo/3.PNG)</br></br>
#### 輸入`yum search htop`確認htop是否有在目前所擁有的儲存庫裡面。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-9/ACS107135/photo/4.PNG)</br></br>

#### 輸入`yum install htop`安裝<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-9/ACS107135/photo/5.PNG)<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-9/ACS107135/photo/6.PNG)<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-9/ACS107135/photo/7.PNG)</br></br>
#### 安裝成功~