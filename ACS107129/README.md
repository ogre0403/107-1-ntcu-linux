# 期中考



## 第一題



### 第一小題

>設定 ver 變數，內容為『 my kernel version is 3.xx 』，其中 3.xx 為 uname -r 輸出的資訊，並顯示出ver變數的值。(10%)



---

打出這樣的指令: ver="my kernel version is \`uname -r\`"

---


其中等號兩邊無空白且變數內的額外指令要加上反單引號。

實作結果: **my kernel version is 3.13.0-107- generic**




### 第二小題

>請顯示目前PATH環境變數的值為何，並說明PATH的功用為何? (10%)



---

使用指令: echo $PATH

---


就可以查看PATH變數的內容，其中PATH的大小寫嚴格區分。

變數PATH的功能為執行檔搜尋的路徑，執行檔/指令的搜尋是依PATH變數內的路徑依序查詢。


## 第二題



### 第一小題

>有一個檔案的屬性權限為 `drwxrwsr-x 3 root mail 4096 2月 16 2017 mail/`，請說明此檔案的特性。(10%)


首先第一行英文字串中，**第一個字母**代表檔案屬性，其中**d**代表目錄檔。
而後九個英文字母為三個三個一組，前面三個代表**擁有者**的權限，由前到後分別為**r:讀取** // **w:寫入** // **x:執行**，有英文字母代表有此權限，而 **-** 則代表沒有此項權限。依此類推，中間三組為**檔案所屬群組**的權限，後三組則是**第三方**的權限，即非擁有者也非檔案所屬群組織使用者。


接著向後一項一向看，數字 **3** 代表此檔名的**inode**所連接的檔名總數。
接著**root**代表此檔案擁有者。
**mail**代表此檔案所屬群組。**4096**代表檔案大小。
**日期**代表檔案最後修改時間。



### 第二小題
>假設有一個script.sh檔案的權限為`-rw-r--r--`，若希望讓`所有人`可以執行該檔案，請問該如何下達指令？請使用數字法與符號法各操作一次。(10%)



數字法:


---

輸入指令: chmod 755 script.sh 

---


r為4、w為2、x為1
因此輸入755



符號法:


---

輸入指令:chmod u+x g+x o+x script.sh

---


代表增加執行權限



## 第三題



### 第一小題

>說明實體連結與符號連結的差異。(10%)


**hardlink**不會創建新檔案，因此使用的是和連結檔案相同的inode，且不可以跨越檔案系統連結。

**symboliclink**會創建新檔案，使用一組新的inode，可以跨越檔案系統連接。

### 第二小題
>在家目錄下建立一個檔名為 hosts.real 的實體連結指到 /etc/hosts？ (請用相對路徑表示家目錄) (5%)

---
使用指令:ln /etc/hosts ~/host.real
---

### 第三小題
>在家目錄下建立一個檔名為 hosts.symbo 的符號連結指到 /etc/hosts？ (請用相對路徑表示家目錄 (5%)

---
使用指令:ln -s /etc/hosts ~/hosts.symbo
---

## 第四題

>建立一個容量為1GB的xfs檔案系統，每次開機都能夠自動的掛載到 /srv/maildir，且該目錄是給 mailgroup 這個群組共用的，其他人不可具有任何權限。再建立一個名為mailuser的帳號，並加入 mailgroup 群組，且此帳號不可使用shell登入系統。

### 第一小題

![1](https://images2.imgbox.com/53/ec/nHSliPeU_o.png)

### 第二小題

![2](https://images2.imgbox.com/56/95/wHKK3aOE_o.png)

### 第三小題

![3](https://images2.imgbox.com/3d/d9/mfk5K68K_o.png)

### 第四小題

![4](https://images2.imgbox.com/b3/e5/n2srKDVX_o.png)

### 第五小題

![5](https://images2.imgbox.com/01/a2/RuEb62FE_o.png)