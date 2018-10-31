# HW-4



# 第一題



### 第一步



![1.1](https://images2.imgbox.com/70/49/jiKEyPxN_o.png)



>首先要建立兩個群組，利用**groupadd**的指令建立，並使用**grep group /etc/group**來查看是否成功建立。



![1.2](https://images2.imgbox.com/08/b0/yV817Reb_o.png)



>使用指令**useradd**來建立六個使用者，並加上 **-g** 的參數來指定各個使用者的initial group。



![1.3](https://images2.imgbox.com/3f/12/Uxzo7sO7_o.png)



>和**HW-3**的時候一樣，使用**echo password | passwd --stdin username**的指令設置密碼，關於其指令詳細在**HW-3**已經稍微提過，所以不再敘述一次了。



![1.4](https://images2.imgbox.com/55/7d/62QhEUBI_o.png)



>使用指令**mkdir**建立目錄並搭配 **-m** 的參數設定各種權限，再使用**chgrp**的指令變更擁有群組，最後使用**ll**指令檢查檔案屬性。



### 第二步



![1.5](https://images2.imgbox.com/6d/dc/eTKbWiov_o.png)



>使用**su**指令切換為myuser1的使用者，利用**cd**進入目錄/srv/myproject並使用**touch**指令建立myuser1.data檔案，再切換回root，然後使用**cp**將/usr/bin/ls的內容複製一份成/usr/local/bin/myls。



![1.6](https://images2.imgbox.com/0c/7d/79rRwQYu_o.png)



>切換回root，先使用**ll**檢查檔案屬性，再用**chmod**更改檔案屬性。其中，根據**HW-3**所學到的，我們知道**後三碼**為擁有者、擁有群組、其他人的rwx權限，而**三碼前面**再加**一碼**可以指定檔案的屬性成**SUID、SGID、SBIT**的屬性，**SUID=4**、**SGID=2**、**SBIT=1**，最後用**ll**檢查使用者的**x**是否變成**s**。



![1.7](https://images2.imgbox.com/69/1d/ZnFPgb41_o.png)



>切換使用者為nouser1，執行/srv/myproject，並且確認為可執行的。



# 第二題



![2.1](https://images2.imgbox.com/7f/e5/XC5r0NUV_o.png)



>使用指令**ps aux**列出所有的程序，再搭配 **|** 和 **grep**將有**rsyslog**關鍵字的程序找出來。


>確認後，將原本的指令加上 **>** 的指令以重新導向後方資料 **(此指令為建立新的或覆蓋)** ，最後利用**cat**指令確認檔案內容。



# 第三題



![3.1](https://images2.imgbox.com/54/be/r0jD4T0j_o.png)



>利用**find**指令搜尋資料並搭配 **-prem** 的參數來藉由指定檔案權限的方式搜尋，因為要搜尋的是**所有擁有SUID屬性的檔案**，因此搭配 **-prem /u=s** 的指令來搜尋兩個目錄。



![3.2](https://images2.imgbox.com/c8/fb/BSMRCXwg_o.png)



>指令型式為: **find  檔案  尋找方式的參數  提供尋找的資料  -exec/-ok  欲執行指令  {} \\;**



>接下來使用**find**的參數 **-exec** 和 **-ok** ，讓使用者可以對找到的檔案或目錄執行特定的指令，而 **{ }** 包著所找到的資料，**\\;** 用來完結動作。其中 **-exec** 和 **-ok** 的差別為: **-ok** 會要求使用者一項一項確認，而 **-exec** 則否。而我們希望執行**ls -l**的指令並且重新導向特定檔案。



>綜合起來，第一次使用 **find /usr/bin -perm /u=s -ok ls -l > findsuidsgid.txt {} \\;** 的指令，一項一項確認後接著第二次。第二次使用 **find /usr/bin -perm /u=s -ok ls -l 1>> findsuidsgid.txt {} \\;**的指令，差異在於將 **>** 更改為 **1>>** 的重新導向方式。



> **>** 和 **1>>** 的差別為: **>** 為建立或覆蓋，而 **1>>** 為覆蓋或累加，我們希望兩個都存在，所以使用累加。



![3.3](https://images2.imgbox.com/04/21/aQzVjcJw_o.png)



>最後使用**cat**指令檢查檔案內容。


