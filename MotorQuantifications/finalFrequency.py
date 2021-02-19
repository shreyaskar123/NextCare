nfft = 512
Fs = 1000
f = 200
val = 9
numArray = [], f_scale = [], ps = [], psAcc = [], hlfps = [], kAcc = [], vAcc = [], f_scale = [], f_est = [] # f_est estimates frequency
for i in range(0,val):
  psAcc[i].append(2.0 * np.abs(acc_fft[i]/df[i].size) ** 2)
for i in range(0,val):
  hlfps.append(ps[i][1:int((ps.size)/2)])
for i in range(0,val):
  kAcc.append(np.argmax(hlfps[i])
for i in range(int(nfft/2)):
    f_scale.append(i)
f_scale = np.array(f_scale, dtype=np.float32) * (Fs/nfft)
for i in range(0,val):
  f_est.append(f_scale[i])

