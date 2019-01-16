##設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。

**ifconfig enp0s8 192.168.200.100
**ifconfig即可看到網路為192.168.200.100(圖1)

##nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。

(安裝)
→首先手動加入repo設定，並直接透過yum安裝
**vi /etc/yum.repos.d/nginx.repo
(寫入下方程式)
**
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/6/$basearch/
gpgcheck=0
enabled=1
(即可yum install nginx)(圖2)

(啟動、驗證)
**systemctl start nginx
**netstat -ant | gerp :80
(即可出現如圖3所示)

##透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器。
(圖4)
##在Linux裡，用`curl`連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器
(圖5)

##
**cd var/log/nginx
**ll可以查看到完整的資訊 access.log error.log
**cat error.log 
