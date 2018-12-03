第一題

-輸入wget https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log載入資料
-cat web.log | grep error
-結果如圖所示

第二題

--c  ：建立打包檔案，可搭配 -v 來察看過程中被打包的檔名(filename)
--j  ：透過 bzip2 的支援進行壓縮/解壓縮：此時檔名最好為 *.tar.bz2
--v  ：在壓縮/解壓縮的過程中，將正在處理的檔名顯示出來！
使用方式:
壓　縮：tar -jcv -f filename.tar.bz2 要被壓縮的檔案或目錄名稱

--輸入tar -jcv -f filename.tar.bz2 /var 2> tar-err.log
--cat tar-err.log