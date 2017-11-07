import numpy as np
import pandas as pd
a = (0,1,2,3)
q_table = pd.DataFrame(columns=a)
print(q_table)
q_table = q_table.append(pd.Series([0]*len(a),index=q_table.columns,name='#',))
q_table = q_table.append(pd.Series([1]*len(a),index=q_table.columns,name='*',))
q_table = q_table.append(pd.Series([2]*len(a),index=q_table.columns,name='$',))
q_table = q_table.append(pd.Series([3]*len(a),index=q_table.columns,name='&',))
print(q_table)
b = np.random.uniform()
print(b)
c = q_table.index
c = q_table.reindex(index=np.random.permutation(c))
print(c)
