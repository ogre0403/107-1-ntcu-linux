## 依下列描述完成並說明各項問題：<br>
### 1.請查詢 curl 或 wget 的用法後，用其中一個指令下載(apache web server)的日誌檔(apache log)。<br>

```
wegt https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log
```
下載完後的檔案為 web.log<br>

### 2.使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。<br>

```
cat web.log |grep error
```

### 3.tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。<br>

```
tar -c -f homework.tar /var 2> rat.err.log
```