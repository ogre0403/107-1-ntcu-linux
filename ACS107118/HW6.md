#作業6  
##問題1  
1. 使用 vi .bashrc 指令進行檔案編輯  
2. 使用 HOST_PATH="/etc/hosts"，再使用 source ~/.bashrc 讓它掛載上去  
3. 最後使用 cat $ HOSTS_PATH 指令確認是否有執行  
##問題2 
1. 先以 vi hw6.c 指令編寫程式，再以 gcc hw6.c 這隻指令來編譯這隻程式  
2. 用 ll hw6.c a.out 建立這個程式的執行檔，並用使用 ./a.out 這個指令執行程式(會發現結果不對)  
3. 使用 echo $? 這個指令發現程式沒有正確的執行  
4. 之後我們進 .bashrc 的檔案裏面,用 export HOSTS_PATH 把程式編譯上去，接下來使用 source ~/.bashrc 把它掛載上去  
5. 用 gcc hw6.c 指令編譯這個程式，再用 ll hw6.c a.out 建立這隻程式的執行檔  
6. 用 ./a.out 這個指令執行程式(結果終於正確了)  
7. 用 echo $? 這個指令後,結果是0,表示程式是正常執行的  
