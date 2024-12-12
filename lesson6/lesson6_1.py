import random

def main():
    set1:set = set()
    #mysetliis:list =[]
    while len(set1)<7:
        myrandom = random.randint(1,49)
        set1.add(myrandom)
        if len(set1) == 7:
            SpecialNum = myrandom
            set1.remove(SpecialNum)
            mysetlist = sorted(set1)
            break
    mysetlist.append(SpecialNum)

    print("本期大樂透電腦選號號碼如下")
    for num in mysetlist:
        print(num,end=" ")
    print()
    print(f'特別號：{SpecialNum}')
if __name__ == '__main__':
    main()