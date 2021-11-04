#! /usr/bin/env python
import rospy
from time import sleep

rospy.init_node("hello_python_node")
password = "aa"
#print(type(password))
#print("account: iclab_xiao_ming")
#s=raw_input("password:")
#print(type(s))
times=0
while times<10:
	sleep(1)
	print(times)
	times=times+1
print("time up!!!")
