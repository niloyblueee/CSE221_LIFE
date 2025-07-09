
n = int(input())
s = []
for idx in range(n):
    s.append(input())


s.sort(key=lambda x: x.split()[0])


lexico = s.copy()  

for idx in range(n):
    for idx2 in range(idx+1, n):
        
        if lexico[idx].split()[0] == lexico[idx2].split()[0]:
            
            hour1, min1 = map(int, lexico[idx].split()[-1].split(':'))
            hour2, min2 = map(int, lexico[idx2].split()[-1].split(':'))
            
          
            if hour1 < hour2 or (hour1 == hour2 and min1 < min2):
                lexico[idx], lexico[idx2] = lexico[idx2], lexico[idx]
           

for _ in lexico:
    print(_, end=("\n"))