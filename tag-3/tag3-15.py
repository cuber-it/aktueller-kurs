import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(50, 4), columns=list('ABCD'))
csv = df.to_csv(index=False)
#with open("dataframe.csv", "w") as fd:
#    fd.writelines(csv)
#print(csv)

print(df.sum())
print(df.mean())