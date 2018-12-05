# HW7
## ADT104138 羅苡倫
*****
## 一、apache log是apache web server的日誌檔
*	請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。</br>

利用curl -O 指令，後面接上網址，即可達成要求。</br>
![新增](https://i.imgur.com/Dhn2UMZ.jpg)</br>

*	使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。</br>

利用cat指令打開log檔案，再利用grep指令抓取有error字串的部分。</br>
![新增](https://i.imgur.com/aykW6tM.jpg)</br>

## 二、tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。

利用tar -jcv -f 檔案名字.tar.bz2 要壓縮的檔案 指令，打包後，使用su切換到一般使用者，最後再利用2<指令把錯誤訊息輸出至tar-err.log檔案。</br>

![新增](https://i.imgur.com/9D2WrUx.jpg)</br>
![新增](https://i.imgur.com/WO6HomL.jpg)</br>
![新增](https://i.imgur.com/CwfeGiA.jpg)</br>

# 參考資料：[點擊這裡](http://linux.vbird.org/linux_basic/0240tarcompress.php#tar "參考資料")
# 感謝觀看 The End
