#HW10  
##Q1 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令 netstat -alntp | grep ssh 確認是否啟動二個sshd服務   
###流程  
 - 用 netstat -alntp 檢查目前的連線狀況(圖10-1)  
 - 用 systemctl start sshd 啟動 sshd 服務(圖10-2)  
 - 再次用 netstat -alntp 檢查 sshd 服務是否使用(圖10-2)  
 - 用 cd /etc 轉換目錄  
 - 用 ll | grep ssh 確認資料夾在 /etc 這個目錄裡面  
 - 用 cd /etc/ssh 轉進去 ssh 資料夾裡面(圖10-3)  
 - 用 cp sshd_config sshd2_config 把資料複製進去新的檔案(圖10-4)  
 - 用 vi sshd2_config 編輯文件(圖10-5)  
 - 更改 port 的部分(圖10-6 10-7)  
 - 用 yum provides semanage 找到下載 semanage 指令(圖10-8)  
 - 用 yum install policycoreutils-python 安裝指令(圖10-9)  
 - 按照老師的提示操作  
 - 用 cp /usr/lib/systemd/system/sshd.service sshd2.service 把檔案複製  
 - 用 vi sshd2.service 更改資料(圖10-10)  
 - 用 systemctl start sshd2.service 啟動sshd服務(圖10-11)  
 - 用 systemctl daemon-reload 重新啟動資料(圖10-12)  
 - 用 systemctl start sshd2.service 再次啟動sshd2 服務(圖10-12)  
 - 用 netstat -alntp | grep ssh 找出題目要求的東西(圖10-12)  
