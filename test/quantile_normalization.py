
import numpy as np 
import pandas as pd

# Import TCGA melanoma data 
## Rna read data
file='test/data/counts.txt'
with open(file, 'rt') as f: 
    read_counts=pd.read_csv(f,index_col=0)

counts=read_counts.values


def quantile_norm(X):
    """
    
    Normalize each X column (sample) to have SAME distribution
    
    Parameters 
    ..........
    
    X: 2D array of flaot shape (m,n)
    
    Returns 
    ..........
    
    Xn: 2D array of float shape (m,n)
        data normalized
    
    """

    ## compute quantiles
    
    quantiles=np.mean(np.sort(X,axis=0),axis=1) ## sort the values by row, thn calculate the mean by column 
    
    ranks=np.apply_along_axis(stats.rankdata,0,X)
    
    ## 
    rank_indices=ranks.astype(int)-1
    
    Xn=quantiles[rank_indices]
    
    return Xn

def quantile_norm_log(x):
    logx=np.log(x+1)
    logxn=quantile_norm(logx)
    return logxn



log_counts_normalized=quantile_norm_log(counts)
print(log_couts_normalized)


