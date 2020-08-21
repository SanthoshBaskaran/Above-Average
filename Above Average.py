test_case=int(input())
solution=[]
solution_list=""
average=0
count=0
for i in range(test_case):
    people_input=list(map(int,input().split()))
    people_input.remove(people_input[0])
    for j in people_input:
        average=average+j
    solution_list=(average/len(people_input))
    for k in people_input:
        if(k>solution_list):
            count=count+1
    solution_list=0
    solution_list=solution_list+float(count/len(people_input)*100)
    x=(format(solution_list,'.3f'))
    str(x)
    x=x+"%"
    solution.append(x)
    people_input.clear()
    count=0
    solution_list=0
    average=0
for s in solution:
    print(s)
    
