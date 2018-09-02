#!/usr/bin/python2

import commands


p = raw_input("enter the password : ")

ip=commands.getstatusoutput("hostname -i")[1]
xy=ip.split(".")



ipv=commands.getstatusoutput(" nmap -n -sP {0}.{1}.{2}.0-100|grep report | awk '{{print $5}}'".format(xy[0],xy[1],xy[2]) )[1].split("\n")
ram_list=[]
hdd_list=[]
ca=commands.getstatusoutput("echo {} > /ip.txt".format(ipv))


def see_ram(r):

     if r==ip:
             s=commands.getstatusoutput("free -m | grep Mem | awk '{{print $4}}'")
             return s[1]
     else:
             s=commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no root@{1} free -m | grep Mem | awk '{{print $4}}'".format(p,r))
             #print s[1]
             
             return s[1]


def max_ram():
   c=see_ram(i)
   ram_list.append(c)
   #maxram=max(ram_list)

def see_hdd(h):

      if h==ip:
             s=commands.getstatusoutput(" df -l / | grep /dev/mapper/ | awk '{{print $4}}'")
             return s[1]
      else:
             s=commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no root@{1} df -l / | grep /dev/mapper/ | awk '{{print $4}}'".format(p,h))
             #print s[1]
             
             return s[1]


def max_hdd():
        c=see_hdd(i)
        hdd_list.append(c)
      # maxhdd=max(hdd_list)


for i in ipv:
        
        
            see_ram(i)
            max_ram()
            see_hdd(i)
            max_hdd()

#KNOWING THE IP

ram_list=[int(i) for i in ram_list]      
print ram_list
hdd_list=[int(i) for i in hdd_list]      
print hdd_list
print ipv

maxram=max(ram_list)
maxhdd=max(hdd_list)

jobtracker_index=ram_list.index(maxram)
namenode_index=hdd_list.index(maxhdd)

jt=ipv[jobtracker_index]
nn=ipv[namenode_index] 
ab=commands.getstatusoutput("echo {} > /jt.txt".format(jt))
ba=commands.getstatusoutput("echo {} > /nn.txt".format(nn))

print jt
print nn







def installing(n):

                            jdk=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{}  rpm -q jdk".format(p,n))
                            hadoop=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{}  rpm -q hadoop".format(p,n))
                            if jdk[0]==0:
                    
                                   print "jdk installed at "+n
                            else:
                                   print "installing jdk at"+n
                                   s1=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{}  yum install jdk -y".format(p,n))
          
                            if hadoop[0]==0:
                                     print "hadoop already at "+n
                            else :
                                     commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /root/Desktop/hadoop-1.2.1-1.x86_64.rpm root@{}:/root/Desktop/".format(p,n))
                                     commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{}  rpm -ivh /root/Desktop/hadoop-1.2.1-1.x86_64.rpm --replacefiles".format(p,n))

def jps(k):

          name=commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{} rpm -q jdk".format(p,k))
          j=commands.getstatusoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no root@{1} /usr/java/{2}/bin/jps | grep node".format(p,k,name[1]))
          return j

def setting_nn(r):
    

    commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /root/Desktop/writtingnode root@{}:/".format(p,r))
    commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /jt.txt root@{}:/".format(p,r))
    commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /nn.txt root@{}:/".format(p,r))
    commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /ip.txt root@{}:/".format(p,r))
    commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{} python /writtingnode".format(p,r))
    commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{} hadoop namenode -format".format(p,r))
    commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{} hadoop-daemon.sh start namenode".format(p,r))
    print "namenode is set"
    #commands.getstatusoutput("sshpass -p {} ssh root@{} /usr/java/jdk/bin/jps".format(p,r))

def setting_dn_tt(t):
     
     commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /root/Desktop/writtingnode root@{}:/".format(p,t))
     commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /jt.txt root@{}:/".format(p,r))
     commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /nn.txt root@{}:/".format(p,r))
     commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /ip.txt root@{}:/".format(p,r))
     commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{} python /writtingnode ".format(p,t))
     commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{} hadoop-daemon.sh start datanode".format(p,t))
     commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{} hadoop-daemon.sh start tasktracker".format(p,t))
     print "datanode is set"
     #commands.getstatusoutput("sshpass -p {} ssh root@{} /usr/java/jdk/bin/jps".format(p,t))

    
    
def setting_jt(g):
     
     commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /root/Desktop/writtingnode root@{}:/".format(p,g))
     commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /jt.txt root@{}:/".format(p,r))
     commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /nn.txt root@{}:/".format(p,r))
     commands.getstatusoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /ip.txt root@{}:/".format(p,r))
     commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{} python /writtingnode ".format(p,g))
     commands.getstatusoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no root@{} hadoop-daemon.sh start jobtracker".format(p,g))
     print "jt is set"
     #commands.getstatusoutput("sshpass -p {} ssh root@{} /usr/java/jdk/bin/jps".format(p,g))


for i in ipv:
 installing(i)
 if  i==nn:
                      setting_nn(i)
                      if i==jt:
                         setting_jt(i)
 else:
                        setting_dn_tt(i)





