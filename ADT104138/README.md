# HW8
## ADT104138 羅苡倫
*****
## 一、請依說明完成下列操作讓虛擬機器彼此間能夠透過網路相互溝通：
*	在VirtalBox內建立一個新的Host-only 網路卡，網段為192.168.100.1/24</br>

打開程式，在右邊全域工具點擊進入，並且案新增一個網路，把ip改成192.168.100.1即可。</br>
![新增](https://i.imgur.com/BJR0aez.jpg)</br>
![新增](https://i.imgur.com/IJ9pQd8.jpg)</br>

*	建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為192.168.100.100/24</br>
*	建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為192.168.100.200/24</br>

簡單新增兩個虛擬機器，並把網路設成僅限主機即可。</br>
![新增](https://i.imgur.com/oFzpgqn.jpg)</br>

然後分別使用ip address add 192.168.100.100/24(第二台改成200/24) broadcast + dev enp0s3 指令即可。
![新增](https://i.imgur.com/79NH8gJ.jpg)</br>
![新增](https://i.imgur.com/DDwk8JE.jpg)</br>

*	將二台虛擬機器的網路設定存至/etc/sysconfig/network-scripts/下相對應的ifcfg-*檔案，重新啟動虛擬機器，確認網路ip設定無誤。</br>
使用vi 指令編輯，各自輸入剛剛設定的ip即可。</br>

![新增](https://i.imgur.com/RBLw9Gm.jpg)</br>
![新增](https://i.imgur.com/eDahfph.jpg)</br>
![新增](https://i.imgur.com/LYFI83h.jpg)</br>

*	從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。</br>

各自輸入 ping指令 ，可以用-c  限制次數，發現可以互相連通即成功。
![新增](https://i.imgur.com/e2cs7PA.jpg)</br>


# 參考資料：[點擊這裡](http://linux.vbird.org/linux_server/0140networkcommand.php#ip_cmd "參考資料")
# 感謝觀看 The End
