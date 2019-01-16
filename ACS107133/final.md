* 設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 ifconfig驗證。(25%)

1.打開virtualbox點選全域工具，再點選上方的主機網路管理員，建立新的網路卡並輸入IPv4位址192.168.200.100

2.再到設定值，點選網路，將新增網路卡為僅限主機介面卡，並使用剛剛新增的網路。

3.打開虛擬機器，輸入ip a 可發現新增了virbr0，輸入ip address add 192.168.200.100 broadcast + dev virbr0 label virbr0，再輸入ifconfig查看(圖1)

* nginx是一套網頁伺服器軟體，請用yum安裝，透過systemctl啟動後，使用netstat驗證nginx有在使用Port 80。(25%)

1.輸入 yum install nginx下載

2.輸入 systemctl start nginx 啟動

3.輸入netstat -nlp | grep nginx (圖2)

* 透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)

(圖3)

* 在Linux裡，用curl連線至192.168.200.100。抓圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)

1.輸入 curl 192.168.200.100 (圖4)

* nginx的日誌檔位於/var/log/nginx目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，格式如下。其中client欄位為客戶端ip。 (30%)

圖5

圖6