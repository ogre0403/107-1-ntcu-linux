1.
���إߤT�ӥΤ�A�b���W�٤��O���G examuser1, examuser2, examuser3 �A�P�ɤT�ӥΤ᪺�K�X���O�y ItIsExam �z�C(�аѦҮѤWpasswd --stdin������)
�`�Nuseradd�����O�n��root�Ӱ���A���̳]�K�X�n��passwd+user�W 

![1](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/1.JPG)


���ЧR���t�Τ��� examuser3 �o�ӱb���A�P�ɱN�o�ӱb�����a�ؿ��P�l���ɮצP�B�R���C
�`�N�Y�n�N�a�ؿ��B�l���ɮקR�����ܭn�O�o��"-r"


![2](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/2.JPG)

��examuser1 ���p�߳Q�޲z���R���F�A���O�o�ӱb�����a�ؿ��P�����l���٦s�b�C�аѦҳo�ӱb���i�઺�a�ؿ�
�ҫO�d�� UID �P GID�A �ù��եH�ӱb���즳�� UID/GID ��T�ӭ��ظӱb���C
�ӳo�ӱb�����K�X�е���ItIsExam���˦��C(�����ظm�b�������O�A�аѦ� man useradd ���u�W��󪺻���)

![3](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/3.JPG)

2.
���إ�examuser4�ϥΪ̱b���A�K�X���N�C

���ϥ� root �N /etc/securetty �ƻs�� examuser4�A�B�o�ӱb���n�������ϥθ��ɮפ~��A(�Y���Ҧ����v��)�C

![4](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/4.JPG)

���إߤ@�ӦW�� /examdata/change.txt �����ɮסA�o���ɮת��֦��̬� sshd�A�֦��s�լ� users�Asshd �iŪ�i�g�A
users �s�զ����iŪ�A ��L�H�S�v���C�B�o���ɮת��ק����нվ㦨 2012 �~ 12 �� 21 �� (������T�Y�i�A�ɶ��H�K)

�u�����ɶ��ܬ�00:00 	touch -d 20150101 (filename)
����&�ɶ�		touch -t 201501150821.32 (filename)

![5](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/5.JPG)

3.
���Шϥ� root �������إߩ��U���ɮ׻P�v���G
drwxrwxr-x  root root /dev/shm/unit05/
drwxr-xr--  root root /dev/shm/unit05/dir1/
-rw-r--r--  root root /dev/shm/unit05/dir1/file1 (�ƻs�Ӧ� /etc/hosts)
drwxr-x--x  root root /dev/shm/unit05/dir2/
-rw-r--r--  root root /dev/shm/unit05/dir2/file2 (�ƻs�Ӧ� /etc/hosts)
drwxr-xr-x  root root /dev/shm/unit05/dir3/
-rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (�ƻs�Ӧ� /etc/hosts)
drwxrwxrwx  root root /dev/shm/unit05/dir4/
-rw-------  root root /dev/shm/unit05/dir4/file4 (�ƻs�Ӧ� /etc/hosts)

![6](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/6.JPG)

![7](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/7.JPG)



�ƻs��cp (���ƻs���ɮ�) (�мg���ɮ�)


���ϥΤ@��ϥΪ� �������i��U���u�@�G

���Шϥ� ls -l /dev/shm/unit05/dir[1-4] �̾ڿ�X�����G��������|���ͳo�ǰ��D�H

![8](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/8.JPG)

���Шϥ� ls -l /dev/shm/unit05/dir1/file1 �A�̧ǱN�W�z���ɦW�� dir1/file1 ~ dir4/file4 ����
�A�̾ڲ��ͪ����G��������|�p���H

![9](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/9.JPG)

���Шϥ� vim(or vi) /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4
�A�����x�s (�αj���x�s)�A��������i�H/���i�H�x�s�H
file1(Permission Denied) ���iŪ���i�s��
file2 �L�k��tab����X��(��Ū�ɤ��i���)
file3 �i�Q�s��
file4 (Permission Denied) ���iŪ���i�s��

![10](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/10.JPG)
![11](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/11.JPG)
![12](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/12.JPG)
![13](https://github.com/0905053883/107-1-ntcu-linux/blob/HW-3/ACS107134/13.JPG)


