## HW8
### 第一題
#### 1. 在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24
* 建立一個新的網路卡
![](https://i.imgur.com/toErw0K.png)

#### 2. 建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24
* 使用`ip address add 198.168.100.100/24 broadcast + dev enp0s8` 更改IP
* 再使用`ip address show enp0s8` 檢查是否成功
![](https://i.imgur.com/so8gYjU.png)
 
 #### 3. 建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24
*  使用`ip address add 198.168.100.200/24 broadcast + dev enp0s8` 更改IP
*  再使用`ip address show enp0s8`檢查是否成功
![](https://i.imgur.com/6RYahGH.png)

#### 4. 將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。
*  使用`vi /etc/sysconfig/network-scripts/ifcfg-enp0s8`查看個個的IP
![](https://i.imgur.com/ZRuMhi2.jpg)
