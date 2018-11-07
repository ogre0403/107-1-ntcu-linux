# HW-5

# 第一題

### 第一步

![1.1](https://images2.imgbox.com/38/d2/FekxpOji_o.png)

>首先使用**ls**指令搭配參數 **-i** 列出檔案的inode，並配合 **-l** 參數列出詳細資料。

此檔案的inode為上圖**紅框**所示的 **4235656**，而**橘框**則顯示的則是 **有多少個檔名連接到此inode** ，因此我們知道此inode只有一個檔名使用。

### 第二步

![1.2](https://images2.imgbox.com/d2/16/rpb3If5f_o.png)

>使用**ln**指令建立來源檔: **/etc/hosts** 的**hardlink** 於目的檔: **/srv/hosts.hard**，並配合 **ls **和參數列出此檔。

紅框顯示出/srv/hosts.hard檔的inode為**4235656**，其中，之所以和/etc/hosts檔的inode相同是因為**hardlink**的特性。**hardlink**是**在某目錄下新增一筆檔名連到其inode號碼的關連記錄**。

而橘框顯示此同一inode的連接檔名由1筆便成2筆，是因為**hardlink**的關係而多了一筆檔名連接到同inode。

**hardlink**的簡單運作示意圖如下:

![1.3](https://images2.imgbox.com/f1/e9/eXiArIU6_o.png)

![1.4](https://images2.imgbox.com/f1/4d/llFchWiw_o.png)

>使用指令 **ln** 搭配參數 **-s** 來建立 **Symbolic link** ，並配合 **ls** 和其參數列出檔案。

紅框顯示出/srv/hosts.soft連結檔( **l**rwxrwxrwx )的inode為 **6370784** ，不同於/etc/hosts的**4235656** ，因為**Symbolic link**會**建立一個獨立的檔案**，而這檔案會讓資料的讀取指向他link的那個檔案檔名，**建立獨立檔案**本身是要使用一組新的inode，因此此連結檔的inode不同於原本檔案的inode。

而/srv/hosts.soft為連結檔且為新建立的，因此橘框顯示出此inode指有一筆檔名連接。

另外，**綠框**表示連結檔大小為10bytes，因為**藍框**檔名 **/etc/hosts** 共十個字，而每個字佔用1bytes，因此共用了10bytes。

**Symbolic link**的簡單運作示意圖如下:

![1.5](https://images2.imgbox.com/0c/dd/BXzlx6Au_o.png)