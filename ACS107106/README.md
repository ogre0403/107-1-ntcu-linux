* 設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。
![image](/ACS107106/1.png)
![image](/ACS107106/2.png)
![image](/ACS107106/3.png)
![image](/ACS107106/4.png)

* nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。
![image](/ACS107106/5.png)
![image](/ACS107106/6.png)
![image](/ACS107106/7.png)

* 透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。
![image](/ACS107106/8.png)

* 在Linux裡，用`curl`連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。
![image](/ACS107106/9.png)

* nginx的日誌檔位於`/var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，格式如下。其中client欄位為客戶端ip。
![image](/ACS107106/10.png)
![image](/ACS107106/11.png)