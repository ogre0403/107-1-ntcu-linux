# HW6
#### 第一題
+請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。
+輸入 vi ~/.bashrc，輸入i進入編輯
+![GITHUB](https://imgur.com/prU8anI.jpg"git圖示")
+新增 HOSTS_PATH=/etc/hosts，並點選ESC鍵離開，並輸入:wq存取離開
+![GITHUB](https://imgur.com/Ph9R6wy.jpg"git圖示")
+輸入source ~/.bashrc不登出讓HOSTS_PATH變數生效
+再輸入cat $ HOSTS_PATH確認有讀取到檔案內容
+![GITHUB](https://imgur.com/TOM8Oad.jpg"git圖示")
+
#### 第二題
+先安裝gcc
+輸入vi 6.c 來輸入程式碼
+![GITHUB](https://imgur.com/S7ghNGK.jpg"git圖示")
+輸入 gcc 6.c
+輸入 ll 6.c a.out
+輸入./a.out
+會顯示 getenv() return NULL(錯誤)
+輸入 echo $?
+會顯示 1(代表沒執行)
+正確做法為 在前面vi ~/.bashrc裡
+HOSTS_PATH=/etc/hosts前面要加export
+這樣 ./a.out才會顯示成正確
+輸入echo $? 也會變成 0