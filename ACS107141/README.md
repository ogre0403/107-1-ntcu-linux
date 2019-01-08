# HW10

## 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 `netstat -alntp | grep ssh`確認是否啟動二個sshd服務。

    $ netstat -alntp | grep ssh
    tcp        0      0 0.0.0.0:22     0.0.0.0:*         LISTEN      1300/sshd
    tcp        0      0 0.0.0.0:2222   0.0.0.0:*         LISTEN      15275/sshd
    tcp6       0      0 :::22          :::*              LISTEN      1300/sshd
    tcp6       0      0 :::2222        :::*              LISTEN      15275/sshd
    
    Note 1: CentOS有使用SELinux ，故預設只允許 SSH 使用埠號 22，若要使用埠號 2222，使請用下列指示開啟並檢查

    sh
    $ semanage port -a -t ssh_port_t -p tcp 2222
    $ semanage port -l | grep ssh
    ssh_port_t tcp 2202, 22
 

    Note 2: CentOS預設的防火牆firewalld會禁止訪問埠號2222，若要透過2222埠連ssh，請先關閉firewalld
--- 
* 輸入<b>`systemctl stop firewalld`</b>關閉防火牆(先關以防萬一)
![](https://i.imgur.com/EPccK5A.png)


* 輸入<b>`systemctl status sshd.service`</b>檢查目前<b>`sshd.service`</b>狀態
![](https://i.imgur.com/t1WYGxh.png)


* 輸入<b>`cd /etc/ssh`</b>進入<b>`/etc/ssh`</b>裡
![](https://i.imgur.com/907w41P.png)


* 輸入<b>`cp sshd_config sshd2_config`</b>複製<b>`sshd_config`</b>至<b>`sshd2_config`</b>
![](https://i.imgur.com/8D8PEOl.png)


* 輸入<b>`vi sshd2_config`</b>進入編輯模式
![](https://i.imgur.com/WAoHSVU.png)
    > 按下a,i,o開始編輯


* 將<b>`#Port 22`</b>改成<b>`Port 2222`</b>
![](https://i.imgur.com/OjHaxEF.png)
    > 按下esc並輸入`:wq`儲存

* 輸入<b>`cd /etc/systemd/system`</b>切換至<b>`/etc/systemd/system`</b>
![](https://i.imgur.com/oZDNbn0.png)

* 輸入<b>`cp /usr/lib/systemd/system/sshd.service sshd2.service`</b>將<b>`sshd.service`</b>的內容複製到<b>`sshd2.service`</b>
![](https://i.imgur.com/KeyykQ9.png)

* 輸入<b>`vi sshd2.service`</b>進入編輯模式
![](https://i.imgur.com/o2Xdhs1.png)
    >按下a,i,o開始編輯

* <b>`Description=OpenSSH server daemon`</b>後面加上一個<b>`2`</b>
    <b>`ExecStart=/usr/sbin/sshd -D $OPTIONS`</b>中間加入<b>`-f /etc/ssh/sshd2_config`</b>
![](https://i.imgur.com/hylpC8T.png)
    >按下esc並輸入`:wq`儲存

* 輸入<b>`systemctl daemon-reload`</b>重新讀取設定檔
    <p>輸入`systemctl enable sshd2`設定重啟後，sshd2會被啟動</p>
    <p>輸入`systemctl start sshd2`啟動sshd2</p>
![](https://i.imgur.com/w2fVcN1.png)
    ><font color="#dd0000"><b>↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑FAILED↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑</b></font>

* 輸入<b>`yum install policycoreutils-python`</b>安裝semanage的套件
![](https://i.imgur.com/QkSYLkk.png)

* 輸入<b>`semanage port -a -t ssh_port_t -p tcp 2222`</b>
    輸入<b>`semanage port -l | grep ssh`</b>檢查 Port 是否為 2222
![](https://i.imgur.com/rLUaPXa.png)

* 輸入<b>`systemctl start sshd2`</b>重新啟動sshd2
![](https://i.imgur.com/GsO8rUn.png)

* 輸入<b>`netstat -tlnp | grep ssh`</b>或<b>`netstat -alntp | grep ssh`</b>確認是否有成功啟動兩個sshd服務![](https://i.imgur.com/MWnOvhd.png)

    # <font color=red size=72>成功！！！！！</font>
