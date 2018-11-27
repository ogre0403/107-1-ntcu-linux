首先利用**vi** 編輯　**.bashrc**　檔案

![image](https://github.com/freshdiefish/107-1-ntcu-linux/blob/HW-6/ACS107125/1.jpg)

此時，我們使用指令**source** 就可以在不登出的情況下使變數生效

![image](https://github.com/freshdiefish/107-1-ntcu-linux/blob/HW-6/ACS107125/2.jpg)

使用**cat $HOST_PATH** 確認變數內容

![image](https://github.com/freshdiefish/107-1-ntcu-linux/blob/HW-6/ACS107125/3.jpg)

如果系統裡沒有gcc，可先執行**yum groupinstall "Development Tools"** 安裝它

利用**vi**創建檔案並貼上以下程式碼

    #include <stdio.h>
    #include <stdlib.h>

    int main(){
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


執行**gcc _(檔名)_.c**編譯後執行 **./a.out**

發現**getenv() return NULL**

再用**echo $?** 查看上個指令的回傳值(也就是我們code的回傳值)為ruturn 1

![image](https://github.com/freshdiefish/107-1-ntcu-linux/blob/HW-6/ACS107125/4.jpg)

可以得知程式讀取不到我剛剛新增的變數

why?因為 **$HOSTS_PATH**為區域變數而非環境變數，無法給其他的程式進行使用

我們回到第一步編輯　**.bashrc**　檔案

在我們的變數宣告行頭加上**export**宣告此為環境變數

再使用**source**讓設定生效

執行 **./a.out**可以確認**getenv()**抓到了我們設定的變數

最後**echo $?** 由程式碼可知成功執行完此檔案，回傳值為0

![image](https://github.com/freshdiefish/107-1-ntcu-linux/blob/HW-6/ACS107125/5.jpg)