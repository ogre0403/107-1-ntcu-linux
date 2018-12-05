#  1.apache log是apache web server的日誌檔
##  Q:請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。
##  Q:使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。
##  A:我利用了curl的用法加上管線符號以及grep來重新導向錯誤輸出到out，在利用cat來看out中的內容
##  ![](https://i.imgur.com/bU4lamH.jpg)  
##  ![](https://i.imgur.com/csMGXGX.jpg) 
#  2.tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。
##  輸入打tar -jcv -f filename.tar.bz2 /var 2> tar-err.log後並且利用cat tar-err.log 來查看錯誤訊息