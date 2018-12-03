#第一題:
apache log網址:https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log

用man curl查詢使用方法
用curl https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log | grep error > out下載此日誌檔，並將此日誌中error發生的原因輸出至out
用cat out將此日誌中error發生的原因顯示至螢幕

#第二題:
用man tar查詢使用方法
用tar -jcv -f filename.tar.bz2 /var 2> tar-err.log打包並壓縮/var目錄，並將錯誤訊息輸出至tar-err.log檔案
用cat tar-err.log將錯誤訊息顯示至螢幕


