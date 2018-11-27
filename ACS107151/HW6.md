### 一.
+ 1.先用 vi .bashrc 進入檔案編輯，在按下i即可開始編輯
+ 2.在最末行新增shell變數 HOSTS_PATH="/etc/hosts" ，輸入完後按下ESC鍵離開編輯，再輸入:wq就可以儲存然後離開編輯模式了。，
+ 3.用 source ~/.bashrc 使修改過的變數不用再次登入就生效
+ 4.輸入cat $HOSTS_PATH確認是否能成功讀取到檔案內容
***
### 二.
+ 1.用vim寫一個C語言程式
+ 2.用 gcc hw6.c 來編譯這隻程式
+ 3.以 ll hw6.c a.out 建立這個程式的執行檔
+ 4.再用 ./a.out 執行程式
+ 5.用 echo $? 會發現程式其實沒有正確執行
+ 6.進 .bashrc 的檔案裏面
+ 7.用 export HOSTS_PATH 把程式編譯上去
+ 8.用 source ~/.bashrc 讓它放在上去
+ 9.再用 gcc hw6.c 這個指令來編譯這隻程式
+ 10.用 ll hw6.c a.out 建立這個程式的執行檔
+ 11.用 ./a.out 這個指令執行程式(和一開始做的步驟一樣)
+ 12.用 echo $? 可以發現結果是0，代表程式是正常執行的