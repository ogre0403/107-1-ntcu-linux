# Final

### 1.設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。
![](https://i.imgur.com/VLFFRVy.png)

### 2.nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。
![](https://i.imgur.com/3lWY9ek.png)

### 3.透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。
![](https://i.imgur.com/jdxZiYf.png)

### 4.在Linux裡，用`curl`連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。
![](https://i.imgur.com/lFV76EM.png)

### 5.nginx的日誌檔位於`/var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊。其中client欄位為客戶端ip。請使用管線指令，找出每個ip連線錯誤的次數。你可能需要使用 `cat`、`cut -d` 、 `sort` 、 `uniq -c`，最後輸出格式，表示自127.0.0.1來的ip發生二次錯誤，自192.168.200.100來的ip發生二次錯誤. 
![](https://i.imgur.com/ZaBhrfQ.png)

#祝老師新年快樂~~~