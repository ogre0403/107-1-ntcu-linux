# HW10
-------------------------------------
## 請仿照課堂上練習，透過systemd管理二個sshd服務，並讓第二個sshd服務的 port 放行於 2222。完成後可以使用指令` netstat -alntp | grep ssh `確認是否啟動二個sshd服務。
* 檢查目前sshd.service的狀態
 > systemctl status sshd.service

![image](01)


* 查看ExecStart:實際執行此daemon的指令或腳本程式
 > cat /usr/lib/systemd/system/sshd.service

![image](02)


* 切換至ssh的目錄
 > cd /etc/ssh

* 將sshd_config的資料複製至sshd2_config
 > cp sshd_config sshd_config

* 編輯sshd2_config中的資料(**修改Port為2222**)
  * **注意!!要將Port 2222前的井字號刪掉!!不然在後面要start sshd2時會有問題!!**
 > vim sshd2_config

![image](03)


![image](04)


* 切換至system的目錄下
  > cd /etc/systemd/system

* 將/usr/lib/systemd/system/sshd.service的內容複製至sshd2.service
  > cp /usr/lib/systemd/system/sshd.service sshd2.service

* 編輯sshd2.service中的資料
  > vim sshd2.service

![image](05)


* 修改其中的Description列，在最後面加上**2**
  > 因為是另一個daemon服務，所以要將從sshd複製過來的檔案修改掉喔!(不然會有問題)

* 還有修改其ExecStart:覆蓋先前已設置的/usr/sbin/sshd
  > ExecStart=/usr/sbin/sshd **-f /etc/ssh/sshd2_config** -D $OPTIONS

![image](06)


* 重新讀取設定檔(修改後都要執行)
  > systemctl daemon-reload

* 設定下次開機時，sshd2會被啟動
  > systemctl enable sshd2

* 立刻啟動sshd2
  > systemctl start sshd2

  > 但會發現是Failed的問題，不過，別擔心，接著做後面的步驟這個問題就會被解決囉!

![image](07)

* 利用**tail**列出後面幾行的資訊
  > tail -n 20 /var/log/messages

  > -n munber:顯示非十行的資訊(原先預設是顯示十行，但要顯示非時行的資訊要加上` -n number `的選項)

  > /var/log/messages隨時會有資料寫入，所以可察看新加入的資料

![image](08)

![image](09)

* 再來先安裝` semanage `的套件，以利之後的步驟進行。
  > yum install policycoreutils-python

![image](10)

    > 解決semanage command not found的問題。
      >  https://www.opencli.com/linux/fix-semanage-command-not-found 

    > semanage 是可以設定 SELinux 的工具，在 RHEL / CentOS minimal 安裝後，並沒有安裝 semanage，所以執行會出現 command not found
  
  > 記得要切換到主目錄下載喔，不然會像我一開始一樣會有問題(這是安裝失敗的畫面!)
![image](11)

  > 這是成功安裝的畫面!
![image](12)

* 讓 ssh 服務使用` 2222 `這個自訂的連接埠號，將這個連接埠號加入` ssh_port_t `列表中
  > semanage port -a -t ssh_port_t -p tcp 2222

* 立刻啟動sshd2(這次就不會有問題囉，以上的步驟以解決先前錯誤的部分)
  > systemctl start sshd2

  > 由於一開始的port連接埠號尚未連接成功，所以才不會啟動成功的喔!

* 確認是否有啟動兩個sshd服務
  > netstat -tlnp | grep ssh

![image](13)


* netstat -tlnp | grep ssh和netstat -alntp | grep ssh會顯示一樣的內容資訊

![image](14)