def runner_up(arr):
    a = max(arr)
    for i in range(len(arr)):
        if arr[i] == a:        
            arr.remove(a)  #remove all the maximum values. There can be more than one
    return max(arr)
 
size_of_arr = int(input())
arr = map(int, input().split())
print (runner_up(arr))