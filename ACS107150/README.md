### 1.請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通：

#### 在VirtalBox內建立一個新的Host-only 網路卡，網段為`192.168.100.1/24`

- 在設定中的網路介面卡2新增僅限主機的介面卡

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-8/ACS107150/1.PNG?raw=true)

- 在喜好設定中的網路IPv4位址設定為192.168.100.1 網路遮罩設定為255.255.255.0

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-8/ACS107150/2.PNG?raw=true)

#### 建立虛擬機器-1，並啟用host-only網路卡，透過`ifconfig` 或 `ip`指令，設定虛擬機器-1的網路為`192.168.100.100/24`

- 輸入ip address add 192.168.100.100/24 broadcast + dev enp0s3

- 輸入ip address show確認

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-8/ACS107150/3.PNG?raw=true)

#### 建立虛擬機器-2，並啟用host-only網路卡，透過`ifconfig` 或 `ip`指令，設定虛擬機器-2的網路為`192.168.100.200/24`

- 輸入ip address add 192.168.100.200/24 broadcast + dev enp0s3

- 輸入ip address show確認

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-8/ACS107150/4.PNG?raw=true)

#### 將二台虛擬機器的網路設定存至`/etc/sysconfig/network-scripts/`下相對應的`ifcfg-*`檔案，重新啟動虛擬機器，確認網路ip設定無誤。

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-8/ACS107150/5.PNG?raw=true)

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-8/ACS107150/6.PNG?raw=true)

#### 從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-8/ACS107150/7.PNG?raw=true)

> ![GITHUB](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-8/ACS107150/8.PNG?raw=true)