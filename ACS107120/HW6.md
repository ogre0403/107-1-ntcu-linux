# 第一題

1. 在家目錄下的.bashrc裡新增一個shell變數 HOSTS_PATH=/etc/hosts

  vim .bashrc
  HOSTS_PATH="/etc/hosts"
  esc離開編輯模式

2. 如何不登出讓HOSTS_PATH變數生效
  
  source .bashrc
  
3. 執行cat $HOST_PATH確認有讀取到檔案內容

  cat $HOSTS_PATH
  
4. 在Linux裡編譯此範例程式並執行
  
  vim test.c
  
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
  
  
  gcc.test.c
  
  ./a.out
  
5. 請問是否有讀到HOSTS_PATH以及$?的值為何
  
  否，因為變數不在子程序裡
  
  $?=1
  
6. 在.bashrc裡要如何修正，讓C語言程式可以讀到環境變數並將檔案內容顯示
  
  用export將變數放入子程序
  
  vim .bashrc
  
  export HOSTS_PATH="/etc/hosts"
  
  source .bashrc
  
  gcc.test.c
  
  ./a.out
  
  $?=0代表成功
