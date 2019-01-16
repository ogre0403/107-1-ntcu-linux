#  1.設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。
##  ![](https://i.imgur.com/igAZnV6.jpg)
#  2.nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。
##  使用yum install nginx，之後輸入systemctl start nginx啟動，最後輸入netstat -tulnp 來查看。
##  ![](https://i.imgur.com/W99GL7v.jpg)

#  3.透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓�圖驗證可以連線至Linux上的nginx網頁伺服器。
##  ![](https://i.imgur.com/VUm8j4M.jpg)
#  4.在Linux裡，用`curl`連線至192.168.200.100。抓�圖驗證可以連線至Linux上的nginx網頁伺服器。
##  輸入curl 192.168.200.100即可登入
##  ![](https://i.imgur.com/YAOWTPV.jpg)
##  ![](https://i.imgur.com/47Xg0N8.jpg)
##  5.nginx的日誌檔位於`/�var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，格式如下。其中client欄位為客戶端ip