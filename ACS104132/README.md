1.
useradd examuser1
useradd examuser2
useradd examuser3
passwd examuser1
ItIsExam 
ItIsExam 
passwd examuser2
ItIsExam 
ItIsExam 
passwd examuser3
ItIsExam 
ItIsExam 
userdel -r examuser3

2.
useradd examuser4
passwd examuser4
aaaaaa
cp /etc/securetty examuser4/
chown examuser4.examuser4 ~examuser4/securetty
mkdir examdata
vi change.txt

3
mkdir unit05
mkdir dir1
cp etc/hosts/file1 file1
mkdir dir2
cp etc/hosts/file2 file2
mkdir dir3
cp etc/hosts/file4 file4
mkdir dir4
cp etc/hosts/file4 file4