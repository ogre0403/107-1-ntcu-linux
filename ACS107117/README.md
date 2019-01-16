#Final  
###1.  
使用ifconfig指令來修改ip    
![](https://ppt.cc/f4hS2x@.png)  
###2.
然後先安裝編譯工具在安裝PCRE  
接著就可以安裝Nginx了
![](https://ppt.cc/fy5cmx@.png)  
然後再用systemctl start nginx.service來啟動nginx  
接著使用systemctl enable nginx.service來讓他開機時自啟
![](https://ppt.cc/fnGnnx@.png)
![](https://ppt.cc/foLFLx@.png)  
###4.  
使用curl來進入192.168.200.100
![](https://ppt.cc/feFhIx@.png)  
###5.  
使用find找到nginx.conf
![](https://ppt.cc/fvVhtx@.png)  
然後vi /usr/local/webserver/nginx/conf/nginx.conf  
在裡面尋找error.log的位置  
接著cd /usr/local/nginx/logs/
![](https://ppt.cc/fR5DYx@.png)