def MissingNumber(n):

   
    m = len(n) + 1

  
    total = m * (m + 1) // 2


    return total - sum(n)


if __name__ == '__main__':

    n= {1,2,4,6,3,7,8}

    print("The missing number is", MissingNumber(n))
