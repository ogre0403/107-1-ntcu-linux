#HW10  
  
可以先關個防火牆  
![Imgur](https://i.imgur.com/f2727Sw.png)  
  
也安裝一下東西 
![Imgur](https://i.imgur.com/B34YLi3.png)  
![Imgur](https://i.imgur.com/OcwZiOT.png)

首先要用cd指令先到 **/etc/ssh** 然後複製一個 **sshd**  
![Imgur](https://i.imgur.com/0HI42u9.png)  
  
接著使用vi修改裡面的port把她從22改成2222，  
![Imgur](https://i.imgur.com/IRrIGPL.png)  
  
之後一樣使用cd到 **/etc/systemd/system** 裡面，然後複製**sshd.service**  
![Imgur](https://i.imgur.com/7W6ccAO.png)  
  
接著用vi修改設定使他可以使用  
![Imgur](https://i.imgur.com/nJXlkHm.png)  
  
最後重新啟動一下設定還有開啟sshd2  
![Imgur](https://i.imgur.com/OcwZiOT.png)  
  
然後就完成啦!!!!!!  


