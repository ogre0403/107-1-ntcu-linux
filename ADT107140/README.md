#1


vim ~/.bashrc   


i ->  HOSTS_PATH=/etc/hosts(不需加export)   ->  esc : wq

![](./1.PNG)

source ~/.bashrc


cat $HOSTS_PATH


![](./3.PNG)



#2


yum groupinstall "Development Tools"

vim test.c

![](./4.PNG)

gcc test.c
 
./a.out         讀不出來

echo $為1       返回值是0，就是執行成功,返回值是0以外的值，就是失敗

![](./5.PNG)

#3


vim ~/.bashrc

i -> export HOSTS_PATH (記得加export)->  esc :wq

![](./6.PNG)

source ~/.bashrc

gcc test.c

./a.out

![](./9.PNG)

echo $?為0代表成功了

![](./8.PNG)




