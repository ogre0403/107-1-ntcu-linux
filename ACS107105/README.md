# (HomeWork-8)

### 建立一個新的Host-only 網路卡
![GITHUB](https://imgur.com/NZ2VoRB.jpg "git圖示")

### 使用*ifconfig*或*ip*指令，將ACS107105的網路設定為192.168.100.100/24
+ *ip address add 198.168.100.100/24 broadcast + dev enp0s8*

![GITHUB](https://imgur.com/zmNDbex.jpg "git圖示")

### 同理，將ACS107105(2)的網路設定為192.168.100.200/24

![GITHUB](https://imgur.com/LWX0xyd.jpg "git圖示")

### 接著把2台虛擬機器的網路相關設定
### 儲存至/etc/sysconfig/network-scripts/下的相對檔案並使用vi修改


![GITHUB](https://imgur.com/MtQj6kq.jpg "git圖示")

### 從ACS107105 ping ACS107105(2)
### 確認網路為連通
### 並從ACS107105(2) ping ACS107105
### 確認網路也是連通

![GITHUB](https://imgur.com/wDKQF2B.jpg "git圖示")





  