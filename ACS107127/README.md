##  <li>在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24</br>
####  點選全域工具的主機網路管理員，並選擇建立(c)。</br>
####  建立一個新的Host-only 網路卡。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-8/ACS107127/screen/1.png)</br>
##  <li>建立虛擬機器-1，並啟用host-only網路卡。</br>
##  <li>建立虛擬機器-2，並啟用host-only網路卡。</br>
####  點選設定值內的網路，選擇"〔僅限主機〕介面卡"將剛新建立的網卡加入並啟用。</br>

![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-8/ACS107127/screen/2.png)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-8/ACS107127/screen/4.png)</br></br>

##  <li>透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24</br>
##  <li>透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24</br></br>

####  輸入" ip address add (ip) broadcast +  dev [裝置名] "，新增網路ip。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-8/ACS107127/screen/3.png)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-8/ACS107127/screen/5.png)</br></br>


##  <li>將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。</br></br>

####  輸入" vi /etc/sysconfig/network-scripts/ifcfg-* "，並在內容新增" IPADDR=(ip) "，完成後儲存修改內容並且重新啟動。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-8/ACS107127/screen/6.png)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-8/ACS107127/screen/7.png)</br></br>

##  <li>從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。</br></br>

####  輸入" ping 192.168.100.XXX "，來確認網路使否有連通。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-8/ACS107127/screen/8.png)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/HW-8/ACS107127/screen/9.png)</br>