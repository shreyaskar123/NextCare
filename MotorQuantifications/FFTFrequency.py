import numpy as np
from scipy import fftpack
accX_fft = 10 * fftpack.fft(df['accX'].to_numpy())
accY_fft = 10 * fftpack.fft(df['accY'].to_numpy())
accZ_fft = 10 * fftpack.fft(df['accZ'].to_numpy())
print(abs(accX_fft.mean()))
print(abs(accY_fft.mean()))
print(abs(accZ_fft.mean()))
