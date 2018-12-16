# HW8
-----------------------------------------
## 請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通：


### 在VirtalBox內建立一個新的Host-only 網路卡，網段為` 192.168.100.1/24 `
* 點選右上角的**權域工具**進入設定


![image](1)


* 建立及設定新的網路卡
  * **1**按下左上角的**建立**
   > VirtualBox Host-Only Ethernet Adapter #3

  * **2**點選內容
  * **3**設定IPv4位址為:` 192.168.100.1 `
   > 設定後按下**套用**

  *  此時上面呈現的IPv4位址遮罩為` 192.168.100.1/24 `，**記得把啟用打勾**!!


![image](2)


-----------------------------------------
### 建立虛擬機器-1，並啟用host-only網路卡，透過` ifconfig ` 或 ` ip `指令，設定虛擬機器-1的網路為` 192.168.100.100/24 `
* 建立虛擬機器**test1**
  > 建立方法:< https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-2/ACS107109/HW2.md >

* 開啟**設定值**至**網路**啟用剛剛新設定的host-only網路卡


![image](3)


* **由於是全新新增的虛擬機器，所以要開啟網路卡，並安裝ifconfig。**
  > 開啟網路卡:nmtui

  > 安裝ifconfig:` yum install net-tools `
  > > ifconfig:可以用來查詢、設定網路卡與 IP 網域等相關參數。

*  設定虛擬機器**test1**的網路為` 192.168.100.100/24 `
  > ` ip address add  192.168.156.100/24 broadcast + dev enp0s3 `


![image](4)



-----------------------------------------
### 建立虛擬機器-2，並啟用host-only網路卡，透過` ifconfig ` 或 ` ip `指令，設定虛擬機器-2的網路為` 192.168.100.200/24 `
* 建立虛擬機器**test2**
  > 建立方法:< https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-2/ACS107109/HW2.md >

* 開啟**設定值**至**網路**啟用剛剛新設定的host-only網路卡


![image](5)


* **由於是全新新增的虛擬機器，所以要開啟網路卡，並安裝ifconfig。**
  > 開啟網路卡:nmtui

  > 安裝ifconfig:` yum install net-tools `
  > > ifconfig:可以用來查詢、設定網路卡與 IP 網域等相關參數。

* 設定虛擬機器**test2**的網路為` 192.168.100.200/24 `
  > ` ip address add  192.168.156.200/24 broadcast + dev enp0s3 `


![image](6)


-----------------------------------------
### 將二台虛擬機器的網路設定存至` /etc/sysconfig/network-scripts/ `下相對應的` ifcfg-* `檔案，重新啟動虛擬機器，確認網路ip設定無誤。
* 輸入` vi /etc/sysconfig/network-scripts/ifcfg-* `
  > 將二台虛擬機器的網路設定存至` /etc/sysconfig/network-scripts/ `下相對應的` ifcfg-* `檔案

  * 虛擬機1:test1
![image](7)
    * ONBOOT要開啟唷!這樣開基的時候就會自動開啟了
      > ONBOOT=yes

    * 新增對應IP位址
      > IPADDR=192.168.100.100

    * 儲存離開


![image](8)


  * 虛擬機2:test2
![image](9)
    * ONBOOT要開啟唷!這樣開基的時候就會自動開啟了
      > ONBOOT=yes

    * 新增對應IP位址
      > IPADDR=192.168.100.200

    * 儲存離開


![image](10)


-----------------------------------------
### 從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。
* 虛擬機1:test1
  * ` ping 192.168.100.200 `
* 虛擬機2:test2
  * ` ping 192.168.100.100 `

![image](11)


* 同時執行，確認網路是互通的


![image](12)