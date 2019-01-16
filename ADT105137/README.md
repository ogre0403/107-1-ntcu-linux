# ADT105137_HW10
1.sshd 的設定檔位於 /etc/ssh/sshd_config，所以複製一個sshd2_config的檔案。

![image](https://github.com/Yubo0826/0107/blob/master/1.PNG)

2.更改裡面內容，在隨便一行加上port 2222

![image](https://github.com/Yubo0826/0107/blob/master/2.PNG)

3.接著修改啟動腳本服務檔，把/usr/lib/systemd/system/sshd.service 複製到/etc/systemd/system ，檔名叫做sshd2.service

![image](https://github.com/Yubo0826/0107/blob/master/3.PNG)

4.更改Unit裡的Description=OpenSSH server daemon 2 ， 和Service裡的ExecStart=/usr/sbin/sshd -f /etc/ssh/sshd2_config -D $OPTIONS

![image](https://github.com/Yubo0826/0107/blob/master/4.PNG)

5.做到這個步驟本應該是差不多了，但是Centos內建還有一層保護，叫做SElinux，會阻止SSH 監聽2222這個port，所以需要用到這個指令semanage來解決

6.首先要使用semanage，需要安裝，yum provides semanage，接著安裝 yum install policycoreutils-python即可。

7.打上semanage port -a -t ssh_port_t -p tcp 2222 這項指令，接著重啟ssh即可完成!

![image](https://github.com/Yubo0826/0107/blob/master/7.PNG)
