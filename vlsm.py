#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#El codigo requiere tener las paqueterias  
#	- ipcalc
#	- numpy
#Se ejecuta como python VLSM.py 192.168.0.0/28 10
#o 					  ./VLSM.py 192.168.0.0/28 10
#Donde 192.168.0.0 => IP inicial
#	   28		   => Mascara de Red para hacer las divisiones
#	   10		   => Numero de subredes de ese tamano, se considera red de uso y desuso en caso de expandirse

import ipcalc,sys
from math import ceil
from numpy import log2

networkId,mask = sys.argv[1].split('/') #'192.168.0.0/21'
num_subnets= int(sys.argv[2]) if len(sys.argv)>2 else 1    #20

def nextNetwork(current):
	a,b,c,d = str(current).split('.')
	a,b,c,d = int(a),int(b),int(c),int(d)
	s=1
	if d<255: 		d+=1; s=0
	else:    		d=0	
	if c<255 and s:	c+=1; s=0
	elif not s:	c=c
	else:			c=0
	if b<255 and s:	b+=1; s=0
	elif not s:	b=b
	else: 			b=0
	if a<255 and s: a+=1; s=0
	elif not s:	a=a
	else: 			a=0
	return '%s.%s.%s.%s'%(a,b,c,d)

def getMask(mask):
	ct=32-int(mask)
	j = ['1' for i in xrange(0,ct)]
	j += ['0' for i in xrange(0,int(mask))]
	a=[]
	for i in xrange(0,4):     
		a+=['.']
		for i in xrange(0,8): a+=[j.pop()]
	a.reverse()
	a=''.join(a)[:-1].split('.') #Unir como numero binario y separar por punto
	print a
	return '%s.%s.%s.%s'%(int(a[0],2),int(a[1],2),int(a[2],2),int(a[3],2))

for i in xrange(0,num_subnets):
	print 'USO' if not i%2 else 'DESUSO',i,'\t\t\t%s <--> /%s'%(getMask(mask),mask)
	nt = ipcalc.Network('%s/%s'%(networkId,mask)) 
	print '\tNetwork ID \t\t', nt[0]	
	print '\tBroadcast \t\t',nt[-1],'\n'
	networkId = nextNetwork(nt[-1])
