# HW10
### 使用ubuntu
一、請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務，範例如下：</br>
複製sshd_config，製造成sshd2_config</br>
![1](img/1.png)</br>
開啟sshd2_config並將port改成2222</br>
![2](img/2.png)</br>
複製sshd.service，製造成sshd2.service，並編輯</br>
![3](img/3.png)</br>
將ExecStart=/usr/sbin/sshd -f /etc/ssh/sshd2_config -D $SSHD_OPTS</br>
![4](img/4.png)</br>
用systemctl指令重啟</br>
![5](img/5.png)</br>
安裝policycoreutils-python-utils，安裝此第三方包才能執行下一航程式</br>
![7](img/7.png)</br>
<pre><code>semanage port -a -t ssh_port_t -p tcp 2222</code></pre>
![6](img/6.png)</br>
<pre><code>netstat -alntp | grep ssh</code></pre>
![8](img/8.png)</br>
