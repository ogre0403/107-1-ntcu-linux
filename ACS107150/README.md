## 1. [apache log](https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log)是apache web server的日誌檔

###   請查詢'curl'或'wget'的用法後，用其中一個指令下載此日誌檔。
###   使用bash的pipe指令，例如'grep'、'cat'...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。

	- 直接打curl <要下載的網址> | grep error > <檔案名稱>
	
	- cat <檔案名稱>

	> ![image]()

## 2. 'tar'是linux下用來打包壓縮目錄的工具，請自行查詢'tar'的用法後，用一般使用者身份打包並壓縮'/var'目錄。在'tar'執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至'tar-err.log'檔案。

	- 打tar -jcv -f filename.tar.bz2 /var 2> tar-err.log將錯誤訊息輸出至'tar-err.log'

	- cat 'tar-err.log'

	- (因為錯誤訊息過多，所以只呈現部份結果。)

	> ![image]()