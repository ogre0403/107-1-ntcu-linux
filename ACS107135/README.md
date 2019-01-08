## 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的port放行於2222。完成後可以使用指令`netstat -alntp | grep ssh`確認是否啟動二個sshd服務，範例如下：

```sh
$ netstat -alntp | grep ssh
tcp 0 0 0.0.0.0:22 0.0.0.0: *       LISTEN 1300/sshd
tcp 0 0 0.0.0.0:2222 0.0.0.0: *       LISTEN 15275/sshd
tcp6 0 0 :::22 ::: *            LISTEN 1300/sshd
tcp6 0 0 :::2222 ::: *            LISTEN 15275/sshd
```

 Note 1: CentOS有使用SELinux ，故預設只允許 SSH 使用埠號 22，若要使用埠號 2222，使請用下列指開啟並檢查

    ```sh
    $ semanage port -a -t ssh_port_t -p tcp 2222
    $ semanage port -l | grep ssh
    ssh_port_t tcp 2202, 22
    ```  

    Note 2: CentOS預設的防火牆firewalld會禁止訪問埠號2222，若要透過2222埠連ssh，請先關閉firewalld。

### `netstat -alntp | grep ssh` 確認sshd服務
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/1.PNG)</br></br>
### `yum provides semanage`查詢semanage於哪個套件
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/2.PNG)</br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/3.PNG)</br></br>
### `yum install policycoreutils-python`安裝工具
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/4.PNG)</br></br>
### 
    ```sh
    $ semanage port -a -t ssh_port_t -p tcp 2222
    $ semanage port -l | grep ssh
    ssh_port_t tcp 2202, 22
    ```  
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/5.PNG)</br></br>
### `service firewalld stop` 關閉firewalld防火牆
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/6.PNG)</br></br>
### 複製sshd_config至sshd2_config
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/7.PNG)</br></br>
### 修改`#Port 22`為`Port 2222`
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/8.PNG)</br></br>
### 複製sshd.service至sshd2.service
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/9.PNG)</br></br>
### 修改sshd2.service
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/10.PNG)</br></br>
### `systemctl daemon-reload`重新讀取設定
### `systemctl start sshd2.service`啟用sshd2.service
### `netstat -alntp | grep ssh`確認第二個sshd服務已啟動
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-10/ACS107135/photo/11.PNG)</br></br>