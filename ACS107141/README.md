### HW6

# 1.請在家目錄下的```.bashrc```裡新增一個shell變數```HOSTS_PATH=/etc/hosts```，(注意不需用export)，說明如何不登出讓```HOSTS_PATH```變數生效，執行```cat $HOST_PATH```確認有讀取到檔案內容。

 * 輸入```vi ~/.bashrc```開啟編輯檔案
> 按下```a```,```i```,```o```即可開始編輯。 
 * 輸入```HOST_PATH="/etc/hosts```
> 按下```esc```並輸入```:wq```，即儲存離開。
![](https://i.imgur.com/nF9tMXn.png)

 * 輸入```source ~/.bashrc```執行環境設定檔指令
 * 輸入```cat $HOSTS_PATH```驗證是否讀取成功
 ![](https://i.imgur.com/JbzMk59.png)


# 2.在C語言程式可以用```getenv()```讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到```HOSTS_PATH```以及```$?```的值為何，請說明。也許需透過```yum groupinstall "Development Tools"```安裝gcc。

 * 輸入```yum groupinstall "Development Tools```安裝gcc。
> 如果出現```cannot find a valid baseurl for repo base/7/x86_64```要先連上網路
 * 輸入```vi cprogram.c```輸入下面程式碼，並按下```esc```輸入```:wq```儲存離開 
>  ```	#include <stdio.h>
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
		}```
 * 輸入```gcc cprogram.c```編譯
 * 輸入```gcc -c cprogram.c```
 * 輸入```ll cprogram*```會看到:
![](https://i.imgur.com/7pVvqnB.png)
 * 輸入```gcc -o cprogram cprogram.o```產生執行檔
 * 輸入```ll cprogram*```會看到:
![](https://i.imgur.com/tskpEr5.png)
 * 輸入```./cprogram```執行
> 出現```getenv() returrn NULL```。 
 * 輸入```echo $?```
> 其值為```1```。 
>	>```HOSTS_PATH```為區域變數，而非全域變數，所以```getenv```無法讀到，會出現```NULL```，於是編譯並執行回傳了```1```。

# 3.在```.bashrc```裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示。
 * 輸入```vi~/.bashrc```，編輯改為```export HOSTS_PATH```
> 按下```esc```並輸入```:wq```，即儲存離開。 
 * 輸入```source ~/.bashrc```令指令生效
 * 輸入```./cprogram```執行並輸入```echo $?```結果如下
![](https://i.imgur.com/SKKrAfb.png) 
  

