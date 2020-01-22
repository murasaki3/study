#--------calc EER------------------------------
#n_theta = 0# しきい値の番号
w_theta = 0.01
score_list = []
ans_label_list = []
num_genuine = 1001
num_spoof = 200
n_lst = num_genuine + num_spoof
i = 0
th = 0
FAR_list = []
FRR_list = []

for i in range(n_lst):
    score_list.append(1)

for i in range(num_genuine):
    ans_label_list.append(1)

for i in range(num_spoof):
    ans_label_list.append(0)


for th in range(int(1/w_theta)):#1/w_theta

    FA = 0
    FR = 0
    for i in range(n_lst):
        if ans_label_list[i] == 1 and score_list[i] < w_theta*th:
            FR = FR + 1
        elif ans_label_list[i] == 0 and score_list[i] > w_theta*th:
            FA = FA + 1


    FAR = FA / num_spoof
    FRR = FR / num_genuine

            
    FAR_list.append(FAR)
    FRR_list.append(FRR)
    #print('FAR :')
    #print(FAR)
    #print('FRR :')
    #print(FRR)
        
    if FAR == FRR:
        EER = FAR
        print(EER)
    elif FAR < FRR:
        ax=bx=w_theta*(th-1)
        ay=FAR_list[th-1]
        by=FRR_list[th-1]
        cx=dx=w_theta*th
        cy=FRR_list[th]
        dy=FAR_list[th]

        sx=ax+abs(cx-ax)*(abs(ay-by)/(abs(ay-by)+abs(cy-dy)))
        EER=(((ay-dy)/(ax-dx))*(sx-ax))+ay
        print('EER is...')
        print(EER)
        with open("kekka.txt", "w") as f:
            print(EER, file=f)
        break
