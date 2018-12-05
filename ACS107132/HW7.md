##一.

#請查詢 curl 或 wget 的用法後，用其中一個指令下載此日誌檔。

#使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。

* 使用man可以查看指令用法

1. (我使用curl){{{curl https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log | grep error}}}
+ 使用{{{crul -s}}}可以不顯示進程

* [見圖1]圖中顯示沒有使用{-s}跟有使用的差異

##二.

#用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。

1. {{{tar -jvc -f file.tar.bz2 /var 2> tar-err.log}}} [見圖2]
+ 將/var的目錄打包壓縮，並將錯誤訊息輸出到tar-err.log
2. {{{cat tar-err.log}}} [見圖3]
+ 將錯誤資料輸出
