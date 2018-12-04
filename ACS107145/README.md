### 一.
+ 1.先用 vi .bashrc 進入檔案編輯，在按下i即可開始編輯
+ 2.在最末行新增shell變數 HOSTS_PATH="/etc/hosts" ，輸入完後按下ESC鍵離開編輯，再輸入:wq就可以儲存然後離開編輯模式了。，
+ 3.用 source ~/.bashrc 使修改過的變數不用再次登入就生效
+ 4.輸入cat $HOSTS_PATH確認是否能成功讀取到檔案內容

### 二.
+ 1.tar是linux下用來打包壓縮目錄的工具，請自行查詢tar的用法後，用一般使用者身份打包並壓縮/var目錄。在tar執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至tar-err.log檔案。
+ 2.輸入tar -jcv -f filename.tar.bz2 /var 2> tar-err.log
+ 3.tar -jcv -f filename.tar.bz2用來壓縮，/var檔案名稱，2> tar-err.log把錯誤訊息輸出至tar-err.log裡
+ 4.輸入cat tar-err.log式是正常執行的