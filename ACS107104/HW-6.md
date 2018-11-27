#請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。

*輸入vi ~/.bashrc

>新增檔案

*輸入i

>啟用編輯

*輸入HOSTS_PATH="/etc/hoats"

>新增變數

*按ESC鍵→:wq

>即可儲存並離開

*輸入source ~/.bashrc

>讀環境設定檔的指令

![image]()

*輸入cat $HOSTS_PATH

>查看有無成功

![image]()

---------------------------------------

#在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。

*輸入yum groupinstall "Development Tools"

>安裝gcc

*輸入'vi test.c'

>新增檔案

*輸入i

>啟用編輯

*輸入程式

![image]()

*輸入'gcc test.c'

>編譯

*輸入'./a.out'

>輸出結果

*輸入'echo $?'

>印出內容

![image]()

*沒有讀到HOSTS_PATH

>因為顯示'getenv() return NULL'

*$?的值為1

>錯誤

-----------------------------------
#在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。

*輸入'vi ~/.bashrc'

>編輯.bashrc

*輸入'export HOSTS_PATH=/etc/hosts'

![image]()

*輸入'source .bashrc'

*輸入'gcc test.c'

>編譯

*輸入'./a.out'

>輸出結果

*輸入'echo $?'

>印出內容

*有讀到HOSTS_PATH

>因為有顯示HOSTS_PATH

*$?的值為0

>正確

![image]()