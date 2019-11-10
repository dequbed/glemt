import math
import numpy as np
import matplotlib.pyplot as plot

import os.path

f = 'data.npy'

if not os.path.isfile(f):
    import mdt
    data = mdt.dataRead(amplitude=5, samplingRate=48000, duration=1/25, channels=[0], resolution=14, outType='volt')
    np.save(f, data, allow_pickle=True)

data = np.load(f, allow_pickle=True)

ch0 = data[0]
t = np.linspace(0, 1000, ch0.size)

# 50Hz => Eine Periode ist 1/50 * sample rate. Ceil um mindestens eine volle Periode zu erhalten.
stop = math.ceil(48000/50)
per = ch0[0:stop]

# Erster Nulldurchgang: Kleinster Absoluter Wert
first_zero = (np.abs(per)).argmin()

full_period = ch0[first_zero : first_zero+stop]


p, (a1, a2) = plot.subplots(2, sharex=True)

a1.plot(t, ch0)
a1.grid(True)
a1.set_title("Komplette Messkurve")
a1.set_ylabel("Spannung")

a2.plot(t[first_zero : first_zero+stop], full_period)
a2.grid(True)
a2.set_title("Einzelne Periode, ausgeschnitten")
a2.set_xlabel("Zeit in ms")
a2.set_ylabel("Spannung")

plot.show()
p.savefig('out.pdf')
