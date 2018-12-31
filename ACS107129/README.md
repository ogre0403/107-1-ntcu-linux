# HW-9

## 第一題

>yum 是透過設定檔的規範去找到安裝/升級伺服器，預設的 CentOS 7 的設定檔的檔名為 /etc/yum.repos.d/CentOS-Base.repo。Red Hat 提供了 EPEL 的計畫，提供額外打包好的軟體，提供給用戶使用。但這些軟體並非官網提供， 因此其軟體庫並沒有在預設的設定檔內。

*	請閱讀 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/ 後，依照其作法，啟用epel repo?isitory，並安裝htop

---------

根據 https://www.cyberciti.biz/faq/installing-rhel-epel-repo-on-centos-redhat-7-x/

![1](https://images2.imgbox.com/45/82/VPsUxBfL_o.png)
![2](https://images2.imgbox.com/0f/02/wC5PMm98_o.png)

### 使用指令: sudo yum install epel-release 

 **yum** 也可以加上參數 **-y** 來省略確認訊息
 
![3](https://images2.imgbox.com/f1/8e/xUtovSga_o.png)

### 使用指令: yum repolist

來refresh repo，並查看configured repositories

![4](https://images2.imgbox.com/34/0f/6FDZmrhb_o.png)
![5](https://images2.imgbox.com/51/56/aj6nAPlN_o.png)

epel 提供了尋找和查詢資訊的方法

![6](https://images2.imgbox.com/db/11/Aq0aiTsm_o.png)
![7](https://images2.imgbox.com/59/0e/uO7Gy9pn_o.png)

### 使用指令: sudo yum install htop

就可以用epel安裝htop

