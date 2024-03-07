import sys; input = sys.stdin.readline

def main():
    while(1):
        try:
            # 0 input
            x = int(input()) * 10**7
            n = int(input())
            nums = [int(input()) for _ in range(n)]
            # 1 sort
            nums.sort()
            # 2 two pointer
            i = 0
            j = n - 1
            flag = False
            while (i < j):
                if nums[i] + nums[j] == x:
                    flag = True
                    break
                elif nums[i] + nums[j] < x:
                    i+=1
                else:
                    j-=1;
            # 3 output
            if flag:
                print("yes", nums[i], nums[j])
            else:
                print("danger")
        except:
            break
    return 

if __name__ == "__main__":
    main()