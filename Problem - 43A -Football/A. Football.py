# l3  = list(map(int, input().split()))
# l4 = input().strip().split()
# i5,i6 = map(int,input().split())
# t = int(input().strip())





n = int(input())
Lines_list = []
for i in range(n):
    line = input().strip()
    Lines_list.append(line)
Teams = set(Lines_list)
teams_list = list(Teams)
if len(teams_list) > 1 :
    Team1_goals = Lines_list.count(teams_list[0])
    Team2_goals = Lines_list.count(teams_list[1])

    if Team1_goals > Team2_goals:
        print(teams_list[0])
    else:
        print(teams_list[1])
else:
    print(teams_list[0])















