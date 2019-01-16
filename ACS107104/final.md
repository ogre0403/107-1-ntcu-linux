#設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。

*進入virtuallbox點選右上角全域工具→點選主機網路管理員→點選建立→在位址 輸入192.168.100.1;網路遮罩 輸入255.255.255.0→按後方啟用即可完成

*輸入ip address add 192.168.200.100/24 broadcast + dev enp0s8

*輸入ip addr(因為輸入ifconfig無法跑出，所以以ip addr代替)

![image](1)

#nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。

*sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm

*sudo yum install -y nginx

*sudo systemctl start nginx.service

![image](2)

#透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器。

*

![image](3)

#在Linux裡，用`curl`連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器。

*curl 192.168.200.100

![image](4)

#nginx的日誌檔位於`/?var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，格式如下。其中client欄位為客戶端ip。

*