### 1.安裝EPEL repo 
+ yum install epel-release
+ (如圖1、2)

### 2.查看epel repo 
+ yum repolist
+ (如圖3)

### 3.列出名為epel的repo下的所有可用安裝包
+ yum --disablerepo="*" --enablerepo="epel" list available
+ (如圖4)

### 4.搜尋htop安裝包 
+ yum search htop
+ (如圖5)

### 5.列出更多有關htop的信息 (如圖6)
+ yum info  htop
+ (如圖6)

### 6.安裝htop (如圖7、8)
+ yum install  htop
+ (如圖7、8)