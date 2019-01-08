+ 將目錄切至ssh 複製sshd_config 為sshd2_config
![GITHUB](https://imgur.com/1gAnQb1.jpg"git圖示")
+ 編輯sshd2_config將port改成2222
![GITHUB](https://imgur.com/eTjAjTA.jpg"git圖示")
+ 換目錄到/usr/lib/systemd 複製ssh.service為sshd2.service
![GITHUB](https://imgur.com/v3SsqM7.jpg"git圖示")
+ 編輯ssh2.service
![GITHUB](https://imgur.com/UBuF6lB.jpg"git圖示")
+ 下載policycoreutils-python
![GITHUB](https://imgur.com/rKM76OP.jpg"git圖示")
+ 下載完成
![GITHUB](https://imgur.com/qIZFzcB.jpg"git圖示")
+ 關閉防火牆
![GITHUB](https://imgur.com/AGVQBIc.jpg"git圖示")
+ 重仔修改過的文件後開啟ssh2.service後使用netstat -alntp | grep ssh
![GITHUB](https://imgur.com/ooZzODh.jpg"git圖示")
