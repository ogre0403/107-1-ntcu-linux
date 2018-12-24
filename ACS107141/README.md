# HW8

## 在VirtalBox內建立一個新的Host-only 網路卡，網段為```192.168.100.1/24```

- 點擊「全域工具」&gt;「主機網路管理員」
![](https://i.imgur.com/sQgC2dq.png)

- 點擊「建立」&gt;「內容」
- 將IPv4位址改成`192.168.100.1`，套用後啟用
![](https://i.imgur.com/wdgBZX6.png)
***

## <p>建立虛擬機器-1，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-1的網路為`192.168.100.100/24`</p><p>建立虛擬機器-2，並啟用host-only網路卡，透過ifconfig 或 ip指令，設定虛擬機器-2的網路為`192.168.100.200/24`</p>

- 建立名為`CentOS TEST-1`和`CentOS TEST-2`的虛擬機器，完成後以root登入
- 輸入`yum install net-tools`
- 分別輸入以下指令修改IP<p>`ifconfig enp0s8 192.168.100.100/24`</p><p>`ifconfig enp0s8 192.168.100.200/24`</p>
![](https://i.imgur.com/hFCv8pM.png)

- 輸入`ifconfig enp0s8`檢查是否修改成功
![](https://i.imgur.com/VHNVVCY.png)
***

## 將二台虛擬機器的網路設定存至`/etc/sysconfig/network-scripts/`下相對應的`ifcfg-*`檔案，重新啟動虛擬機器，確認網路IP設定無誤

- 輸入`vi /etc/sysconfig/network-scripts/ifcfg-enp0s8`
    > 輸入a、i、o開啟編輯
- 將`ONBOOT=no`改成`ONBOOT=yes`<p>將`dhcp`改成`static`</p>
- CentOS TEST-1 輸入 `IPADDR=192.168.100.100`<p>CentOS TEST-2 輸入 `IPADDR=192.168.100.200`</p>
![](https://i.imgur.com/IjbGyTQ.png)
    > 按下`ESC`並輸入:wq儲存
***

## 從虛擬機器-1 ping 虛擬機器-2確認網路是連通，並從虛擬機器-2 ping 虛擬機器-1，確認網路也是連通。

- 重啟兩台虛擬機
- CentOS TEST-1輸入`ping 192.168.100.200`<p>CentOS TEST-2輸入`ping 192.168.100.100`</p>
![](https://i.imgur.com/qEQYUnP.png)
![](https://i.imgur.com/3S0pD9U.png)

    # 確認連通!



