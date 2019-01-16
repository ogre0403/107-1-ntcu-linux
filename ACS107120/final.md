# 期末考

1. 設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。
   請用 `ifconfig`驗證。
  
  ifconfig enp0s8 192.168.200.100/24 netmask 255.255.255.0

2. nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。
  
  yum install nginx
  systemctl start nginx
  systemctl status nginx
  netstat -alntp
  
3. 透過實體 windows 上的瀏覽器，連線至192.168.200.100。
  
  ![image]()

4. 在Linux裡，用`curl`連線至192.168.200.100。
  
  curl 192.168.200.100
  
5. nginx的日誌檔位於`/var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，
   請使用管線指令，找出每個ip連線錯誤的次數。
  
  curl 不存在的網頁 | grep error > out
  
  cat out | cut -d , -f 2 | sort | uniq -c

  
