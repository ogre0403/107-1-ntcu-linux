1.Install Extra Packages for Enterprise Linux repository configuration:

輸入yum install epel-release來安裝(圖1 2)

2.List your new repos:

輸入yum repolist查看(圖3)

3.Search and install package:

輸入yum --disablerepo="*" --enablerepo="epel" list available搜尋和安裝(圖4)

4.輸入yum search htop，搜尋htop(圖5)

5.輸入yum info htop，獲取更多訊息(圖6)

6.輸入yum install htop，安裝htop(圖7 8 9)