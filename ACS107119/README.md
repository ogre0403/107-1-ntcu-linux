#1
1.按全域工具進入全域工具,再按左上角的建立,建立新的網路卡,然後按左上角的內容,更改內容為192.168.200.100/24。用ip address add 192.168.200.100/24 broadcast + dev enp0s3 設定虛擬機器的網路。用 `ifconfig`驗證,並用ping 192.168.200.100確定有連線到。

2.先用rpm -ivh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rp載他的安裝檔,並用yum install nginx安裝,再用systemctl start nginx啟動nginx,最後用netstat -tulpn查看是否nginx有在使用Port 80。

