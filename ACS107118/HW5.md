##流程一
1.使用* ls -ali *指令查看/ etc / hosts檔案。   
2.可以發現索引節點為4213704且目前有一個檔名共用此碼。  
![](https://ppt.cc/fG776x@.png)

##流程二
1.使用 ln / etc / hosts /srv/hosts.hard 指令建立實體連結  
2.使用 ll / etc / hosts /srv/hosts.hard 指令列出相關詳細資料  
3.找出inode為 4213704 但不同的是，此inode有兩個檔名共用
![](https://ppt.cc/fJh9Ux@.png)

#流程三
1.使用 ln -s /etc/hosts /srv/hosts.soft指令 。
2.以此建立符號連結  
3.由此可見inode碼為13407472且目前有一個檔名共用此碼。  
![](https://ppt.cc/fStAex@.png)
