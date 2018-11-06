## HW5_關於連結檔案的建置行為


使用 **-i** 的參數來列出 _etc/hosts_ 的inode資訊

我們可以發現inode號碼為**4213160**

且目前使用此號碼的檔案只有一個

![image]("https://github.com/freshdiefish/107-1-ntcu-linux/blob/HW-5/ACS107125/5_01.png")

然後我們使用ln指令建立一個**實體連結(Hard link)** 新檔名為 _/srv/hosts.hard_

結果inode號碼和原本的檔案 _/etc/hosts_相同，且後面的連結數也變為了"**2**"

這是因為實體連結為建立一個inode、檔案屬性和原本檔案相同的新檔案

而新舊檔案連結一樣的inode指向block裡的資料，可以拿來當備份的功能

![image]("https://github.com/freshdiefish/107-1-ntcu-linux/blob/HW-5/ACS107125/5_02.png")

再來，我們使用ln並加上 **-s** 參數表示建置一個 **符號連結(Symbolic Link)**

如下圖顯示inode號碼為**13017241**，連結數為"**1**"

這個就相對好理解多了，可以把它想成在 _Windows_ 環境底下的**捷徑** 

新檔案 _/srv/hosts.soft_所含的資料內容為**讀取檔名 _/etc/hosts_**

 因為擁有不同的資料內容，故作為獨立的兩檔案擁有不同的inode號碼

![image]("https://github.com/freshdiefish/107-1-ntcu-linux/blob/HW-5/ACS107125/5_03.png")