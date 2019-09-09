"""
百钱百鸡问题
"""


small=0
for f in range(0,21):
	for m in range(0,34):
		if(5*f+3*m+(100-f-m)/3==100):
			small=100-f-m
			print('公鸡有%d只,母鸡有%d只,小鸡有%d只'%(f,m,small))

			


  
