#### 1.請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令`netstat -alntp | grep ssh`確認是否啟動二個sshd服務，範例如下：

$ netstat -alntp | grep ssh
tcp        0      0 0.0.0.0:22     0.0.0.0:*     LISTEN      1300/sshd
tcp        0      0 0.0.0.0:2222   0.0.0.0:*     LISTEN      15275/sshd
tcp6       0      0 :::22          :::*          LISTEN      1300/sshd
tcp6       0      0 :::2222        :::*          LISTEN      15275/sshd
Note 1: CentOS有使用SELinux ，故預設只允許 SSH 使用埠號 22，若要使用埠號 2222，使請用下列指開啟並檢查

```sh
$ semanage port -a -t ssh_port_t -p tcp 2222
$ semanage port -l | grep ssh
ssh_port_t tcp 2202, 22
```  

Note 2: CentOS預設的防火牆firewalld會禁止訪問埠號2222，若要透過2222埠連ssh，請先關閉firewalld。

- cd /etc/ssh
- cp sshd_config sshd2_config
- vi sshd2_config加上Port 2222

> ![GITHUB]()

- cd /etc/systemd/system
- cp /usr/lib/systemd/system/sshd.service sshd2.service
- vi sshd2.service把ExecStart=/usr/sbin/sshd -D $OPTIONS改為ExecStart=/usr/sbin/sshd -f /etc/ssh/sshd2_config -D $OPTIONS

> ![GITHUB]()

- systemctl daemon-reload
- yum install policycoreutils-python
- semanage port -a -t ssh_port_t -p tcp 2222
- semanage port -l | grep ssh
- systemctl stop firewalld關掉防火牆
- netstat -alntp | grep ssh

> ![GITHUB]()