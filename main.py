import networkx as nx
import pandas as pd
import numpy as np
import csv
def read_network(network):
    print('\n')
    print("** Loading and processing network file")
    with open(network,'r') as network_file:
        G=nx.read_edgelist(network_file,delimiter='\t')
        print("\t Network file Processing done")
        print("\t Network contains %s nodes and %s edges\n"%(G.number_of_nodes(),G.number_of_edges()))
        return G
def remove_self_links(G):
    G.remove_edges_from(nx.selfloop_edges(G))
def input_gene_list(file_in):
    print('** Reading input gene list')
    gene_list=set()
    with open(file_in,'r')as gene_file:
        reader=csv.reader(gene_file,delimiter='\t')
        for row in reader:
            row1=(row[0])
            gene_list.add(row1)
    print("\t No of Genes in the input gene list:%s"%(len(gene_list)))
    return gene_list
N=read_network("Human-PPI.txt")
remove_self_links(N)
l1=input_gene_list("protein-list1.txt")
l2=input_gene_list("protein-list2.txt")
S=nx.complete_graph(N)
S.degree()
print(list(S.degree()),file=open("nodes.txt", "a"))
print(nx.clustering(S),file=open("Clustering.txt","a"))
#print(nx.average_clustering(S))
