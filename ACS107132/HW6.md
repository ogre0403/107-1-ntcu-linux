##一.

#請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts
1. [vi ~/.bashrc]
2. 按i編輯，打上{HOSTS_PATH="/etc/hosts"}
3. 按Esc，打[:wq]儲存離開
+ [:p!]不儲存離開

#說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。
1. [source ~/.bashrc]，source可使變數不登出始生效(1.jpg)
2. [cat $HOSTS_PATH](2.jpg)

##二.

#在C語言程式可以用getenv()讀取LINUX的環境變數。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。
1. [vi program.c]
2. 輸入程式碼[:wq]儲存離開(3.jpg)
3. [gcc program.c]-[ll program.c a.out]-[./a.out]
4. 輸入[echo $?]值=1
5. 沒有讀到HOSTS_PATH，因為它不在子程序內

##三.

#在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。
1. [vi ~/.bashrc]
2. 按i編輯，打{export HOSTS_PATH}，按Esc，[:wq]儲存離開
3. [source ~/.bashrc]使變數不登出始生效
4. 再執行一次[gcc program.c]-[ll program.c a.out]-[./a.out]
5. 輸入[echo $?]值=0