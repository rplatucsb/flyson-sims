import pickle as pkl
from .smit import SimIter

rs = []
sm = SimIter()
for r in sm:
    rs.append(r)

pkl.dump(rs, open("firstrun.pkl", "wb"))
