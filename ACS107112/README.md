## 第一題
+ 先用vi .bashrc 進入檔案編輯
![](https://i.imgur.com/y9APBrg.png)
+ 在最末行新增shell變數HOSTS_PATH=/etc/hosts
![](https://i.imgur.com/0SChmdH.png)
+ 用 source ~/.bashrc 使修改過的變數不用再次登入就生效
![](https://i.imgur.com/FI2kyVc.png)
+ 用 cat $HOSTS_PATH 來確認有寫入
![](https://i.imgur.com/es6Iw1o.png)
## 第二題
+ 用vim寫一個C語言程式
![](https://i.imgur.com/3ZrWMO6.png)
+ 用 gcc hw6.c 來編譯這隻程式
+ 以 ll hw6.c a.out 建立這個程式的執行檔
+ 用 ./a.out 執行程式
+ 用 echo $? 會發現程式其實沒有正確執行
+ 進 .bashrc 的檔案裏面
+ 用 export HOSTS_PATH 把程式編譯上去
+ 用 source ~/.bashrc 讓它放在上去
+ 用 gcc hw6.c 這個指令來編譯這隻程式
+ 用 ll hw6.c a.out 建立這個程式的執行檔
+ 用 ./a.out 這個指令執行程式(結果終於對了)
+ 用 echo $? 這個指令後
+ 結果是0
+ 代表程式是正常執行的
## 後面忘記截到圖片了...





