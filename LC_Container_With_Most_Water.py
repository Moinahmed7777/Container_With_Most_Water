# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 20:29:29 2020

@author: Necro
"""

def max_area(height):
    X=height
    L=len(X)
    end_p=L-1
    start_p=0
    maxArea=0
    while end_p>start_p:
        curr_area=(min(X[start_p],X[end_p]))*abs(end_p-start_p)
        maxArea=max(maxArea,curr_area)
        if curr_area<=maxArea:
            curr_S=X[start_p]
            curr_E=X[end_p]
            if curr_S<=curr_E:
                start_p=start_p+1
            if curr_E<=curr_S:
                end_p-=1

    return(maxArea)

def main():
    t_list=[1,8,6,2,5,4,8,3,7]
    if max_area(t_list)==49:
        print('For test list,',t_list,', passed!')
    else:
        print('For test list,',t_list,', failed!')
               
    
    
if __name__ == '__main__':

    main()