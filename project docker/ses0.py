import os
os.system("systemctl start docker")
while True:
	print('''
	press 0 to exit
	press 1 to see running os/container
	press 2 to see os images
	press 3 to install docker image
	press 4 to run os in docker''')
	n=int(input("enter your choice")
	if n==0:
		os.system("exit")
	elif n==1:
		os.system("docker ps")
	elif n==2:
		os.system("docker images")
	elif n==3:
		os=input("enter name of os")
		os.system("doker pull {}".format(os))
	elif n==4:
		os=input("enter name of os")
		os.system("doker run -t -i {}".format(os))
	input("press enter to continue")
