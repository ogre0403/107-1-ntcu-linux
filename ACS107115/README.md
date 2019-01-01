#homework09  
##q1  
###yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。  

請閱讀 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，依照其作法，啟用epel repo�isitory，並安裝htop  
###流程  
 - 首先找到他的網站(圖9-1)  
   (**大概看一下流程**)  
 - 用 yum install epel-release 指令下載封包(圖9-2,圖9-3)  
 - 用 cd /tmp 這隻指令跳轉資料夾  
 - 用 wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm 下在檔案到指定資料夾  
 - 用 ls rpm 這隻指令確認版本(圖9-4)(**前面兩個步驟的截圖我沒有截到**)  
 - 用 yum repolist 這隻指令安裝 repolist(圖9-4)  
 - 用 yum --disablerepo="*" --enablerepo="epel" list available 安裝(圖9-5)  
 - 接下來要安裝 htop  
 - 用 yum search htop 下載,找到檔案(圖9-6)  
 - 用 yum info htop 下載,找到更多資訊(圖9-7)  
 - 用 yum install htop 下載,安裝 htop(圖9-8)  