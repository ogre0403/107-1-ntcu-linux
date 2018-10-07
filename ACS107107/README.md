#1.如何安裝LINUX
##1.下載centos的ISO[下載區](http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1804.iso)
##2.下載virtual box[下載區](https://www.virtualbox.org/)
##3.打開virtual box之後按下新增![](https://i.imgur.com/yM4f3RT.jpg)
##4.之後名稱、類型、版本可依個人喜好而設定
##5.下一個步驟中的記憶體也可自由設定
##6.到了建立虛擬機器時選擇立即建立,類型使用VDI
##7.到下個步驟選擇動態配置
##8.之後的虛擬硬碟大小也可自由設定
##9.按下建立後就暫時完成了一個虛擬機器了
##10.在新建立的虛機點右鍵按下設定之後選擇網路設定,確認一下是不是![這個設定](https://i.imgur.com/uSKGmCO.jpg)
##11.再來在上方有一個存放裝置點下去,會看到控制器:IDE下方是空的,這時就要選擇ISO的時候了![](https://i.imgur.com/W5BZ91Y.jpg)把剛剛下載的centosISO存進去
##12.之後進入你的虛機中測試,選項中選擇Install,然後慢慢等待
##13.進入畫面中後,選擇你想要的語言![](https://i.imgur.com/Tg3txWV.jpg)
##14.進入安裝畫面後,按下安裝目的地
##15.之後點選自行配置![](https://i.imgur.com/QxPy118.jpg)
##16.進入此畫面後LVM改成標準分割選擇加號![](https://i.imgur.com/1htF3hM.jpg)
##17.設定兩個分割區/和/home(大小自由設定)![](https://i.imgur.com/3PZbJ2G.jpg)
##18.最後設定網路![](https://i.imgur.com/cYBoojh.jpg)
##19.按下安裝後設定ROOT和USER用戶的帳密![](https://i.imgur.com/zeqhHO1.jpg)
##20.點下重新開機就行了![](https://i.imgur.com/t3b185D.jpg)
##21.輸入帳密![](https://i.imgur.com/RCje08c.jpg)
##22.目錄下已有ROOT和HOME了![](https://i.imgur.com/UUs7LfU.jpg)