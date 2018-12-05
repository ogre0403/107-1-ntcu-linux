1.(這邊選擇用wget的方式)，先輸入yum -y install wget來安裝wget的指令，
安裝完成後，輸入su -m (username)來切換成一般的使用者，
再輸入wget https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log，
來下載apache log這個日誌檔。
2.輸入cat web.log | grep error來輸出發生錯誤的原因。
------------------------------------------------------------------------------------------------------
1.輸入tar -jcv -f filename.tar.bz2 /var 2> tar-err.log，
可以將/var的目錄打包壓縮，並將錯誤訊息輸出到tar-err.log。