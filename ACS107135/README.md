### 1.apache log是apache web server的日誌檔<br>

#### 請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。<br>

#### 使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現<br>
##### 用curl -o [檔名] [URL] 下載此日誌檔。<br>
##### cat [檔名] | grep error 只輸出error發生的原因。<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-7/ACS107135/photo/1.PNG)<br>
### 2.tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。<br>
##### tar -c -f [檔名.tar] [目標資料夾] 2> tar-err.log<br>
參數[-c]為建立打包檔案<br>
[2>]為以覆蓋的方式將「錯誤的訊息」輸出到指定的檔案或裝置上<br>
##### cat tar-err.log <br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-7/ACS107135/photo/2.PNG)<br>
![image](https://github.com/ACS107135/107-1-ntcu-linux/blob/HW-7/ACS107135/photo/3.PNG)<br>
