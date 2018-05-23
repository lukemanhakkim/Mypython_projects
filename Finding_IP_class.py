import re
#Ip=raw_input("Enter the IP:")
Ip= "127.255.16.17"
print Ip

#classA
p1='^([0-9]|[0-9][0-9]|[0-1][0-2][0-6])\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])\.([0-9]|[0-9][0-9]|[0-2][0-5][0-5])$'
#classB
p2='^((1(2[8-9]|[3-8][0-9]|9[0-1]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))|192\.0\.0\.0)$'
#classC
p3='^((1(9[2-9])|2([0-1][0-9]|2[0-3]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))|224\.0\.0\.0)$'
#classD
p4='^((2(2[4-9]|3[0-9]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))|240\.0\.0\.0)$'
#classE
p5='^((2(4[0-9]|5[0-4]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))|255\.0\.0\.0)$'
#loopback
p6='^127\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))\.([0-9]|[1-9][0-9]|1([0-9][0-9])|2([0-4][0-9]|5[0-5]))$'
if re.search(p1,Ip):
    print "This is class A IP"

elif re.search(p2,Ip):
    print "This is class B IP"

elif re.search(p3,Ip):
    print "This is class C IP"

elif re.search(p4,Ip):
    print "This is class D IP used for Multicast purpose"

elif re.search(p5,Ip):
    print "This is class E IP for Research purpose"

elif re.search(p6,Ip):
    print "This is loopback IP for debugging purpose"
else:
    print "Invalid IP format"