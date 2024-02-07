def solution(spell, dic):
    # 빈 문자열에 dic 쪼개서 추가 후 이차원 배열로 단어 추가
    bin = []
    for i in dic:
        temp = []
        for j in i:
            temp.append(j)
        bin.append(temp)
    
    # 정렬 된 리스트끼리 비교 
    clean = []
    for z in bin:
        clean.append(sorted(z))
    
    spell = sorted(spell)

    if spell in clean : 
        return 1
    else: return 2
        

print(solution(["z", "d", "x"],	["def", "dww", "dzx", "loveaw"]))