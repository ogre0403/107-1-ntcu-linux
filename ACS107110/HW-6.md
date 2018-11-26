→vim .bashrc
→HOSTS_PATH="/etc/hosts"(建立變數)
(圖6-1)
→vim test.c (建立一個檔案)
→按i開始輸入
→輸入程式
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
→按esc跳出
→輸入:wq即可存檔離開
→輸入gcc test.c
→輸入./a.out
顯示:getnev() return NULL
→輸入echo $?
顯示:1
(如圖6-2)
→最後再進入vim .bashrc
→HOSTS_PATH="/etc/hosts"前面加入export
→輸入source .bashrc
→輸入echo $HOSTS_PATH
顯示:/etc/hosts
→輸入cat $HOSTS_PATH
如圖所示(6-3)
   	
