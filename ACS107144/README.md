# 1. 關於連結檔的建置行為：
## 在/etc/hosts檔案，找出 inode號碼、有幾個檔名在使用該 inode號碼
* 輸入 `ls -ali /etc/hosts`
> 在權限前那串數字為 inode碼，在權限後的數字表示有幾個檔案在使用此 inode碼

  * inode 為 4237960
  * 只有一個檔名在使用該inode

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-5/ACS107144/5-1.png)

## 建立實體連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.hard，找出 inode號碼、有幾個檔名在使用該 inode號碼
* 輸入 `ln /etc/hosts /srv/hosts.hard`
> 建立實體連結
* 輸入`cd /srv`
> 進入 srv
* 輸入`ls`
> 確認實體連結成功建立於 srv
* 輸入 `ls -ali hosts.hard`
> 在權限前那串數字為 inode碼，在權限後的數字表示有幾個檔案在使用此 inode碼

  * inode 為 4237960
  * 有兩個檔名在使用該inode
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-5/ACS107144/5-2.png)

* 有兩個檔案共用同 inode 的原因
  * 實體連結是指向的實際文件的精確副本。實體連結和原文件共享相同的inode。
![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-5/ACS107144/5-3.png)

## 建立符號連結，原始檔案為 /etc/hosts 而新的檔案檔名為 /srv/hosts.soft，找出 inode號碼、有幾個檔名在使用該 inode號碼
* 輸入 `ln -s /etc/hosts /srv/hosts.soft`
> 建立符號連結
* 輸入 `ls -ali hosts.hard`
> 在權限前那串數字為 inode碼，在權限後的數字表示有幾個檔案在使用此 inode碼

  * inode 為 6354901
  * 只有一個檔名在使用該inode

* 只有一個檔案使用此 inode 的原因
  * 符號連結會產生一個獨立的檔案，所以會有自己的 inode

![image](https://github.com/KAORIKOU/107-1-ntcu-linux/blob/HW-5/ACS107144/5-4.png)



