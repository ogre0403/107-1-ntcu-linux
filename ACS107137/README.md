## 請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通：
### 在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24

### 建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24

```
ip address add 198.168.100.100/24 broadcast + dev enp0s8 (切換為root)
ip address show enp0s8 (查看)
```


### 建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24

```
ip address add 198.168.100.200/24 broadcast + dev enp0s8 (切換為root)
ip address show enp0s8 (查看)
```


### 將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤

```
vi /etc/sysconfig/network-scripts/ifcfg-enp0s8 (設定兩個虛擬機器的網路檔案)
reboot (重啟機器)
ip address show enp0s8 (查看)
```




### 從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通

```
虛擬機器1 ping 192.168.100.200
虛擬機器2 ping 192.168.100.100
```


