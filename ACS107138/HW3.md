1.�Ұʤ��e�w�˪��������A�n�Jroot�b���A��J�K�X�A
�Hroot��������Juseradd examuser1�ӫإ�examuser1�o�ӥΤ�A
�A��Jpasswd examuser1�A��ltlsExam�@��examuser1���K�X�A
��Lexamuser2��examuser3�]�����ӤW�����B�J�ӫإߡC
2.��Juserdel -r examuser3�R��examuser3���b���M�ؿ��C
3.��J id examuser1�A�d��examuser1��UID�MGID�A�O1001�A�A��Jadduser -u 1001 examuser1�A���s�إ�examuser1���b���C
------------------------------------------------------------------------
1.�̤W�����覡�A�n�Jroot�A�M���Juseradd examuser4�ӫإ�examuser4�o�ӱb���A�A��Jpasswd examuser1�A�]�w�K�X�C
2.���ۿ�Jcp/etc/securetty/home/examuser4/�A��/etc/securetty/�ƻs��examuser4�A�Q��chomd����v���A
��Jchmod u=rwx, g=rwx, o=rwx���C
3.����Jcd�^��a�ؿ��A��Jmkdir examdata�ӫإ�examdata�A
��Jcd examdata/�i�J�Ӹ�Ƨ��A��Jtouch change.txt�إ��ɮסA
��Jchown sshd change.txt�A��֦��̦W�٧令sshd�A
�A��Jchgrp users change.txt�A��s�զW�٧令users�A
�n����v���A�ҥH��Jchmod u=rw, g=r, o= change.txt�A���֦��̥i�HŪ�g�A���s�եi�HŪ�A�Ө�L�ϥΪ̨S���v���A
��Jtouch -t 20121221xxxx.txt���ɶ��C
------------------------------------------------------------------------
1.�^��a�ؿ��A��Jmkdir dev�ӫإ�dev�o�Ӹ�Ƨ��A��Jcd dev/�i�Jdev��Ƨ��A
��Jmkdir shm�A�bdev����Ƨ��̦A�]�@�ӥs�@shm���l��Ƨ��A��Jcd shm/�i�J�A
��Jmkdir unit05�A�Х�unit05�o�Ӹ�Ƨ��A��Jcd unit05/�H�i�J��Ƨ��A
��Jchmod u=rwx, g=rwx, o=rx���unit05����Ƨ��v���A���ᱵ�۫إ�dir1-4����Ƨ��A
�@�˫e�����覡��Jchmod�h����v���C
2.��Jls -1/dev/shm/unit05/dir[1-4]�A
dir1�����G�O�iŪ�Adir2�����G�O�i����Adir3�����G�O�iŪ�i����Adir4�����G�O�iŪ�i�ק�i����C
3.��Jls -1/dev/shm/unit05/dir1/file[1-4]�A
file1�����G�O�iŪ�Afile2�����G�O�iŪ�Afile3�����G�O�iŪ�i��g�Afile4�����G�O�S���v���C
