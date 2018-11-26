### 請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，

### 說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。
    使用 vi 編輯進入 .bashrc 檔
    之後使用source filename 來不登出讓更改生效
![1](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-6/ACS107134/1.PNG)

### 在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。

### 請在Linux裡編譯此範例程式並執行，請問是否有讀到HOSTS_PATH以及$?的值為何，請說明。

### 也許需透過yum groupinstall "Development Tools"安裝gcc。


    #include <stdio.h>
    #include <stdlib.h>
    int main()
    {
        const char* s = getenv("HOSTS_PATH");
        if(s == NULL){
            printf("getenv() return NULL\n");
            return 1;
        }
        
        printf("HOSTS_PATH :%s\n",(s!=NULL)? s : "getenv returned NULL");
        printf("\n %s content is: \n", s);
    
        int c;
        FILE *file;
        file = fopen(s, "r");
        if (file) {
            while ((c = getc(file)) != EOF)
                    putchar(c);
            fclose(file);
        }
    }

### 在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。

#### (1).
##### 編譯 #    : gcc file.c  一定要.c
##### 執行 #    : ./檔案
> Ans : 無法透過 ` getenv() `讀到變數 *HOSTS_PATH*的值。
> 雖然沒有讀到傳回值但對程式來說判斷 *s* 為 NULL 有成立，所以 *$?* 有傳回值 1。

#### (2).
    我不會