### 在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24
* 選擇右上角的全域工具進行設定
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-8/ACS107144/8-1-1.png)
1. 選取建立，建立新的網路卡
2. 選取內容，編輯網路卡  
3. 在IPv4位址欄位輸入`192.168.100.1`
4. 套用
5. 勾選啟用網路卡
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-8/ACS107144/8-1-2.png)

### 建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24
* 建立名為 ex-1 的虛擬機
* 建立完成後，以root登入
* 輸入`yum install net-tools`
> 安裝 ifconfig，之後需要用到
* 輸入`IP address add 192.168.100.100/24 broadcast + dev enp0s3`
> 設定網路
* 輸入`ip address show`
> 顯示結果

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-8/ACS107144/8-2-1.png)

### 建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24
* 建立名為 ex-2 的虛擬機
* 建立完成後，以root登入
* 輸入`yum install net-tools`
> 安裝 ifconfig，之後需要用到
* 輸入`IP address add 192.168.100.200/24 broadcast + dev enp0s3`
> 設定網路
* 輸入`ip address show`
> 顯示結果

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-8/ACS107144/8-3-1.png)

### 將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。
* 輸入`vi /etc/sysconfig/network-scripts/ifcfg-*`
* 編輯內容
> ex-1 輸入`IPADDR=192.168.100.100` 並儲存
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-8/ACS107144/8-4-1.png)
> ex-2 輸入`IPADDR=192.168.100.200` 並儲存
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-8/ACS107144/8-4-2.png)

### 從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。
* ex-1，輸入`ping 192.168.100.200`
* ex-2，輸入`ping 192.168.100.100`
* 同時執行
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-8/ACS107144/8-5-1.png)
