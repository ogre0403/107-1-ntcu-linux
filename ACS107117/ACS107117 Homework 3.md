#1.  
使用useradd來新增使用者  
ex **:** useradd examuser  
  
但是我不知道為啥冒出這個問題
![](https://ppt.cc/fL8tvx@.png)
  
冒出了甚麼cannot lock..............  
於是我就上網查了一下，幾乎都沒有看到，最後只有看到有人說刪掉 /etc/gshadow.lock 就可以了，  
雖然刪掉了之後也可以新增使用者了但是我不知道為什麼......。  
  
如果要刪除使用者則要使用userdel 的指令  
ex **:** userdel examuser  
  
如果要連家目錄一起刪除的話要加-r  
ex **:** userdel -r examuser    
  
輸入userdel -r examuser3刪除examuser3的帳號和目錄。
輸入 id examuser1，查看examuser1的UID和GID，是1001，再輸入adduser -u 1001 examuser1，重新建立examuser1的帳號。

  
  
#2.  
一樣使用useradd增加examuser4  
接著使用cp複製文件到examuser4
ex **:** cp xxxxx /home/examuser4  
然後使用chmod轉換文件權限  
ex **:** chmod xxx xxxxx  
使用mkdir來創造一個文件  
(但要一個一個創資料夾  ex **:** 要創/to/gg 的話要先創/to再創/to/gg)  
修改擁有者用chown指令，群組則是chgrp  
  
修改時間則用touch指令，如下圖

![](https://ppt.cc/fGbXmx@.png)
  
#3.
1.使用mkdir,且r=4,w=2,x=1  
Ex **:** mkdir -m 775 /dev/shm/unit05/    
或是使用mkdir只創資料夾然後用chmod改權限也可行。   
可以用ll語法確定權限是否為自己想要的
 
2.輸入ls -1/dev/shm/unit05/dir[1-4]，
dir1的結果是可讀，  
dir2的結果是可執行，  
dir3的結果是可讀可執行，  
dir4的結果是可讀可修改可執行。  

3.輸入ls -1/dev/shm/unit05/dir1/file[1-4]，
file1的結果是可讀，  
file2的結果是可讀，  
file3的結果是可讀可改寫，  
file4的結果是沒有權限。 



