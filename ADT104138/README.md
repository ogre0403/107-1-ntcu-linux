# HW6
## ADT104138 羅苡倫
*****
## 一、依下列描述完成並說明各項問題：
*	請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。</br>

利用vi ~/.bashrc 指令，更改裡面的內容，增加變數</br>
![新增](https://i.imgur.com/UYj9J0V.jpg)</br>

要讓變數立即生效，則可以使用source ~/.bashrc 或者 . ~/.bashrc，此兩種指令皆相同。最後再執行cat $HOST_PATH確認內容。</br>
![新增](https://i.imgur.com/GNqqUh6.jpg)</br>
![新增](https://i.imgur.com/Byzjywz.jpg)</br>

*	在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。</br>

先用touch 建立一個.c檔案，輸入指令 vi 撰寫範例程式。再安裝gcc 輸入指令編譯並執行。</br>
![新增](https://i.imgur.com/QUkRK8z.jpg)</br>

會發現return NULL，且$?回傳1，代表並沒有讀取到範例程式裡的s變數。</br>
![新增](https://i.imgur.com/q4zeZmt.jpg)</br>


*	在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。</br>

若要變數在其他子程序執行，則需要在變數前面加入 export 使之變成環境變數。</br>
如下圖，參考自鳥哥的LINUX私房菜</br>
![新增](https://i.imgur.com/3ZZdqp7.jpg)</br>

實作</br>
![新增](https://i.imgur.com/5sJmiDj.jpg)</br>
![新增](https://i.imgur.com/Zko0p3m.jpg)</br>

# 參考資料：[點擊這裡](http://linux.vbird.org/linux_basic/0320bash.php#source "參考資料")
# 感謝觀看 The End
