#(1)
點選進入"全域工具"，建立新的網路卡，按"內容"將IPv4位址設定為"192.168.100.1"，並勾選"啟用"。
#(2)
新增一個新的虛擬機器-1，按"設定值"裡的"網路"，選擇"僅限主機介面卡"(名稱就是剛剛建立的網路卡)，安裝 yum install net-tools，接著輸入ip address add 192.168.100.100/24 broadcast + dev enp0s8。
#(3)
新增另一個虛擬機器-2，步驟同上，接著輸入ip address add 192.168.100.200/24 broadcast + dev enp0s8。
#(4)
虛擬機器-1:輸入vi /etc/sysconfig/network-scripts/ifcfg-*，接著改ONBOOT=yes，並新增ip位址IPADDR=192.168.100.100，打wq儲存離開。

虛擬機器-2:輸入vi /etc/sysconfig/network-scripts/ifcfg-*，接著改ONBOOT=yes，並新增ip位址IPADDR=192.168.100.200，打wq儲存離開。
#(5)
虛擬機器-1:輸入ping 192.168.100.200 確認網路是連通

虛擬機器-2:輸入ping 192.168.100.100 確認網路也是連通