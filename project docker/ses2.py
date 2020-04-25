import os
os.system("systemctl start docker")
while True:
	print('''
	press 0 to exit
	press 1 to see docker information
	press 2 to clear/stop all the docker conatiners
	press 3 to configure web services
	press 4 to start web server
	press 5 to stop web server
	press 6 to install net-tools''')
	n=int(input("enter your choice")
	if n==0:
		os.system("exit")
	elif n==1:
		os.system("docker info")
	elif n==2:
		os.system("docker rm -f $(docker ps -a -q)")
	elif n==3:
		os.system("yum install httpd")
	elif n==4:
		os.system("rm -rf /var/run/httpd/*")#any error remove that line
		os.system("/usr/ubin/httpd")
	elif n==5:
		os.system("killall httpd")	
	elif n==6:
		os.system("yum install net-tools")
	input("press enter to continue")
