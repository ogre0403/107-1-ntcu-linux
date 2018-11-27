#Homework 6

###1.  
首先需要使用 **vi** 這個指令  
使用 **vi** 進入 **.bashrc** 編輯  
在最底下加入 **HOSTS_PATH="etc/hosts"**  
然後使用 **:wq** 退出並儲存  
接著使用 **source ~/.bashrc** 使此修改生效  
然後用 **cat $HOSTS\_PATH** 確認有沒有讀到檔案內容   
(那兩個\_ _讓字體變斜真的弄超久才發現是他們害的= =，查到最後才發現要用反斜來讓特殊符號無效)
  
  
首先要先安裝gcc，因為後面需要用到  
要使用 **yum groupinstall "Development Tools"** 來安裝gcc  
有了gcc之後就可以來編譯程式  
用 **gcc HW6.c**   
接著使用 **./a.out**  
然後使用 **echo $?** 這時會發現程式的值為1 
  
所以這時需要用 **vi** 進入 **.bashrc** 裡編輯  
然後一樣在最底下多加入一行 **export HOSTS_PATH**  並使用 **:wq** 儲存並退出  
接著同樣使用 **source ~/.bashrc** 使此修改生效  
  
然後重新 gcc  
然後再次使用 **./a.out** 就會發現程式是我們想要的了!  
  
  
  
  
  

  
