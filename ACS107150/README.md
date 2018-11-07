# 在 /etc/hosts 檔案，請找出

## 該檔案的 inode 號碼為幾號？

-   inode號碼為2115530

## 這個 inode 共有幾個檔名在使用？

-   由檔案連結數可知只有1個在使用

> ![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-5/ACS107150/1.PNG?raw=true)

# 建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，請找出

## /srv/hosts.hard的 inode 號碼為幾號？

-   inode號碼為2115530

## 這個 inode 共有幾個檔名在使用？

-   由檔案連結數可知有兩個在使用

## 說明原因。

-   因為建立實體連結inode不會改變
-   所以會多一個檔案使用來源檔的inode

> ![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-5/ACS107150/2.PNG?raw=true)

# 建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，請找出

## /srv/hosts.soft的 inode 號碼為幾號？

-   inode號碼為6312160

## 這個 inode 共有幾個檔名在使用

-   由檔案連結數可知只有1個在使用

## 說明原因

-   因為建立符號連結時會產生一個獨立的檔案
-   所以inode和來源檔不同

> ![github](https://github.com/JackyBigNose/107-1-ntcu-linux/blob/HW-5/ACS107150/3.PNG?raw=true)     
    