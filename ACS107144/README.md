### 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務

* 查看 sshd.service 目前的狀態
  * 輸入`systemctl status sshd.service`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-01.png)

* 切換至 ssh 目錄
  * 輸入 `cd /etc/ssh`
* 將 sshd_config 的資料複製至 sshd2_config
  * 輸入 `cp sshd_config sshd2_config`
* 編輯 sshd2_config 中的資料
  * 輸入 `vim sshd2_config`

  * 將 `#Port 22` 改成 `Port 2222`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-02.png)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-03.png)

* 切換至 system 目錄下
  * 輸入 `cd /etc/systemd/system`
* 將 /usr/lib/systemd/system/sshd.service 的內容複製至 sshd2.service
  * 輸入 `cp /usr/lib/systemd/system/sshd.service sshd2.service`
* 編輯 sshd2.service 中的資料
  * 輸入 `vim sshd2.service`

  * 將 `Description=OpenSSH server daemon` 改成 `Description=OpenSSH server daemon 2`

  * 將 `ExecStart=/usr/sbin/sshd -D $OPTIONS` 改成 `ExecStart=/usr/sbin/sshd -f etc/ssh/sshd2_config -D $OPTIONS`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-04.png)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-05.png)

* 重新讀取設定檔
  * 輸入 `systemctl daemon-reload`
* 設定重新開機後，sshd2會被啟動
  * 輸入 `systemctl enable sshd2`
* 立即啟動sshd2
  * 輸入 `systemctl start sshd2`
* 結果為 failed
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-06.png)


* 安裝 semanage 的套件
  * 輸入 `yum install policycoreutils-python`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-07.png)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-08.png)

* 確定 port 為 2000 設定成功
  * 輸入 `semanage port -a -t ssh_port_t -p tcp 2222`

  * 輸入 `semanage port -l | grep ssh`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-09.png)

* 再啟動sshd2
  * 輸入 `systemctl start sshd2`
* 確認是否有成功啟動兩個 sshd 服務
  * 輸入`netstat -tlnp | grep ssh` 或 `netstat -alntp | grep ssh`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-10/ACS107144/10-1-10.png)



