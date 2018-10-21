def fibo(n):
    arr=[0]*(n+1)
    if n == 1 or n == 0:
        return 1
    arr[1]=1
    arr[2]=1
    for i in range(3,n+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[n]


if __name__=='__main__':
    while(True):
        try:
            user_input=input('Enter a number: ')
            if  'exit' not in str(user_input):
                print(fibo(user_input)) 
            else:
                break
        except KeyboardInterrupt:
            print('\nExiting')
            break