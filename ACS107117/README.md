使用之前用的 **yum** 指令下載  
**→** **yum -y install wget**  
    
![](https://ppt.cc/f4HcXx@.png)  

然後使用 **wget** 來下載  
**wget https://raw.githubusercontent.com/ogre0403/107-1-ntcu-linux/master/resource/web.log**
  
  
然後使用 **cat web.log | grep error** 將此日誌中error發生的原因輸出至螢幕

![](https://ppt.cc/fh8EWx@.png)  
  
然後換成一般使用者(記得不要用root)    
  
打指令製造一個壓縮檔，並以**tar-err.log**存在當前目錄裡  
**tar -jcv -f filename.tar.bz2 /var 2> tar-err.log**    
  
![](https://ppt.cc/fE1Zhx@.png)
  
最後 **cat tar-err.log**，抓出存在檔案中的錯誤訊息  

![](https://ppt.cc/f6TOSx@.png)