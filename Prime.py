print("These are all the prime numbers between 1 and 100:")
for num in range(100):# for all numbers up to 100 do the following:
    if num > 1:# if "num" is larger than 1 do the following:
        for n in range(2,num):# for "n" between 2 and "num" do the following:
            #print("num = "+ str(num) + "  n = "+ str(n))# this is for logs
            #str makes the numbers printable in the same line as text(str=text)
            #print("n = "+ str(n))
            if (num % n) == 0:# if "num" divided by "n" is equal to 0(not prime)
                break# starts the above again from 2 until a new prime is found
#full command example:
#num = 6,N = 2. 6%2=3 not prime, next, num=7, n=2. 7%2=3.5, n=3 etc until n>num
        else:
            print(int(num), end="|")#if "num" is not equal to 0(prime) print "num"
#print() = to show something on the screen.
