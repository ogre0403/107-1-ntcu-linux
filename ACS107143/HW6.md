### HW6

# 1

<ol>輸入"vi ~/.bashrc"，然後在最下面新增"HOSTS_PATH="/etc/hosts"(下面第一張圖)，然後輸入"source ~/.bashrc"，可以執行該腳本，然後輸入"cat $HOSTS_PATH"(第二張圖)。
</ol>

![1](1.jpg)

![2](2.jpg)

# 2

<ol>新增一個檔案"touch 檔名.c"，然後編輯並輸入git上的程式碼，指令是"vi 檔名.c"，編輯完之後輸入"gcc test.c"，然後執行"./a.out"，再輸入"echo $?"，得到值為1
<\ol>

> 說明：因為HOSTS_PATH是區域變數，不是全域變數，所以getenv沒有辦法讀到，會出現NULL，於是編譯並執行回傳了1。

![3](3.jpg)

# 3

<ol>在第一題編輯的檔案中"HOSTS_PATH="/etc/hosts"前面加上export，變成"export HOSTS_PATH="/etc/hosts"(下面第一張圖)，然後輸入"source ~/.bashrc"，這樣剛剛打出來的程式就可以讀到這個環境變數了(下面第二張圖)
<\ol>

![4](4.jpg)

![5](5.jpg)
