<strong>第一大題</strong>

<em>1.<em>
+ 首先執行VM Ware附帶的工具Virtual Network Editor
+ 之後如圖設置
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-8/ACS107103/conf1.png)
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-8/ACS107103/conf2.png)

<em>2.<em>
+ 虛擬機器-1的部分
+ 首先添加一張新的網卡
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-8/ACS107103/kali.PNG)
+ 之後開機，進系統後先確認網卡名稱
+ 然後執行ifconfig eth1 192.168.100.100來設定IP
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-8/ACS107103/kali_setip.png)

<em>3.<em>
+ 虛擬機器-2的部分
+ (步驟類似)
+ 首先添加一張新的網卡
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-8/ACS107103/centos.PNG)
+ 之後開機，進系統後先確認網卡名稱
+ 然後執行ifconfig ens37 192.168.100.200來設定IP
![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-8/ACS107103/centos_setip.png)

<em>4.<em>
+ 在虛擬機器-2上
+ 執行vi /etc/sysconfig/network-scripts/ifcfg-ens37創建並修改其文件內容
+ 記得加上IPADDR=192.168.100.200
+ 還有UUID的部分需正確設定
+ (這部分可用nmcli con show查看)
+ ![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-8/ACS107103/editcfg.png)

<em>5.<em>
+ 在虛擬機器-1上執行ping 192.168.100.200
+ ![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-8/ACS107103/ping1.png)
+ 在虛擬機器-2上執行ping 192.168.100.100
+ ![image](https://github.com/j6s94e04/107-1-ntcu-linux/blob/HW-8/ACS107103/ping2.png)
+ 成功互通!!