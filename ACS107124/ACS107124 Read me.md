(一)-1
1. 輸入 " yum -y install wget " 安裝 " wget "指令
2. 輸入 " su -m (username) " 切換一般使用者
3. 輸入 " wget https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log "，下載日誌檔" apache log "

(一)-2
* 輸入 " cat web.log | grep error " 輸出錯誤原因

(二)
1. 輸入" tar -jcv -f filename.tar.bz2 /var 2> tar-err.log "
2. 將 " /var " 目錄打包壓縮
3. 錯誤訊息會輸出至" tar-err.log " 
4. 以 "cat" 查看
