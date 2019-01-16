### 設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。

* 在全域工具中先新增一張192.168.200.100的網路卡
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/final/ACS107144/f-01.png)
* 用root登入虛擬機
* 輸入`ip address add 192.168.200.100/24 broadcast + dev enp0s8`
* 輸入`ifconfig enp0s8`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/final/ACS107144/f-02.png)

### nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。

* 輸入`yum install nginx`
* 輸入`systemctl start nginx`
* 輸入`systemctl status nginx`
  * 查看nginx的狀態
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/final/ACS107144/f-03.png)
* 輸入`netstat -alntp | grep nginx`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/final/ACS107144/f-04.png)

### 透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/final/ACS107144/f-06.png)

### 在Linux裡，用`curl`連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。
* 輸入`curl http://192.168.200.100/`
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/final/ACS107144/f-05.png)

### nginx的日誌檔位於`/var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，格式如下。其中client欄位為客戶端ip。 (30%)

```
2019/01/15 19:28:28 [error] 12337#0: *4 open() "/usr/share/nginx/html/aa" failed (2: No such file or directory), client: 127.0.0.1, server: _, request: "GET /aa HTTP/1.1", host: "127.0.0.1"
```

請使用管線指令，找出每個ip連線錯誤的次數。你可能需要使用 `cat`、`cut -d` 、 `sort` 、 `uniq -c`

最後輸出格式，表示自127.0.0.1來的ip發生二次錯誤，自192.168.200.100來的ip發生二次錯誤. 

```
    2  127.0.0.1
    1  192.168.200.100
```

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/final/ACS107144/f-07.png)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/final/ACS107144/f-08.png)
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/final/ACS107144/f-09.png)
