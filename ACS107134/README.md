* ���ϥ�
">" ���ϥ�
![]()
`���Ϊk
�ť|�Ӧ��t�@�إΪk
### �Х�ӽҰ�W�m�ߡA�z�Lsystemd�޲z�G��sshd�A�ȡA�����ĤG��sshd�A�Ȫ� port ���� 2222�C
### ������i�H�ϥΫ��O netstat -alntp | grep ssh �T�{�O�_�ҰʤG��sshd�A�ȡA�d�Ҧp�U�G

` $ netstat -alntp | grep ssh `

` tcp        0      0 0.0.0.0:22     0.0.0.0:*     LISTEN      1300/sshd `

` tcp        0      0 0.0.0.0:2222   0.0.0.0:*     LISTEN      15275/sshd `

` tcp6       0      0 :::22          :::*          LISTEN      1300/sshd `

` tcp6       0      0 :::2222        :::*          LISTEN      15275/sshd `

1.���]�wssh�s���𪺳]�w�� /etc/ssh/sshd_config�C

�ƻs�@�����W�� sshd2_config �A�N�s����אּ2222
![](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-10/ACS107134/3.PNG)

2.�A���ssh���]�w�}�� /usr/lib/systemd/system/sshd.service�C

�ƻs�@�����W��sshd2.service �A�NExecstart�W�[ -f /etc/ssh/sshd2_config 
![](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-10/ACS107134/4.PNG)

3.systemctl start sshd2 �ҰʸӪA��
![](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-10/ACS107134/1.PNG)
