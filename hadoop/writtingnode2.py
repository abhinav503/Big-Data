#!/usr/bin/python2



import commands

ip=commands.getstatusoutput("hostname -i")[1]

f1=open("/ip.txt",'r')
s=f1.read()
k=s.split("\n")[0]
j=k[1:len(k)-1].split(",")

f2=open("/nn.txt",'r')
ss=f2.read()
nn=ss.split("\n")[0]


f3=open("/jt.txt",'r')
s2=f3.read()
jt=s2.split("\n")[0]



def write_mapred_jt(d):
        f=open("/etc/hadoop/mapred-site.xml",'w')
         
        f.write("""  <?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>

</configuration>
""".format(d))
         f.close()
         print "written "+d

def write_hdfs_dn() :
   
    f=open("/etc/hadoop/hdfs-site.xml",'w')
    
    commands.getstatusoutput("mkdir /dn")

    f.write("""  <?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/dn</value>
</property>

</configuration>
""")

    f.close()  
    print "written hdfs dn"

def write_hdfs_nn() :
   
       f=open("/etc/hadoop/hdfs-site.xml",'w')
    
       commands.getstatusoutput("mkdir /nn")

       f.write("""  <?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/nn</value>
</property>

</configuration>
""")

       f.close() 
       print "written hdfs nn" 

def writecore(r) :
      g=open("/etc/hadoop/core-site.xml",'w')

      g.write("""  <?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>

</configuration>
""".format(r)) 

      g.close()
      print "written core "+r

for i in j:
   if i==nn:
         write_hdfs_nn()   #writing namenode
         writecore(ip)    #saying that this the namenode

   else:
     if i==jt:
              write_mapred_jt(ip)    #telling that it is job tracker
              writecore(ip) #telling about namenode
                
     else:
                  write_hdfs_dn()   #wriiting datanode
                  write_mapred_jt(ip)  #telling about jt for task tracker
                  writecore(ip)     #telling about namenode for datanode

