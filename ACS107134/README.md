
* �]�wvirtualbox���������A�[�J�@�ihost-only�����d�A�bLinux�̳]�w����������������192.168.200.100/24�C

�Х� `ifconfig`���ҡC(25%)

![1](https://github.com/0905053883/107-1-ntcu-linux/blob/final/ACS107134/1.PNG)

* nginx�O�@�M�������A���n��A�Х�`yum`�w�ˡA�z�L`systemctl`�Ұʫ�A�ϥ�`netstat`����nginx���b�ϥ�Port 80�C(25%)

![2](https://github.com/0905053883/107-1-ntcu-linux/blob/final/ACS107134/2.PNG)

* �z�L���� windows �W���s�����A�s�u��192.168.200.100�C

������ҥi�H�s�u��Linux�W��nginx�������A���C(10%)


* �bLinux�̡A��`curl`�s�u��192.168.200.100�C

������ҥi�H�s�u��Linux�W��nginx�������A���C(10%)

![4](https://github.com/0905053883/107-1-ntcu-linux/blob/final/ACS107134/4.PNG)

* nginx����x�ɦ��`/var/log/nginx`�ؿ��U�A��s�u���s�b�������ɡAnginx�|�O��������T�C

�榡�p�U�A�䤤client��쬰�Ȥ��ip�C (30%)

```
2019/01/15 19:28:28 [error] 12337#0: *4 open() "/usr/share/nginx/html/aa" failed (2: No such file or directory), client: 127.0.0.1, server: _, request: "GET /aa HTTP/1.1", host: "127.0.0.1"
```

�Шϥκ޽u���O�A��X�C��ip�s�u���~�����ơC�A�i��ݭn�ϥ� `cat`�B`cut -d` �B `sort` �B `uniq -c`

�̫��X�榡�A��ܦ�127.0.0.1�Ӫ�ip�o�ͤG�����~�A��192.168.200.100�Ӫ�ip�o�ͤG�����~. 

```
    2  127.0.0.1
    1  192.168.200.100
```

