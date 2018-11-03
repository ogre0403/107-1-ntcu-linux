## ◎在 /etc/hosts 檔案，請找出
 ├>該檔案的 inode 號碼為幾號？ 
 │   Ans:16789384
> 想要看inode號碼的話要使用 ls 的子功能 "-i" 
  
 └>這個 inode 共有幾個檔名在使用？
 │   Ans:一個

> 需要"詳細"列出，所以要使用 ls 的子功能 "-l"  
![1](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-5/ACS107134/1.JPG)

## ◎建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出
 │    因為/etc/hosts有權限上的問題，一般使用者不能建立連結，需要切換到root才能操作
 
 ├>/srv/hosts.hard的 inode 號碼為幾號？
 │  Ans:16789384
> 想要看inode號碼的話要使用 ls 的子功能 "-i" 
 
 ├>這個 inode 共有幾個檔名在使用？
 │  Ans:兩個
> 需要"詳細"列出，所以要使用 ls 的子功能 "-l" 
 
 └>說明原因。

    實體連結是以多個檔案對應到同一個inode的方式建立的連結，所以會發現新檔案的inode會跟原檔案的一樣
![2](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-5/ACS107134/2.JPG)
      
## ◎建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出
 │    因為/etc/hosts有權限上的問題，一般使用者不能建立連結，需要切換到root才能操作
 
 ├>/srv/hosts.soft的 inode 號碼為幾號？
 │  Ans:51151208
> 想要看inode號碼的話要使用 ls 的子功能 "-i" 
 
 ├>這個 inode 共有幾個檔名在使用
 │   Ans:一個
> 需要"詳細"列出，所以要使用 ls 的子功能 "-l" 
 
 └>說明原因。

    符號連結跟實體連結不一樣，會另外占用一個inode跟空間。所以上述的inode只會有一個檔名
![3](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-5/ACS107134/3.jpg)
