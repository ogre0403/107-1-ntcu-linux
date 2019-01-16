* 設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。(25%)</br></br>

在virtual box 的全域工具上加入一張host-only網路卡，並在虛擬機器內輸入`ifconfig enp0s3 192.168.200.100`，
輸入`ifconfig`可以在裡面發現多了一行192.168.200.100，最後用`ping 192.168.200.100`測試連接成功。
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/1.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/2.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/3.png)</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/4.png)</br></br>

* nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。(25%)</br></br>

輸入`vi /etc/yum.repos.d/nginx.repo`，並在內容新增
`[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1`
接著就可以下指令安裝`yum install nginx`</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/5.png)</br></br>

啟動 Nginx 服務：`systemctl start nginx`</br>
檢查 Nginx 是否正常啟動：`systemctl status nginx`</br>
用`netstat -ano | grep 0.0:80`驗證nginx有在使用Port 80</br>
![1](https://github.com/ad8902210302/107-1-ntcu-linux/blob/final/ACS107127/screen/6.png)</br></br>

* 透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)
![]()</br></br>

* 在Linux裡，用`curl`連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)
![]()</br></br>

* nginx的日誌檔位於`/?var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，格式如下。其中client欄位為客戶端ip。 (30%)