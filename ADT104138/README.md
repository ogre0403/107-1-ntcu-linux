# HW9
## ADT104138 羅苡倫
*****
## 一、yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。
*	請閱讀 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，依照其作法，啟用epel repo�isitory，並安裝htop</br>

依照題目要求，先啟用Epel擴充套件庫。因此，先執行指令yum install epel-release。</br>
![新增](https://i.imgur.com/VZGDPEc.jpg)</br>
![新增](https://i.imgur.com/OGuPlvP.jpg)</br>

安裝完成後，即可開始安裝htop這個系統狀態監控工具，輸入指令yum install htop即可達成目的。</br>
![新增](https://i.imgur.com/24DdnTc.jpg)</br>

輸入htop指令檢查。</br>
![新增](https://i.imgur.com/rGE9q07.jpg)</br>
![新增](https://i.imgur.com/9DLCaIW.jpg)</br>

# 參考資料：[點擊這裡](https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ "參考資料")
# 感謝觀看 The End
