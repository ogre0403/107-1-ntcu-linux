### 一.
+ 1.(用curl的方法，下載此日誌檔。)
+ 2.輸入curl https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log下載資料
+ 3.在後面再用grep error > error呈現資料，中間用|分開。
+ 4.再輸入cat web.log | grep error
+ 5.只把日誌中error發生的原因輸出至螢幕
***
### 二.
+ 1.輸入tar -jcv -f filename.tar.bz2 /var 2> tar-err.log
+ 2.將錯誤訊息輸出至 tar-err.log
+ 3.再輸入cat tar-err.log查看 tar-err.log 的內容
