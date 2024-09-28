'''
스킬트리 돌면서 이전 스킬을 배웠는지 체크. 배우지 않았다면 return
'''

from collections import defaultdict

def solution(skills, skill_trees):
    answer = 0
    skill_dict = defaultdict(int)
    for s in range(1, len(skills) + 1):
        skill_dict[skills[s - 1]] = s
    
    for skill in skill_trees:
        tmp = 1     # 몇 번쨰 스킬인지 체크
        for s in range(1, len(skill) + 1):
            if skill_dict[skill[s - 1]]:
                if skill_dict[skill[s - 1]] <= tmp:
                    tmp += 1
                else:
                    break
        else:
            answer += 1
                
    return answer