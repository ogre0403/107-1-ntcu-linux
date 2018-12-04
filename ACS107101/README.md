####HW7
# 第一題
+
+ 1.
+(1)apache log是apache web server的日誌檔
+
+#請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔
+apache log 的連結 https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log
+
+用curl下載資料，再後面再用grep error > error呈現資料。
+
+輸入curl https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log | grep error > out
+
+(2)
+再輸入cat web.log | grep error
+
+只把日誌中error發生的原因輸出至螢幕
+
#第二題
+
+ #tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。
+輸入tar -jcv -f filename.tar.bz2 /var 2> tar-err.log
+
+>tar -jcv -f filename.tar.bz2用來壓縮，/var檔案名稱，2> tar-err.log把錯誤訊息輸出至tar-err.log裡
+
+*輸入cat tar-err.log