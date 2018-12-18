1.開啟virtual box，再點選右上方的全域工具，點進主機網路管理員，
在按左上角的建立，建立新的網路卡之後，按右鍵的內容，將網段更改為192.168.100.1/24。
2.點選左上角的新增，輸入機器名稱-1，然後再點選設定值裡面的網路，選擇啟用
Host-only網路卡，安裝成功之後，輸入install net-tools來下載ifconfig，下載好之後，
輸入ifconfig enp0s8 192.168.100.100，再輸入ifconfig。
3.再依上述的方式建立另外一個虛擬機器，名稱為-2，
一樣在設定值的地方啟用Host-only網路卡，輸入install net-tools來下載ifconfig，
輸入ifconfig en0s8 192.168.100.200，再輸入ifconfig。
4.打開-1的虛擬機器，輸入vi /etc/sysconfig/network-scripts/ifcfg-*，
然後在ONBOOT=no的地方，把no改成yes，再新增ip位址IPADDR=192.168.100.100。
打開-2的虛擬機器，輸入vi /etc/sysconfig/network-scripts/ifcfg-*，
然後在ONBOOT=no的地方，把no改成yes，再新增ip位址IPADDR=192.168.100.200。
5.打開-1的虛擬機器，輸入ping 192.168.100.200，然後在-2的虛擬機器輸入ping 192.168.100.100，
確認網路是否互通。