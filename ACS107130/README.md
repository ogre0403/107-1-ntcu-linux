# 1.apache log是apache web server的日誌檔
## Q1.請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。
### 輸入curl 網址下載
## Q2.使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。
### 於網址後輸入| grep error > output將此日誌中error發生的原因輸出至螢幕，然後輸入cat output。
![7](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-7/ACS107130/7.PNG)
![8](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-7/ACS107130/8.PNG)
# 2.tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。
### 輸入tar -jcv -f filemane.tar.bz2 /var 2> tar-err.log
![6](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-7/ACS107130/6.PNG)
![3](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-7/ACS107130/3.PNG)
### 輸入cat tar-err.log檢視錯誤
![4](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-7/ACS107130/4.PNG)
![5](https://github.com/hfjdgfj/107-1-ntcu-linux/blob/HW-7/ACS107130/5.PNG)