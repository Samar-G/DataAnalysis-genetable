# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 00:35:38 2020

@author: samar
"""

import pandas as pn
import matplotlib.pyplot as mp
#import numpy as np
#from numpy import median

dataset= pn.read_csv(r'C:\Users\samar\gene_table.txt')
'''
Different Biotypes
'''
countOfGenes=pn.unique(dataset['gene_biotype'])
#print(countOfGenes)
print("Number of Different Biotypes:",len(countOfGenes))

'''
Number of Genes
'''
print("Total number of genes:",len(dataset))
'''
Min, Max, Average, and Median of Known Isoforms
'''
ma=dataset.get('transcript_count').max()
mi=dataset.get('transcript_count').min()
me=dataset.get('transcript_count').mean()
med=dataset.get('transcript_count').median()
print("Maximum Value:",ma)
print("Minimum Value:",mi)
print("Average of Values:",me)
print("Median of Values:",med)
'''
Chromosomes and Genes in Increasing order
'''
NoGenes= dataset.groupby(dataset['chromosome']).size()
print("Chromosomes Sorted:",NoGenes.sort_values())
'''
Bar Chart for number of Chromosomes
'''
NoGenes.plot.bar()
mp.rcParams['figure.figsize']=(22,17)
#mp.rcParams['lines.color'] = 'C6'
mp.xlabel("Chromosomes")
mp.ylabel("Number of Genes")
mp.show()
'''
Percentage of Genes Located on + Strand
'''
df= pn.DataFrame(dataset)
ps=(df[df.get('strand')=='+'])
n = ((ps.pivot_table(index=['chromosome','strand'], aggfunc='size'))/df.pivot_table(index=['chromosome'], aggfunc='size'))*100
print("Percentage of Genes Located on + Strand:")
print (n.round(decimals=3))
#print(((df.pivot_table(index=['chromosome','strand'], aggfunc='size'))/df.pivot_table(index=['chromosome'], aggfunc='size'))*100)
#print(((dataset.groupby(['chromosome','strand']).size())/(dataset.groupby(['chromosome']).size()))*100)
'''
Average number of Transcripts
'''
df= pn.DataFrame(dataset)
grpGene = df.groupby('gene_biotype')
mean = grpGene.mean().round(decimals=3)
print(mean)
