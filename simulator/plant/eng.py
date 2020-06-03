from _io import StringIO
import numpy as np

class Engine:

    def __call__(self, t):
        """ Linear interpolation for thrust from time """
        return np.interp(t, self.time, self.force)
     
    def __init__(self, fname):
        f = fname
        if isinstance(fname, str):
           f = open(fname, "r") 

        time = []
        force = []
        info = ""
        for line in f.readlines():
            if line[0] == ";":
                continue
            try:
                t1, f1 = filter(None, line.split(" "))
                time.append(float(t1))
                force.append(float(f1))
            except: # FIXME specific exception
                info = line
        f.close()
        self.time = np.array(time)
        self.force = np.array(force)
        self.info = info.strip()


f50_text = """
    ; Estes F50 Blue thunder Porpellant [Relabeled Aerotech]
    ; File produced July 4, 2000
    ; The total impulse, peak thrust, average thrust and burn time are
    ; the same as the averaged static test data on the NAR web site in
    ; the certification file.
    F50 29 98 6 .0379 .0836 Estes
      0.012 51.377
      0.023 61.197
      0.026 66.117
      0.044 66.564
      0.082 69.685
      0.152 73.264
      0.208 75.053
      0.237 77.279
      0.254 76.832
      0.272 77.726
      0.307 77.726
      0.330 76.832
      0.336 78.621
      0.342 76.832
      0.354 79.590
      0.363 76.385
      0.371 77.756
      0.395 76.385
      0.447 75.937
      0.523 73.711
      0.652 68.344
      0.810 60.302
      0.828 62.539
      0.836 58.076
      0.901 53.603
      1.079 37.074
      1.158 29.480
      1.196 25.464
      1.246 16.976
      1.301  9.380
      1.430  0.000
"""
f50 = Engine(StringIO(f50_text))
