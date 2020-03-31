#!/usr/bin/env python
# coding: utf-8

# In[36]:


def pivot_finalization(arr): # this function finds the correct place for last item in array 
    num=arr[-1] #starting with default pivot
    leftind=0
    rightind=len(arr)-2
    while leftind<=rightind:
        if arr[leftind]<= num:
            leftind=leftind+1
        elif arr[rightind]>=num:
            rightind=rightind-1
        elif arr[leftind]> num and arr[rightind]<num:
            temp=arr[leftind]
            arr[leftind]=arr[rightind]
            arr[rightind]=temp
        else:
            pass
    temp1=arr[leftind]
    arr[leftind]=num
    arr[-1]=temp1
    return arr,leftind


# In[37]:


pivot_finalization([3,4,5,6,1])


# In[38]:


pivot_finalization([3,4,5,6,4])


# In[39]:


def quick_sortify(arr):
    if len(arr)<2:
        return arr
    else:
        arrf,pivot=pivot_finalization(arr)
        print (arrf)
        return quick_sortify(arrf[:pivot])+quick_sortify(arrf[pivot:])


# In[40]:


quick_sortify([5,54,12])


# In[41]:


quick_sortify([3,4,2,12,54,1,5,10])


# In[ ]:





# In[ ]:




