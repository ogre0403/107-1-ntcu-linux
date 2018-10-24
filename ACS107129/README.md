# Linux HW-3

# 第一題



### 第一小節



![1.1](https://images2.imgbox.com/c3/ac/lFYS3RYd_o.png)



>首先要建立三個帳號，利用**useradd**的指令建立。

>建立密碼以**echo password | passws --stdin username**的指令進行，因為顯示出密碼是這次的要求，這指令可以大量設定密碼，但顯示密碼同時也是這個指令的風險/壞處所在。



### 第二小節



![1.2](https://images2.imgbox.com/59/0b/gPPOC77D_o.png)



>接著利用**ls / ls -l / ll**等等的指令確認家目錄的建立，再用**userdel -r**的指令刪除**examuser3**，然後再利用指令確認/home和/var/spool/mail的內容。



### 第三小節



![1.3](https://images2.imgbox.com/d3/33/rYUYHIq9_o.png)



>利用**userdel**的指令刪除**examuser1**並且重新確認/home和/var/spool/mail的內容。



![1.4](https://images2.imgbox.com/1e/a1/odL1kzQQ_o.png)



>為了用相同的UID重建被刪除的帳號，使用**useradd -u**的參數來以指定UID的方式創建帳號，並加入 **-U** 的參數來建立和帳戶相同的群組。
>在確認帳號UID相同之後，再以上述**echo password | passwd --stdin username**的指令設定密碼即可。



# 第二題



### 第一小節



![2.1](https://images2.imgbox.com/95/28/R2jWhLiR_o.png)



>這次嘗試使用**useradd -p**的指令以直接設定密碼為123的方式建立使用者。

>接著使用**cp  檔案來源  複製目的地**的指令複製一份檔案到/home/examuser4裡，並注意此時examuser4對於這份複製的檔案屬於other的分類且沒有任何權限。


![2.2](https://images2.imgbox.com/3a/37/qEVvsHsu_o.png)



>先利用**chown**的指令將examuser4改成這份複製檔案的擁有者，再利用**chmod**的指令配合數字法將擁有者的權限由 **6(rw-)** 提升至 **7(rwx)** 。



###第二小節



![2.2](https://images2.imgbox.com/59/35/4EVL0h7R_o.png)

>利用**mkdir**的指令建立名為exmadata的目錄，接著再examdata內利用**touch**的指令建立一份空的change.txt檔案。



![2.3](https://images2.imgbox.com/81/08/lWRbuKwf_o.png)



>利用**chown**的指令更改檔案擁有者為**sshd**，接著利用**grep users /etc/group**的指令確認users的群組是否存在。

>接著利用**chgrp**的指令變更檔案的群組，用**chmod**的指令將權限改為640的狀態，再利用指令確認檔案的屬性。



![2.4](https://images2.imgbox.com/9f/b4/frVrUmuy_o.png)



>最後利用**touch -t**的指令修改時間，由前到後分別為**西元年 月 日 小時 分 秒**。


# 第三題



### 第一小節



![3.1](https://images2.imgbox.com/03/8b/KdoBLXj9_o.png)



>首先將表格的檔案和目錄建立起來，重複利用**chmod / mkdir / cp **三種指令。



![3.2](https://images2.imgbox.com/60/cc/ubFL5Tit_o.png)



>接著確認各項屬性和表格上一致。

### 第二小節



![3.3](https://images2.imgbox.com/6e/2c/AYG2K7zP_o.png)



>先利用**su**的指令將身分由**root**切換回**一般使用者(shimakaze)**，接著輸入 **ls -l /dev/shm/unit05/dir[1-4]** 的指令並觀察現象。

首先我們發現**檔案1**和**目錄2**無法成功顯示出來，接著比較各個目錄之間還有檔案之間的權限，再配合錯誤發生時所提供的英文提示，我們可以推測**檔案1**之所以無法顯示是因為**dir1**對於**shimakaze**而言為不可執行的，導致我們只可停留在能讀取**dir1**的情形；而第二號甚至連**檔案2**都沒出現是因為**dir2**對於**shimakaze**而言是不可讀取的目錄，既然不可讀取就不用提更深入的事情了。



### 第三小節



![3.4](https://images2.imgbox.com/97/aa/AgvFm4pK_o.png)



>利用指令依序執行四個項目。

在四個目錄當中只有**dir1**對於**shimakaze**而言為不可執行的，因此沒有路徑可以抵達目錄內的檔案。而其他三個通過目錄後，內部的檔案對於**shimakaze**而言皆是可讀取的，其中**file4**是因為處於**dir4**的架構中，而非本身屬性。

### 第四小節



![3.5](https://images2.imgbox.com/14/35/eIR6YMYr_o.png)
![3.6](https://images2.imgbox.com/57/02/LOByRp0Q_o.png)

![3.7](https://images2.imgbox.com/89/57/2XFtE0AC_o.png)



>利用指令進入文字編輯模式

發現**file1**是唯讀檔案，並不能藉由強制儲存退出來更動內容。因為**file1**對於**shimakaze**而言為不可改寫的。



![3.8](https://images2.imgbox.com/06/b0/HQtEak73_o.png)

![3.9](https://images2.imgbox.com/74/b9/Z4yrCTYQ_o.png)



發現**file2**也是跟**file1**有相同情形，強制也沒用。



![3.10](https://images2.imgbox.com/08/81/Pe22pXod_o.png)

![3.11](https://images2.imgbox.com/3c/a5/92Qqe3or_o.png)



**file3**本身對**shimakaze**而言是可改寫的，因此可以正常的更動內容。



![3.12](https://images2.imgbox.com/4f/33/n3T44PKE_o.png)

![3.13](https://images2.imgbox.com/7b/63/ZlTcFMqD_o.png)

![3.14](https://images2.imgbox.com/bb/a2/jsNpLJ8j_o.png)



**file4**對於**shimakaze**而言是不可改寫的，因此正常儲存無法更動其內容。但是因為**file4**位於**dir4**架構中，而**dir4**對於**shimakaze**而言是可改寫的，因此我們可以用強制執行儲存離開來更動**file4**的內容。