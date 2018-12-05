###  <li>apache log是apache web server的日誌檔。</br>
###  <li>apache log網址為 https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log </br></br>

##  Q1:請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。</br>
####  用"curl 網址"下載檔案內容。</br>
##  Q2:使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。</br>
####  在下載的網址後方輸入" | grep error > output "(圖中的黃色框框)將此日誌中error發生的原因輸出至螢幕。</br>
####  再輸入"cat output"檢視錯誤的地方。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen7/1.png)</br></br>

##  Q3:tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。
####  壓縮方式：用"tar -jcv -f filename.tar.bz2 要被壓縮的檔案或目錄名稱"。</br>
####  "2>"是用覆蓋的方法將錯誤的資料輸出到指定的檔案(tar-err.log)。</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen7/2.png)</br></br>

####  J格係正在壓縮的檔案(跑太多了只截了部分)。
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen7/3.png)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen7/4.png)</br></br>

####  再用"cat tar-err.log"檢視錯誤內容。
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen7/5.png)</br>
![Alt text](https://github.com/ad8902210302/107-1-ntcu-linux/blob/master/ACS107127/screen7/6.png)