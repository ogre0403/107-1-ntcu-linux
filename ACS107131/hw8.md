## 請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通：    
    
## *在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24    
    
#### 點主機網路管理員，建立新的網路卡，網段為192.168.100.1/24    
![1](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-8/ACS107131/1.PNG?raw=true)    
     
## *建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24       
    
#### 建立虛擬機器1     
#### ip address add 192.168.100.100/24 broadcast + dev enp0s3     
#### ip address show enp0s3 檢查    
![2](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-8/ACS107131/2.PNG?raw=true)    
![4](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-8/ACS107131/4.PNG?raw=true)    
## *建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24   
   
#### 建立虛擬機器2    
#### ip address add 192.168.100.200/24 broadcast + dev enp0s3     
#### ip address show enp0s3 檢查    
![3](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-8/ACS107131/3.PNG?raw=true)   
![5](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-8/ACS107131/5.PNG?raw=true)    
## *將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。     
       
#### vi /etc/sysconfig/network-scripts/ifcfg-enp0s3   
![6](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-8/ACS107131/6.PNG?raw=true)   
![7](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-8/ACS107131/7.PNG?raw=true)   
#### i 更改內容    
#### 將 onboot 改成 yes    
#### :w 儲存     
#### :q 離開    
   
## *從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。
     
#### 虛擬機器1 ping 192.168.100.100    
#### 虛擬機器2 ping 192.168.100.200    
#### 兩個虛擬機器要同時在開啟狀態     
![8](https://github.com/edmundabc/107-1-ntcu-linux/blob/HW-8/ACS107131/8.PNG?raw=true)     