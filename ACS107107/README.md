##  1-1.請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。'
##  輸入vim ~/.bashrc 進入後新增變數
##  ![](https://i.imgur.com/ln8DyZs.jpg)
##  利用source ~/.bashrc讓修改過的變數不用再次登入就生效
##  ![](https://i.imgur.com/5hvI3hI.jpg)
##  輸入cat $HOSTS_PATH來確認有沒有寫入
##  ![](https://i.imgur.com/aqHs6US.jpg)
##  1-2.在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。
##  先用yum groupinstall "Development Tools"安裝gcc
##  在打好程式
##  ![](https://i.imgur.com/Dkyxheb.jpg)
##  之後進行編譯輸出
##  ![](https://i.imgur.com/62oVVKs.jpg)
##  $?的值為1
##  ![](https://i.imgur.com/QtfGVJa.jpg)
##  沒有讀到HOSTS_PATH因為HOSTS_PATH不在子程序當中
##  利用 export 指令將該變數用到子程序中
##  ![](https://i.imgur.com/HsK3wn4.jpg)
##  之後要再打source ~/.bashrc才會生效喔!!
##  之後再編譯執行後就能讀到HOSTS_PATH了
##  echo $?的結果也變成0了
##  ![](https://i.imgur.com/VzfhbPK.jpg)