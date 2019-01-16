##設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。

* 在VirtualBox中，按右上角**全域工具**->**主機網路管理員**->**建立**
* 按**內容**調整剛剛建立的網路卡，選擇手動組態介面卡，將**IPv4 位址改為192.168.200.10**
* ![1.png]

* **機器工具**->**設定值**->**網路**->**附加到：僅限主機卡**
* ![2.png]

* `ifconfig enp0s3 192.168.200.100`->`ifconfig enp0s3`查看
* ![3.png]


##nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。

* 設定nginx的yum檔案
* `vi /etc/yum.repos.d/nginx.repo`
* 新增內容：
  [nginx]
  name=nginx repo
  baseurl=http://nginx.org/packages/centos/7/$basearch/
  gpgcheck=0
  enabled=1

* `yum install nginx`安裝
> 這邊不知道為甚麼一直出錯，結果重開機就好了。。。
* `service nginx start`，`chkconfig nginx on`啟動nginx
* `netstat -tulnp`查看port
* ![4.png]


##透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。

* ![5.png]


##在Linux裡，用`curl`連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。

* `curl 192.168.200.100`
* ![6.png]


###nginx的日誌檔位於`/var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，格式如下。其中client欄位為客戶端ip。

* `cat /var/log/nginx/error.log | cut -d ' ' -f 16 | sort | uniq -c`
* ![7.png]