#Final Test

 +1.設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。(25%)

 ![GITHUB](https://imgur.com/30TnPbL.jpg"git圖示")

 +2.nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。(25%)

 先建立檔案 /etc/yum.repos.d/nginx.repo，在檔案內加入下方圖片文字，就可以用yum來安裝nginx

 ![GITHUB](https://imgur.com/5i9EbSB.jpg"git圖示")

 ![GITHUB](https://imgur.com/5GiMadT.jpg"git圖示")

 ![GITHUB](https://imgur.com/RRhFtbh.jpg"git圖示")

 +接著netstat -alntp 看nginx service使用到哪個port，就可以看出使用的port是80。

 ![GITHUB](https://imgur.com/X9QPUB2.jpg"git圖示")

 +3.透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)

 ![GITHUB](https://imgur.com/xqGL1Pk.jpg"git圖示")

 +4.在Linux裡，用`curl`連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)

 ![GITHUB](https://imgur.com/GVSgF5t.jpg"git圖示")

 