# params['AmpX'] = AmpX
df['time'].shape
#params.drop_duplicate(subset = None, keep = "first", inplace = True)
df['AmpY'] = AmpY
df['AmpZ'] = AmpZ
import matplotlib.pyplot as plt
plt.figure()
plt.plot(df['time'],AmpX)
plt.plot(df['time'],AmpY)
plt.plot(df['time'],AmpZ)
count = 0
# df['time'] = df['time'](df['time'] <= 0.005)
print(df['time'])
for i in df['time']:
    if i > 0.005:
        df['time']
AmpX = AmpX[count: 594]
AmpY = AmpY[count: 594]
AmpZ = AmpY[count: 594]

#params.head()
