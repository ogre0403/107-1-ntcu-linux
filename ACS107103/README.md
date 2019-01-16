<strong>期末考</strong>

<em>1.<em>
+ 先開啟VMWARE並為虛擬機器添加一張網卡
+ 在右邊的選項選擇HOST-ONLY
![image](netcard.PNG)
+ 接著開啟自帶的Virtual Machine Editor進行設定
+ 將Subnet IP設定為192.168.200.0
![image](vnedit.png)
+ 在機器內執行ifconfig ens37 192.168.200.100手動設定IP位址
![image](centos-2019-01-16-13-53-17.png)
![image](centos-2019-01-16-13-53-35.png)

<em>2.<em>
+ 先執行yum install nginx來安裝nginx
![image](centos-2019-01-16-13-54-33.png)
![image](centos-2019-01-16-13-56-11.png)
![image](centos-2019-01-16-13-56-29.png)
+ 接著執行systemctl start nginx來啟動nginx
+ 再來執行netstat -alntp來查看port的使用狀態
+ 如圖所示80 port正在被nginx使用並監聽中
![image](centos-2019-01-16-13-57-34.png)

<em>3.<em>
+ 在windows上開啟瀏覽器並造訪192.168.200.100
![image](winbrowser.PNG)

<em>4.<em>
+ 在機器內執行curl 192.168.200.100抓取網頁內容
![image](centos-2019-01-16-14-27-14.png)
![image](centos-2019-01-16-14-27-27.png)

<em>5.<em>
+ 執行cat error.log | cut -d , -f 2 | cut -d : -f 2 | uniq -c
+ 如圖所示 可以看到來自192.168.200.1的錯誤有3次
![image](centos-2019-01-16-15-46-15.png)
