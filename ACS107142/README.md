# 1.apache log是apache web server的日誌檔
*  ##  請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。
### 使用curl下載
![](https://i.imgur.com/2CmSgqy.png)
* ##  使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。
### 使用grep抓出error發生的原因
![](https://i.imgur.com/8gMwTTG.png)
# 2.tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。
### 用tar -jcv -f filename.tar.bz2 /var 2> tar-err.log將錯誤訊息輸出至tar-err.log,然後用cat查看