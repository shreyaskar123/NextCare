# AmpX Comuptation
velX = []
velY = []
velZ = []
velX.append(0)
velY.append(0)
velZ.append(0)
AmpX = []
AmpY = []
AmpZ = []
AmpX.append(0)
AmpY.append(0)
AmpZ.append(0)
for i in range(xAcc.size - 1):
    velX.append(integrate.simps(xAcc[0:i + 1], varTime[0:i + 1], even='avg'))
for i in range(xAcc.size -1):
    AmpX.append(integrate.simps(xAcc[0:i + 1], varTime[0:i + 1], even='avg'))
for i in range(yAcc.size -1):
    velY.append(integrate.simps(yAcc[0:i + 1], varTime[0:i + 1], even='avg'))
for i in range(yAcc.size -1):
    AmpY.append(integrate.simps(yAcc[0:i + 1], varTime[0:i + 1], even='avg'))  
for i in range(zAcc.size -1):
    velZ.append(integrate.simps(zAcc[0:i + 1], varTime[0:i + 1], even='avg'))
for i in range(zAcc.size -1):
    AmpZ.append(integrate.simps(zAcc[0:i + 1], varTime[0:i + 1], even='avg'))      
for i in AmpX:
    print(i)
for i in AmpY:
    print(i)
for i in AmpZ:
    print(i)


