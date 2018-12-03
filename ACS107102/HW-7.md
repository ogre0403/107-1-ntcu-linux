#### 指令連續下達和資料重流導向
### 指令
## `apache log`是`apache web server`的日誌檔
1.  `apache log` 的連結 `https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log`
    `curl https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log | grep error > out`
2.  `cat out`

    ```
    [Sun Mar 7 21:16:17 2004] [error] [client 24.70.56.49] File does not exist: /home/httpd/twiki/view/Main/WebHome
    ```

### 資料重流導向
1. `tar`是linux下用來打包壓縮目錄的工具，請自行查詢`tar`的用法後，用一般使用者身份打包並壓縮`/var`目錄。在`tar`執行過程中，忽略正常輸出結果，但需將錯誤訊息輸出至`tar-err.log`檔案。
   `tar -jcv -f filename.tar.bz2 /var 2> tar-err.log`
   `cat tar-err.log`列印錯誤資料