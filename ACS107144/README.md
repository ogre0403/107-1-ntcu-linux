## 1.

# ���ϥ�root�n�J

# �إ� examuser1�Bexamuser2�Bexamuser3
* useradd �ɦW
* passwd �ɦW
* ��J�K�X�GItIsExam
* �A���T�{�K�X�G ItIsExam

# �R���t�Τ��� examuser3 �b���A�P�ɱN�o�ӱb�����a�ؿ��P�l���ɮצP�B�R��
* userdel -r examuser3
 > �@�w�n�[ -r �~��N�[�ؿ��P�l���ɮצP�B�R��
* �� id examuser3 �ˬd�b���O�_�R��

# examuser1 ���p�߳Q�޲z���R���F�A���O�o�ӱb�����a�ؿ��P�����l���٦s�b�C�Ѧ�UID/GID���رb���C
* ���R�� examuser1�A�R�����O�Guserdel examuser1 
  > (���ݭn�[-r�A�]���ڭ̭n�O�d�L�b�a�ؿ��P�����l�󪺸��)
* �i�J�a�ؿ��A���O�Gcd /home
* �d�ݮa�ؿ����b������ơA���O�Gll 
* �i�J�l���ơA���O�Gcd /var/spool/mail
* �d�ݶl�󤤱b����ơA���O�Gll
 > �o�{��̬Ҧ�1001����ơA�i���o�O�b���W�پD�R���� examuser1 �b�ؿ��P�����l�󤤥��D���������
* �Q��1001���ظ�ơA���O�Guser add -u 1001 -U examuser1
* ���s�]�w examuser1 ���K�X�A���O�Gpasswd examuser1
 > ��J�K�X�GItIsExam
 > �A���T�{�K�X�G ItIsExam
* �A���^��a�ؿ��A���O�Gcd /home
* �d�ݮa�ؿ����b������ơA���O�Gll 
 > �o�{examuser1�w���\����
* ������A���s�}���A�ϥ� examuser1 �n�J�A�T�{�ק令�\�C

## 2.

# �إ� examuser4
* useradd �ɦW
* passwd �ɦW
* ��J�K�X�G�ۭq
* �A���T�{�K�X�G �ۭq

# �ϥ� root �N /etc/securetty �ƻs�� examuser4�A�B�o�ӱb���n�������ϥθ��ɮפ~��A(�Y���Ҧ�. ���v��)�C
* �ƻs /etc/securetty �� /home/examuser4�A���O�Gcp /etc/securetty /home/examuser4
* �i�� examuser4 �̡A���O�Gcd examuser4
* �ˬd�O�_���\�ƻs�ɮ׵� examuser4�A���O�Gls
 > ���\���ܷ|�X�{�е����⩳�u�����Ʀr
* �ϥ�root�������ɮ��v��
* ����ɮ��v���A���O�Gchmod u=rwx,g=rwx,o=rwx /home/examuser4/securetty
* �����b����examuser4 �A���O�Gsu - examuser4
* �d�ݱb���v���A���O�Gll

# �إߤ@�ӦW�� /examdata/change.txt �����ɮסA�o���ɮת��֦��̬� sshd�A�֦��s�լ� users�Asshd �iŪ�i�g�Ausers �s�զ����iŪ�A ��L�H�S�v���C�B�o���ɮת��ק����нվ㦨 2012 �~ 12 �� 21 �� (������T�Y�i�A�ɶ��H�K)
* �i��D�ؿ��A���O�Gcd /
* �إ߷s����ơA���O�Gmkdir examdata 
* �T�{��Ƨ��s�W���\�A���O�Gls
* �i�Jexamdata��Ƨ��A���O�Gcd examdata
* �s�W�ɮ�change.txt�A���O�Gtouch change.txt
* �T�{�ɮ׷s�W���\�A���O�Gls
* �d���ɮת��֦��̻P�v���A���O�Gll
* ����ɮ׾֦��̬�sshd�A���O�Gchown sshd change.txt
* ����ɮת��s�լ�users�A���O�Gchgrp users change.txt
* ����ɮ��v����-rw-r-----�A���O�Gchmod u=rw,q=r,0= change.txt
* �ˬd�ɮ��v���ξ֦��̬O�_�ק令�\�A���O�Gll
* ���ɶ��A���O�Gtouch -t 201212211200 change.txt
 > �~���ɤ��������ݭn�Ů�
* �ˬd�ɶ��O�_�ץ����\�A���O�Gll



## 3.

# �ϥ� root �������إߩ��U���ɮ׻P�v���G
1. drwxrwxr-x  root root /dev/shm/unit05/
2. drwxr-xr--  root root /dev/shm/unit05/dir1/
3. -rw-r--r--  root root /dev/shm/unit05/dir1/file1 (�ƻs�Ӧ� /etc/hosts)
4. drwxr-x--x  root root /dev/shm/unit05/dir2/
5. -rw-r--r--  root root /dev/shm/unit05/dir2/file2 (�ƻs�Ӧ� /etc/hosts)
6. drwxr-xr-x  root root /dev/shm/unit05/dir3/
7. -rw-rw-rw-  root root /dev/shm/unit05/dir3/file3 (�ƻs�Ӧ� /etc/hosts)
8. drwxrwxrwx  root root /dev/shm/unit05/dir4/
9. -rw-------  root root /dev/shm/unit05/dir4/file4 (�ƻs�Ӧ� /etc/hosts)
 > �H�U�Ϥ峡���藍�W�A�]���b�g�����O��A�ڷQ��󦳮Ĳv���g�k�A�]����r�ԭz�������Ĳv�����k�A�ϫh���ڦb�g�ɪ������C
* �i�J�D�K�F�A���O�Gcd /
* �i�Jdev�A���O�Gcd dev/
* �i�Jshm�A���O�Gcd shm/
* �إ�unit05�ؿ��ɡA���O�Gmkdir unit05/
* �ק�unit05���v���A���O�Gchmod u=rwx,g=rwx,o=rx unit05
* �i�Junit05�A���O�G cd unit05/
* �إ� dir1,dir2,dir3,dir4 ��Ƨ�
 > ���O
 > mkdir dir1/
 > mkdir dir2/
 > mkdir dir3/
 > mkdir dir4/
* �ק� dir1,dir2,dir3,dir4 ���v��
 > ���O
 > chmod u=rwx,g=rx,o=r dir1
 > chmod u=rwx,g=rx,o=x dir2
 > chmod u=rwx,g=rx,o=rx dir3
 > chmod u=rwx,g=rwx,o=rwx dir4
* �ƻs/etc/hosts�� dir1,dir2,dir3,dir4�A�ɦW�אּ file1,file2,file3,file4�C
 > ���O
 > cp /etc/hosts /dev/shm/unit05/dir1/file1
 > cp /etc/hosts /dev/shm/unit05/dir2/file2
 > cp /etc/hosts /dev/shm/unit05/dir3/file3
 > cp /etc/hosts /dev/shm/unit05/dir4/file4
* �i�J dir1�A�ק� file1 �v���A
 > ���O�G
 > cd dir1/
 > chmod u=rw,g=r,o=r file1
* �^�W���A���O�G..
* �i�J dir2�A�ק� file2 �v���A
 > ���O�G
 > cd dir2/
 > chmod u=rw,g=r,o=r file2
* �^�W���A���O�G..
* �i�J dir3�A�ק� file3 �v���A
 > ���O�G
 > cd dir3/
 > chmod u=rw,g=rw,o=rw file3
* �^�W���A���O�G..
* �i�J dir4�A�ק� file4 �v���A
 > ���O�G
 > cd dir4/
 > chmod u=rwx,g=rwx,o=rwx file4

# �Шϥ� ls -l /dev/shm/unit05/dir[1-4] �̾ڿ�X�����G��������|���ͳo�ǰ��D�H
* �]��examuser1�Oother 
 > dir1 �����G�u��Ū�C
 > dir2 �u�����A�ҥH�ݤ������F��C
 > dir3 ����������ܡA�u�O�L�k�ק�C
 > dir4 �Ҧ����v�����}��F�A�ҥH����N�ϥΡC
 > ���檬�p�p��

# �� ls -l /dev/shm/unit05/dir1/file1 �A�̧ǱN�W�z���ɦW�� dir1/file1 ~ dir4/file4 ����A�̾ڲ��ͪ����G��������|�p���H
* �]��examuser1�Oother 
 > dir1 �����G�u��Ū�C
 > dir2 �����G�u��Ū�C
 > dir3 �iŪ�i��C
 > dir4 �Ҧ����v������_�ӤF�C
 > ���檬�p�p��

# �� vim /dev/shm/unit05/dir1/file1 ~ vim /dev/shm/unit05/dir4/file4�A�����x�s (�αj���x�s)�A��������i�H/���i�H�x�s�H
* �]��examuser1�Oother 
 > vim /dev/shm/unit05/dir1/file1�A�L�k��w:�x�s�A�]��other�S��file1���ק��v��
 > vim /dev/shm/unit05/dir2/file2�A�L�k��w:�x�s�A�]��other�S��file2���ק��v��
 > vim /dev/shm/unit05/dir3/file3�A�i��w:�x�s�A�]��other��file3���ק��v��
 > vim /dev/shm/unit05/dir4/file4�A�L�k��w:�x�s�A�]��other�S��file4���ק��v��





