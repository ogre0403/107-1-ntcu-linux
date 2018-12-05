### HW6

1.<br/>
(1)輸入vi .bashrc，進去後在最下面一行加上HOSTS_PATH=/etc/hosts<br/>
![01](HW6/01.png)<br/>
使用source ~/.bashrc，讓變數不登出就能生效<br/>
最後用cat去呈現<br/>
![02](HW6/02.png)<br/>
(2)輸入vi test.c，進去後打上範例程式碼<br/>
![03](HW6/03.png)<br/>
用g++ -c -o 去compiler程式碼，compiler完後用./執行<br/>
最後得到NULL及1，因為HOSTS_PATH是區域變數<br/>
![04](HW6/04.png)<br/>
(3)要讓變數在其他子程序執行，需要在變數前面加入export使變成環境變數<br/>
![05](HW6/05.png)<br/>
![06](HW6/06.png)<br/>