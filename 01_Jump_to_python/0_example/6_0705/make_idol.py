def show_candidates(candidate_list):
    print(candidate_list)
    make_idol(candidate_list)
def make_idol(candidate_list):
    for line in candidate_list:
        print("신예 아이돌 %s 인기 급상승"% line)
    make_world_star(candidate_list)
def make_world_star(candidate_list):
    for line in candidate_list:
        print("아이돌 %s 월드스타 등극"% line)

f = open("연습생.txt", "r", encoding="UTF-8")
line = f.readlines()
data_line = []
for i in line[:3]:
    data_line.append(i[:-1])
data_line2 = data_line + line[3:]
show_candidates(data_line2)
f.close()
