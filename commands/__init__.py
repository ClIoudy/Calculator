import os

this = os.path.basename(__file__)
p = os.path.dirname(__file__)

__all__ = [f[:-3] for f in os.listdir(p) if f[-3:] == ".py" and f != this]