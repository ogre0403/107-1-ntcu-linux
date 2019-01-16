1.
rpm -ql openssh-server
圖一

systemctl status sshd.service
systemctl status sshd.socket
圖二

vi /etc/ssh/sshd_config
圖三

semanage port -a -t ssh_port_t -p tcp 2222
圖四

firewall-cmd --permanent --zone=public --add-port=2222/tcp
圖五

systemctl restart sshd.service
圖六

ss -tnlp | grep sshd
圖七

