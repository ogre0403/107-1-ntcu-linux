##  <li>yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的CentOS 7 的設定檔的檔名為/etc/yum.repos.d/CentOS-Base.repo。</br>
##  Red Hat 提供了EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。</br></br>

##  請閱讀https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/後，依照其作法，啟用epel repo isitory，並安裝htop。</br></br>

###  因為htop在epel這個repo裡，所以要安裝htop就得先安裝epel。</br></br>

###  輸入`yum install epel-release`安裝epel repo。</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-9/ACS107127/screen/1-1.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-9/ACS107127/screen/1-2.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-9/ACS107127/screen/1-3.png)</br></br>

###  輸入`yum repolist`查看是否安裝成功。</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-9/ACS107127/screen/2-1.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-9/ACS107127/screen/2-2.png)</br></br>

###  輸入`yum search htop`查看htop是否在目前所擁有的repo裡。</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-9/ACS107127/screen/3.png)</br></br>


###  輸入`yum info htop`看htop的資訊。</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-9/ACS107127/screen/4.png)</br></br>


###  最後輸入`yum install htop`安裝。。</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-9/ACS107127/screen/5-1.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-9/ACS107127/screen/5-2.png)</br>