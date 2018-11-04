# HW5
---------------------------------
## 關於連結檔案的建置行為:


---------------------------------
### 在 /etc/hosts 檔案，請找出


> 利用`` ls -ali 檔案名稱  ``找尋inode號碼。
> > **ls -ali**最前面的數值即為inode號碼。
> > > **-a**:全部的檔案，連同隱藏檔( 開頭為 . 的檔案) 一起列出來。

> > > **-l**:長資料串列出，包含檔案的屬性與權限等等資料。

> > > **-i**:列出 inode 號碼。

> > > > **-ali**為** -a **、**-l**、**-i**的組合。


* 該檔案的 inode 號碼為幾號？


**2129800**


* 這個 inode 共有幾個檔名在使用？


**1**


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-5/ACS107109/HW5img/1-1.png)


---------------------------------
### 建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出


> 利用`` ln /etc/hosts /srv/hosts.hard ``建立實體連結。
> > **ln 實體目錄或檔案 連結的目錄或檔案**:連結檔案或目錄。
> > > 將`` /etc/hosts ``連結至`` /srv/hosts.hard ``。

> 再利用`` ll -i /etc/hosts /srv/hosts.hard ``查找檔案相關資訊。
> > **-i**:列出 inode 號碼。
> > > 會發現其兩個檔案名稱使用同一個inode號碼(連結數:2)。


* /srv/hosts.hard的 inode 號碼為幾號？


**2129800**


* 這個 inode 共有幾個檔名在使用？


**2**


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-5/ACS107109/HW5img/2-1.png)


* 說明原因


因為每個目錄底下都有`` . ``的檔案名稱，並且`` . ``又代表為目錄自己，所以**目錄本身會有兩個檔案名稱跟隨自己**，反之，**會有兩個檔案名稱連結至相同的inode號碼**。
> 因此，其inode號碼會有兩個檔案名稱在使用。

> **hard link**
> >每個檔案都會使用一個inode，檔案的內容由inode之記錄來指向。因此，想要讀取其檔案時，須經由目錄記錄的檔案名稱指向正確的inode號碼才可以讀取。
> > > 多個檔案名稱可以對應到同一個inode號碼。

> **inode 與 block 都沒有改變。**


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-5/ACS107109/HW5img/2-2.png)


---------------------------------
### 建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出


> 利用`` ln -s /etc/hosts /srv/hosts.soft ``建立Symbolic link。
> > **ln -s 真實目錄或檔案 連結的目錄或檔案 ``:連結檔案或目錄。
> > > **-s**:提供 symbolic line 的連結。
> > > > 將`` /etc/hosts ``連結至`` /srv/hosts.soft ``。

> **同第一題的步驟查找inode號碼以及共有幾個檔名在使用**。
> > 利用`` ls -ali 檔案名稱  ``找尋inode號碼。
> > > **ls -ali**最前面的數值即為inode號碼。
> > > > **-a**:全部的檔案，連同隱藏檔( 開頭為 . 的檔案) 一起列出來。

> > > > **-l**:長資料串列出，包含檔案的屬性與權限等等資料。

> > > > **-i**:列出 inode 號碼。
> > > > > **-ali**為** -a **、**-l**、**-i**的組合。


* /srv/hosts.soft的 inode 號碼為幾號？


**309227**


* 這個 inode 共有幾個檔名在使用


**1**


![image](https://github.com/YANGshujun1110/107-1-ntcu-linux/blob/HW-5/ACS107109/HW5img/3-1.png)


* 說明原因


因為其為建立**單一的獨立新檔案**，且此檔案會使**資料讀取時直接指向其link中的檔案內容**。
> 因此，其inode號碼只會有一個檔案名稱在使用。

> **symbolic link**

> **inode 與 block 會改變。**
> >會佔用掉 inode 與 block。


-----------------------------------------
#### 補充:


* 由於每一台電腦的不同，所以每個人的inode號碼會不太一樣。
* 如果ln不加任何參數，其就屬於實體連結(hard link)。
