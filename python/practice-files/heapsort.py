def heapify(arr,n,root):
    largest=root
    l=root*2+1
    r=root*2+2
    
    if l<n and arr[largest]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest!=root:
        arr[largest],arr[root]=arr[root], arr[largest]
        heapify(arr,n,largest)

def heapsort(arr):
    #create a max heap
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr, n, i)
    for j in range(n-1,0,-1):
        arr[j],arr[0]=arr[0],arr[j]
        heapify(arr,j,0)
        
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
n = len(arr)
print("Sorted array is", end=' ')
for i in range(n):
    print(arr[i])
