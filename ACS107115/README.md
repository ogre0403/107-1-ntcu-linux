#homework7    
##q1    
###流程      
 + 先用 curl https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log > out.txt     
   把網站日誌下載下來,並且把結果儲存到 out.txt 這個文字檔      
   (圖hw7-q1-01)      
 + 再用 cat | grep error out.txt 顯示出蒐集過資訊的結果    
   cat 顯示出結果    
   grep 蒐集關鍵字資料    
   error 我要收集的關鍵字    
   (圖hw7-q1-02)  

##補充  
+ 基本上都是用來從網站下載物件的指令,但是 curl 比 wget 多一個上傳的功能  
+ crul 用法    
 - http://charleslin74.pixnet.net/blog/post/419235508-%5Blinux%E6%8C%87%E4%BB%A4%5D-curl%E7%9A%84%E7%94%A8%E6%B3%95    
 - https://www.ewdna.com/2012/04/wget.html    
+ wget 用法    
 - https://www.ewdna.com/2012/04/curl_18.html    



##q2    
###流程    
 + 先用 su - user001 這隻指令切換成一般使用者    
   (圖 hw7-q2-01)  
 + 再用 tar -jvc -f filename.tar.bz2 /var 2> tar-err.log 打包壓縮 var 目錄, 並且將錯誤訊息重新導向至 tar.err.log 這個日誌  
   (圖 hw7-q2-02 是開始, 圖 hw7-q2-03 是中間過程, 圖 hw7-q2-04 是結果)  
 + 最後用 cat tar-err.log 顯示輸出的資料,確認是否符合需求  
   (圖 hw7-q2-05 是開始, 圖hw7-q2-06 是結束)  
##補充  
 + tar 的相關用法在以下幾個網站有比較詳細的介紹  
   - http://charleslin74.pixnet.net/blog/post/434429879-%5Blinux%5D-tar%E6%8C%87%E4%BB%A4%E7%9A%84%E7%94%A8%E6%B3%95  
   - http://www.cnblogs.com/peida/archive/2012/11/30/2795656.html  

##貼心小提示  
 + 其實鳥哥的網站介紹的非常詳細,我個人有買他的書,我個人還蠻推的 