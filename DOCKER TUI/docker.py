import os
os.system("systemctl start docker")
os.system("tput setaf 1")
print("""\t\t\t Welcome to Docker TUI program """)
os.system("tput setaf 7")
i=0
while True:
        i=i+1
        if 1==15:
            i=1
        if i==1 or i==9 :
            i=i+1
        os.system("tput setaf {}". format(i))
        print('''
        press 0: To exit
        press 1: To see running os/container
        press 2: To see os images
        press 3: To install docker image
        press 4: To run os in docker
        press 5: Check Ram details
        press 6: history of os created or stopped
        press 7: Giving name to os
        press 8: Install any software or command in your comtainer
        press 9: to remove any particular os/container
        press 10: to remove all the os in one go 
        press 11: to create new image of current os/container
        press 12: to see docker information
        press 13: to configure web services
        press 14: detailed info of os
        press 15: network details of os
        press 16: Create your own network
        press 17: connect network to os
        press 18: disconnect network from os
        press 19: to get ip of os
        press 20: details of storage
        press 21: create persistenet storage
        press 22: docker command help
        press 23: download wordpress image
        press 24: download mysql
        press 25: install docker compose
        press 26: check docker compose version
        press 27: start infrastructure of web app
        press 28: start docker compose
        press 29: stop docker compose
        press 30: remove infrastructure  ''')
        n=int(input("Enter your choice:"))
        if n==0:
            exit()
        elif n==1:
            os.system("docker ps")
        elif n==2:
            os.system("docker image ls")
        elif n==3:
            nm=input("enter the name of the OS image")
            os.system("docker pull {}". format(nm))
        elif n==4:
            nm=input("name of the OS")
            os.system("docker run -dit {}". format(nm))
        elif n==5:
            os.system("free -m")
        elif n==6:
            os.system("docker ps -a")
        elif n==7:
            nme=input("enter the name to give ")
            osn=input("enter the os to give name")
            os.system("docker run -dit --name {0} {1}". format(nme,osn))
        elif n==8:
            cmd=input("enter the software or command(its software) name")
            os.system("yum install {}". format(cmd))
        elif n==9:
            osm=input("enter the name of os")
            os.system("docker container rm {}". format(osm))
        elif n==10:
            os.system("docker container rm -f $(docker container ls -a -q )")
        elif n==11:
            while True:
                print("""
                press 1: to create new image
                press 2: for checking  the new image of os
                press 3: for runing it""")
                ch1=int(input("enter chioce"))
                if ch1==1:
                    nnm=input("enter the  name of container:")
                    n2=input("new image name")
                    os1=input("name of old image :")
                    os.system("docker run -dit --name {0} {1}". format(nnm,os1))
                    os.system("docker commit {0} {1}". format(nnm,n2))
                    break
                elif ch1==2:
                    os.system("docker image ls")
                    break
                elif ch1==3:
                    nnm=input("enter the same new image name ")
                    os.system("docker run -it {}". format(nnm))
                    break
        elif n==12:
            os.system("docker info")
        elif n==13:
            os.system("yum install httpd")
        elif n==14:
            osn=input("name of container")
            os.system("docker logs {}". format(osn))
        elif n==15:
            os.system("docker network ls")
        elif n==16:
            d=input("enter the driver name")
            n=input("enter name of new network")
            os.system("docker network create -driver {0} {1}". format(d,n))
            print("network created")
            os.system("docker network ls")
        elif n==17:
            n=input("network name")
            o=input(" os name")
            os.system("docker network connect {0} {1}". format(n,o))
        elif n==18:
            n=input("network name")
            o=input(" os name")
            os.system("docker network disconnect {0} {1}". format(n,o))
        elif n==19:
            nm=input("name of os")
            os.system(" docker inspect {} | grep IP". format(nm))
        elif n==20:
            os.system("docker volume ls")
        elif n==21:
            n=input("storage name")
            os.system("docker volume create {}". format(n))
            print("storage created")
            os.system("docker volume ls")
        elif n==22:
            os.system("docker run --help")
        elif n==23:
            os.system("docker pull wordpress")
        elif n==24:
            os.system("docker pull mysql")
        elif n==25:
            os.system('curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-sompose')
            os.system("chmod +x /usr/local/bin/docker-compose")
        elif n==26:
            os.system("docker-compose version")
        elif n==27:
            os.system("docker-compose up -d")
        elif n==28:
            os.system("docker-compose start")
        elif n==29:
            os.system("docker-compose stop")
        elif n==30:
            os.system("docker-compose rm")
        input("Press enter to continue....")
        os.system("clear")



