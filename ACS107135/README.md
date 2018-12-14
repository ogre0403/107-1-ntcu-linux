### 請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通：<br>

#### ˙在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/1.PNG)<br>
#### ˙建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig或ip指令，設定虛擬機器-1的網路為192.168.100.100/24<br>
##### 虛擬機器-1:<br>
##### ip address add 198.168.100.100/24 broadcast + dev enp0s8 (需先切換為root)<br>
##### ip address show enp0s8 查看
<center class="half">
    <img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/1.52.PNG"/><img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/2.PNG">
</center>

#### ˙建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig或ip指令，設定虛擬機器-2的網路為192.168.100.200/24<br>
##### 虛擬機器-2:<br>
##### ip address add 198.168.100.200/24 broadcast + dev enp0s8 (需先切換為root)<br>
##### ip address show enp0s8 查看<br>
<center class="half">
    <img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/1.5.PNG"><img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/3.PNG">
</center>

#### ˙將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。<br>
##### vi /etc/sysconfig/network-scripts/ifcfg-enp0s8<br>
<center class="half">
    <img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/4.PNG"><img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/5.PNG">
</center><br>
虛擬機器-1(上)/虛擬機器-2(下)<br><br>
<center class="half">
    <img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/6.PNG"><img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/7.PNG">
</center>
#### ˙從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。<br>
##### ping 198.168.100.xx 確認無誤<br>
虛擬機器-1(上)/虛擬機器-2(下)<br>
<center class="half">
    <img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/8.PNG"><img src="https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-8/ACS107135/photo/9.PNG">
</center>
