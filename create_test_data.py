import numpy as np
import pandas as pd

NUM_CH = 10

DAT_POINTS = 1000
data = np.random.random([NUM_CH, DAT_POINTS])

np.save("dat.npy", data)


data = np.random.random([15, DAT_POINTS])
df = pd.DataFrame(data.T, columns=[f"ch_csv_{i}" for i in range(15)])
df.to_csv("data.csv", index=False)
