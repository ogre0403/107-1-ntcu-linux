# Final Exam

1. 設定virtualbox虛擬機器，加入一張host-only網路卡，在Linux裡設定虛擬機器的網路為192.168.200.100/24。請用 `ifconfig`驗證。
 + 建立新的網卡，設定IP位址為192.168.200.100/24。

    ![GITHUB]( https://imgur.com/vNZv7O9.jpg"git圖示")
    
 + 設定虛擬機網卡。

    ![GITHUB]( https://imgur.com/OVEL3gT.jpg"git圖示")
    
+ 進入虛擬器，用ifconfig指令設定IP，再檢驗。

    ![GITHUB]( https://imgur.com/DixBVkg.jpg"git圖示")
    
2. nginx是一套網頁伺服器軟體，請用`yum`安裝，透過`systemctl`啟動後，使用`netstat`驗證nginx有在使用Port 80。
    
+ 先安裝 epel，輸入指令 yum install epel-release。
    
    ![GITHUB]( https://imgur.com/69egiSt.jpg"git圖示")
    
    ![GITHUB]( https://imgur.com/qPMrh1J.jpg"git圖示")
    
+ 再安裝 nginx，輸入指令 yum install nginx。

    ![GITHUB]( https://imgur.com/ryk0KKG.jpg"git圖示")
    
    ![GITHUB]( https://imgur.com/axgkqUV.jpg"git圖示")
    
+ 安裝完後用 systemctl start nginx 的指令，啟動 nginx，再用 systemctl status nginx 檢驗。

    ![GITHUB]( https://imgur.com/nq1a9LW.jpg"git圖示")
    
+ 再透過 netstat 的指令驗證nginx有在使用Port 80。
    + 輸入 netstat -ap | grep nginx ，確認 nginx 的連線。
    + 再輸入 netstat -aｎ | grep ：80 ，確認 Port 80 的連線狀況。

    ![GITHUB]( https://imgur.com/dp6VhNz.jpg"git圖示")


3. 透過實體 windows 上的瀏覽器，連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器。

+ 
    
    ![GITHUB]( .jpg"git圖示")
    
    
4. 在Linux裡，用`curl`連線至192.168.200.100。抓?圖驗證可以連線至Linux上的nginx網頁伺服器。

+ 輸入指令 curl 192.168.200.100 ，如下圖。

    ![GITHUB]( https://imgur.com/lIqdugn.jpg"git圖示")
    
    ![GITHUB]( https://imgur.com/k2Zrm7k.jpg"git圖示")

5. nginx的日誌檔位於`/?var/log/nginx`目錄下，當連線不存在的網頁時，nginx會記錄相關資訊，格式如下。其中client欄位為客戶端ip。

+ 