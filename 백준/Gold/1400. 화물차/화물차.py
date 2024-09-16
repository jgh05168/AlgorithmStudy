'''
출발지 -> 짐 싣고 -> 도착지
동 서 남 북
A : 출발지, B : 배송지
. : 진입 금지
# : 각 도로
숫자 : 신호둥에 의해 제어되는 교차로
    - 교차로는 적어도 세 개의 도로 셀과 인접하다
    - 0 ~ 9로 표시된다.
    - k번호의 교차로라면, 0 ~ k까지의 교차로가 존재함
이동 :
- 차량의 이동, 차량이 어떤 위치에서 멈춰 서 있는 시간도 단위 시간으로 측정
- 화물차 진입 방향에 파란불이 켜져 있을 때만 교차로 진입이 가능함.
    - 교차로에 들어간 차량은 언제든지 임의의 방향으로 나갈 수 있다.
- 신호등은 동서 / 남북 두 개의 신호가 주기적으로 켜진다.
    - 초기에는 동서 / 남북 방향이 될 수 있다.
    - 교차로의 신호 주기 : 동서 방향의 시간이 a시간 켜지고, 남북 방향의 신호가 b시간 켜진다.

풀이:
bfs
bfs에 들어가는 단위 시간과 교차로의 시간을 잘 파악해야 한다.
    - 교차로 시간을 수학적으로 어떻게 풀지 ?
        -> a + b를 한 다음, 현재 이동 거리에서 나눠보자.
        -> 나머지값이 a 이내라면 동서, 아니라면 남북 이 열린 것
===================================================================
그냥 안풀려서 원초적인 방식으로 수동으로 교차로 바꿔주기
'''
#백준 1400번 화물차
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]

while True:
    m,n=map(int,input().split())
    if m==0 and n==0:
        break
    room=[]

    visited=[[False]*n for _ in range(m)]
    sx,sy=0,0
    ex,ey=0,0
    answer=1e9
    color=0
    coloring=[False for _ in range(10)]
    for x in range(m):
        tmp=input().rstrip()
        for y in range(n):
            if tmp[y]=='A':
                sx,sy=x,y
            elif tmp[y]=='B':
                ex,ey=x,y
            elif "0"<=tmp[y]<="9":
                color+=1
        room.append(tmp)
    for _ in range(color):
        lo=input().split()
        if lo[1]=='-':
            coloring[int(lo[0])]={'dir':lo[1] ,'a':int(lo[2]),'b':int(lo[3])+int(lo[2]),'sum':int(lo[3])+int(lo[2])}
        else:
            coloring[int(lo[0])]={'dir':lo[1],'a':int(lo[2])+int(lo[3]),'b':int(lo[3]),'sum':int(lo[3])+int(lo[2])}

    q=deque()
    q.append([sx,sy])
    visited[sx][sy]=True
    time=0
    out=False
    while q:
        size=len(q)
        time+=1
        while size:
            x,y=q.popleft()


            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]

                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                if visited[nx][ny]==True:
                    continue
                if room[nx][ny]=='.':
                    continue


                if room[nx][ny]=='#':
                    visited[nx][ny]=True
                    q.append([nx,ny])

                elif "0"<=room[nx][ny]<="9":
                    num=int(room[nx][ny])

                    if d<2:
                        if coloring[num]['dir']=='-':
                            visited[nx][ny]=True
                            q.append([nx,ny])
                    #방향이 다르면 대기했다가 건너기
                        else:
                            q.append([x,y])
                    else:
                        if coloring[num]['dir'] == '|':
                            visited[nx][ny] = True
                            q.append([nx, ny])
                        # 방향이 다르면 대기했다가 건너기
                        else:
                            q.append([x, y])
                else:
                    answer=time
                    out=True
                    break
            size-=1
        if out==True:
            break
        #신호등 하나하나 돌려주기
        for num in range(color):

            now_state=coloring[num]['dir']

            if now_state=='-':
                if time>=coloring[num]['a']:
                    coloring[num]['a']+=coloring[num]['sum']
                    coloring[num]['dir']='|'
            else:
                if time>=coloring[num]['b']:
                    coloring[num]['b']+=coloring[num]['sum']
                    coloring[num]['dir']='-'



    if answer==1e9:
        print("impossible")
    else:
        print(answer)
    p=input()