# HW-6 第一題

## 這次使用個人筆電完成，因此截圖不同以往。

## 第一小題

>請在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts，(注意不需用export)，說明如何不登出讓HOSTS_PATH變數生效，執行cat $HOST_PATH確認有讀取到檔案內容。

![1](https://images2.imgbox.com/95/5c/JgDIFZJg_o.png)

首先用指令 **vi** 編輯 **.bashrc** 檔案。

![2](https://images2.imgbox.com/0b/5e/2XcNQntw_o.png)

輸入 **HOSTS_PATH=/etc/hosts** 的個人設定，按esc後輸入:wq儲存離開。

![3](https://images2.imgbox.com/b5/f5/2lk8a2pM_o.png)

接著使用指令 **source** 搭配設定檔.bashrc，即可在不登出的情況讓剛設定的變數生效。

![4](https://images2.imgbox.com/12/fd/zWOpTQnK_o.png)

接著輸入cat $HOSTS_PATH來確認設定是否成功。

## 第二小題

>在C語言程式可以用getenv()讀取LINUX的環境變數，範例程式如下。請在Linux裡編譯此範例程式並執行，請問否有讀到HOSTS_PATH以及$?的值為何，請說明。也許需透過yum groupinstall "Development Tools"安裝gcc。

![5](https://images2.imgbox.com/2e/48/YAuvHyxj_o.png)

首先確認ubuntu已經有gcc了。

![6](https://images2.imgbox.com/c9/3f/a9lxvbCk_o.png)

接著用vi創建新的c語言檔,並複製貼上程式碼,再用gcc編譯此檔案。

![7](https://images2.imgbox.com/75/d1/sRCsI0fV_o.png)

接著執行a.out檔,發現輸出爲getenv() return NULL，並執行指令 **$?** 觀察程式運行狀況，發現輸出爲 1 ，因為此程式碼的緣故(最後附上程式碼解釋)，所以判斷程式並未如預期正常執行。


程式無法正常執行原因：因為程式在執行時並未偵測到我新增的變數，因此依循程式碼給出錯誤訊息。而偵測失敗的根本原因則是因為我所新增的變數屬於個人設定，而非環境變數，因此無法分享給其他子程序(程式碼)使用。

![8](https://images2.imgbox.com/11/04/5UovJSsy_o.png)

解決方法是回到設定檔，加上指令 **export** 來讓變數成為環境變數。然後再用指令 **source** 使設定生效。可以使用指令 **export | grep HOSTS** 來確認設定是否生效。

![9](https://images2.imgbox.com/65/25/4AuBLLhc_o.png)

再次執行程式碼，結果正確輸出檔案內容。

## 程式碼解釋

### 第一小段




	const char *s=getenv("HOSTS_PATH");

	if(s==NULL){

		printf("getenv() return NULL);

		return 1;

	}



首先：函式 **getenv()** 輸入環境變數的名稱字串，則輸出字元型別指標，不同於putenv 或 setenv ，我們不能藉由此程式修改環境變數。如果名稱不存在於環境變數名單，則輸出null pointer。

因此當我們找不到變數，指標s會被設定為null，因而進入if述句中，並且映出錯誤訊息，然後回傳數值 1 結束這回合。


### 第二小段




	printf("HOSTS_PATH :%s\n",(s!=NULL)?s:"getnev returned NULL");

	printf("\n %s content is: \n",s);




分別代表正確輸出結果中的HOSTS_PATH : /etc/hosts和/etc/hosts content is:兩句話。
其中()?:的結果爲真，輸出s。


### 第三小段




	int c;

	FILE *file;

	file=fopen(s,"r");

	if(file){

		while((c=getc(file))!=EOF)

			putchar(c);

		fclose(file);

	}



簡單來說就是一個一個字元把檔案內容輸出。

一般來說FILE型別只能爲pointer，會因為fopen或tmpfile而自動指定位址。
利用函式fopen(const char *filename,const char *mode)回傳特定檔案的FILE pointer，並根據輸入對檔案執行動作，這次的程式碼是執行讀取功能。

file被指定後進入if述句。
函式getc(FILE*)回傳internal file position indicator所指向的字元(int)。在發生錯誤時或者檔案讀取完畢時回傳EOF，並設定不同的indicator。
將字元(int)存入c，用putchar函式輸出。
fclose函式結束檔案的關聯並且flush緩衝，如果成功關閉則回傳值爲 0 ，如果失敗則回傳值爲EOF。


