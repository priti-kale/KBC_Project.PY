que=[
    "1. who was the first female president in india",
    "2. when bhagat singh wrote his first letter in jail and how old he was that time",
    "3. what is the current calculation of population in the world",
    "4. where female population was very less  in the world in 2015",
    "5. what is the main festival of the world"
    ]
option=[
    ["1:indira gandhi","2:pratibha devisingh patil","3:swati mukharji","4:sarswati devi"],
    ["1:nov 1 1926(19 year)","2:jan 2 1921(20 year)","3:feb 30 1890(22 year)","4:mar 3 1987(25 year)"],
    ["1:7.96 (Billin people)","2:8.92(Billin people)","3:3.93 (Billian people)","4:2.93 (Billian people)"],
    ["1:United Arab Emirates only 26.7%","2:iran only 23.1%","3:UK only 20.3%","4:netherland only 21.5%"],
    ["1:Carnival in Rio de Janeiro","2:dewali","3:Deventer Book Fair","4:Berlin Love Parade","Edinburgh Fringe Festival",]]

solution=[2,1,1,1,1]
lifeline=[["2: pratibha devisingh patil","3: swati mukharji"],
["1: nov 1 1992(19 year)","4: mar 3 1987(25 year)"],
["1: 7.96% Billion people","3: 3.93 Billion people"],
["1: United Arab Emirates only 26.7%","2: iran only 23.1%"],
["1: Carnival in Rio de janerio","3: Berlin Love parade"]]
money=0
life_line=2
def ques():
    if len(que)>0:
        i=0
        while i<1:
            print(que[i])
            que.remove(que[i])
            i=i+1
        opt()
    else:
        print("Take your prise",money)
        print("THANK YOU")
def opt():
    j=0
    while j<1:
        for i in option[j]:
            print("   ",i)
        option.remove(option[j])
        j=j+1
    lif()
def ans():
    global money
    answer=int(input("enter the answer"))
    if answer==1 or answer==2 or answer==3 or answer==4:
        k=0
        while k<1:
            if answer==solution[k]:
                money+=1000
                print("    answer is correct")
                solution.remove(solution[k])
                ques()
            else:
                print("        wrong answer:-" )
                print("        answer is",solution[k])
                solution.remove(solution[k])
                ques()
            k=k+1
    else:
        print("enter valid answer in 1,2 ,3,4:-")
        ans()
def lif():
    global life_line
    if life_line>0:
        l=0
        while l<1:
            life=input("enter the lifeline:-")
            if life=="yes":
                life_line-=1
                for i in lifeline[l]:
                    print("    ",i)
                lifeline.remove(lifeline[l])
                ans()
            elif life=="no":
                lifeline.remove(lifeline[l])
                ans()
            else:
                print("Tell anser  yes or no:-")    
                lif()
    else:
        print("you can't take lifeline:-")
        lifeline.pop(0)
        ans()
ques()




























