###  Shell 基礎認識
## shell 變數
1. 在家目錄下的 `.bashrc` 裡新增一個shell變數 `HOSTS_PATH=/etc/hosts`
  *  `HOST_PATH=/etc/hosts`
2. 不登出變數即生效 
  *  `source ~/.bashrc`
3. 檢視
  *  `cat $HOST_PATH`

## Linux下的c語言
1. 範例程式 `test.c`

  ```
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

  ```

  *  `gcc -o test test.c`
  *  `./test`
       `getenv() return NULL`
    -  未查到HOSTS_PATH
  *  `$?`
    -  `bash: 127:command not found`
  *  `echo $?`
    -  `1`

## 讀到環境變數並將檔案內容顯示
1. `export HOST_PATH="/etc/hosts"`
   `source ~/.bashrc`
   `cat $HOST_PATH`
   `gcc -o test test.c`
   `./test`

   ```
   HOSTS_PATH :/etc/hosts
   
   /etc/hosts contest is:
   127.0.0.1  localhost localhost.localdomain localhost4 localhost4.localdomain4
   ::1        localhost localhost.localdomain localhost6 localhost6.localdomain6
   ```

   *  因為該變數在其他的子程序之下，須以export來使變數變成環境變數