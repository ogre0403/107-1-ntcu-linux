* 的使用
">" 的使用
![]()
空四個有另一種用法

### 1.apache log是apache web server的日誌檔
### 請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。
### 使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。

    yum -y install wget 下載wget
    wget 是在進行"網路資料"的取得，語法: wget [-option] [url]

` wget https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log `
會產生出一個web.log檔，裡面有所有的資料
![1](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-7/ACS107134/1.PNG)
    
我們透過 cat web.log | grep error 讓他輸出error的資訊。
![2](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-7/ACS107134/2.PNG)

### 2.tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。
### 在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。

    tar 只能打包不能壓縮，需要經過tar再經過gzip or bzip2的格式壓縮。

![3](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-7/ACS107134/3.PNG)