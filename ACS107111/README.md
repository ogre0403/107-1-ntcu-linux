+ 用ifconfig設定ens37為192.168.200.100 用ifconfig檢驗
![GITHUB](https://imgur.com/CiTRQWB.jpg"git圖示")
+ 安裝nginx後用systemctl啟動
![GITHUB](https://imgur.com/Y11JqNG.jpg"git圖示")
+ 使用netstat -tulpn確認port80為nginx
![GITHUB](https://imgur.com/yLhCknL.jpg"git圖示")
+ 也可用netstat -ant |grep:80檢查 
+ 用curl 192.168.200.100連線
![GITHUB](https://imgur.com/h4WjzRb.jpg"git圖示")
+ 用google連接IP 但我好像用錯網卡了所以IP是另一張的
![GITHUB](https://imgur.com/wpPL4Ra.jpg"git圖示")
+ 因此我再用curl連接192.168.174.128
![GITHUB](https://imgur.com/J1TZE5y.jpg"git圖示")
+ 用cut -d , -f 2 /var/log/nginx/error.log |sort|uniq -c查看錯誤訊息
![GITHUB](https://imgur.com/SUW9pWe.jpg"git圖示")