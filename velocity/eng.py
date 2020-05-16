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
