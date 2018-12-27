### 1.安裝EPEL repo 
+ yum install epel-release
![image](https://github.com/gigilin7/107-1-ntcu-linux/blob/HW-9/ACS107106/1.png)
![image](https://github.com/gigilin7/107-1-ntcu-linux/blob/HW-9/ACS107106/2.png)

### 2.查看epel repo 
+ yum repolist
![image](https://github.com/gigilin7/107-1-ntcu-linux/blob/HW-9/ACS107106/3.png)

### 3.列出名為epel的repo下的所有可用安裝包
+ yum --disablerepo="*" --enablerepo="epel" list available
![image](https://github.com/gigilin7/107-1-ntcu-linux/blob/HW-9/ACS107106/4.png)

### 4.搜尋htop安裝包 
+ yum search htop
![image](https://github.com/gigilin7/107-1-ntcu-linux/blob/HW-9/ACS107106/5.png)

### 5.列出更多有關htop的信息 (如圖6)
+ yum info  htop
![image](https://github.com/gigilin7/107-1-ntcu-linux/blob/HW-9/ACS107106/6.png)

### 6.安裝htop (如圖7、8)
+ yum install  htop
![image](https://github.com/gigilin7/107-1-ntcu-linux/blob/HW-9/ACS107106/7.png)
![image](https://github.com/gigilin7/107-1-ntcu-linux/blob/HW-9/ACS107106/8.png)
