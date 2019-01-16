### 透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務。

![image](/ACS107106/1.png)
![image](/ACS107106/2.png)
![image](/ACS107106/3.png)
![image](/ACS107106/4.png)
![image](/ACS107106/5.png)
![image](/ACS107106/6.png)
![image](/ACS107106/7.png)

### CentOS有使用SELinux ，故預設只允許 SSH 使用埠號 22，若要使用埠號 2222，請使用指令開啟並檢查

![image](/ACS107106/8.png)

### CentOS預設的防火牆firewalld會禁止訪問埠號2222，若要透過2222埠連ssh，請先關閉firewalld。

![image](/ACS107106/9.png)