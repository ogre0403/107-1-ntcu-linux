# Final期末作業
## ADT104138 羅苡倫
*****
## 請依下述情境完成系統操作後再用相關指令進行驗證，請抓驗證指令的圖：
*	設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。(25%)</br>

打開程式，在右邊全域工具點擊進入，並且案新增一個網路，把ip改成192.168.200.100，並且利用ifconfig指令設定IP及顯示IP驗證。</br>
![新增](https://i.imgur.com/yTyy0j4.png)</br>
![新增](https://i.imgur.com/STivMT6.png)</br>
![新增](https://i.imgur.com/ePEzUbG.png)</br>

*	nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。(25%)</br>

要先安裝之前先使用指令```sudo rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm```</br>
然後再利用yum指令安裝，最後輸入```sudo systemctl start nginx.service```啟動即可。</br>

![新增](https://i.imgur.com/E2uXedR.png)</br>
![新增](https://i.imgur.com/vm87QvK.png)</br>
![新增](https://i.imgur.com/P8am1OU.png)</br>

最後再檢查是否占用port80</br>
![新增](https://i.imgur.com/orZQy1Z.png)</br>

*	透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓�圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)</br>

Linux裡面可以顯示，不知道為什麼windows就是不能。
![新增](https://i.imgur.com/7C9xY5p.png)</br>


*	在Linux裡，用`curl`連線至192.168.200.100。抓�圖驗證可以連線至Linux上的nginx網頁伺服器。(10%)</br>

利用curl 指令驗證</br>
![新增](https://i.imgur.com/h2cuM4R.png)</br>

*	nginx的日誌檔位於`/�var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，格式如下。其中client欄位為客戶端ip。 (30%)</br>
故意輸入錯一次網址，便可利用指令顯示</br>
![新增](https://i.imgur.com/R2DBLoi.png)</br>

# 感謝觀看 The End
