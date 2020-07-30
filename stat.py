#%%
import pandas as pd
import tensorflow as tf
import scipy
import scipy.stats

#%%
df = pd.read_csv('bicicletas-compartidas.csv')

#%%
fm = tf.keras.datasets.fashion_mnist
(img,cat) = fm.load_data()[0]
# %%
import numpy as np
import datetime
from datetime import date
#%%
coin = ['x','o']
counter = [0,0]
p = 1/2
#%%
from scipy.stats import bernoulli
#%%
a  = bernoulli.rvs(p,size=1000)
sum(a)
# %%
for i in range(1000):
    toss = bernoulli.rvs(p)
    counter[toss] = counter[toss] + 1
    print(coin[toss])
#%%
from scipy.stats import binom

# %%
v  = binom.rvs(p=p,n=100,size=100)
s  = pd.Series(v)
c = s.value_counts()
c_p = c/100
print(c_p)
# %%


# %%
