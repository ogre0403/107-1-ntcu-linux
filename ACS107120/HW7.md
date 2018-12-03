# 第一題

  1.
  
  (1) apache log是apache web server的日誌檔，用一個指令下載此日誌檔
  
  curl https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log | grep error > out
  
  (2) 使用bash的pipe指令，例如grep、cat...等等，將此日誌中error發生的原因輸出至螢幕，但其他資訊不需要呈現。
  
  cat out
  
  2. tar是linux下用來打包壓縮目錄的工具
  
  (1) 用一般使用者身份打包並壓縮/var目錄
  
  tar -jcv -f filename.tar.bz2 /var 2> tar-err.log
  
  (2) 在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。
  
  cat tar-err.log