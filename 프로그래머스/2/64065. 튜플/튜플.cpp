/*
튜플의 성질 :
1. 중복된 원소가 있을 수 있음
2. 운소에 정해진 순서가 있으며, 순서가 다르면 서로 다른 튜플임
3. 튜플의 원소 개수는 유한하다

중복되는 원소가 없는 튜플 이 주어질 때, 집합 기호를 이용해 표현 가능함

풀이 : set 사용하면 풀리는거 아닌가 ..

*/

#include <string>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

bool cmp(vector<int> a, vector<int> b){
    return a.size() < b.size();
}

int dat[1000001] = {0, };

vector<int> solution(string s) {
    vector<int> answer;
    
    string num = "";
    vector<int> tmp;
    vector<vector<int>> comb;
    for (int i=0;i<s.size();i++){
        if (0 <= s[i] - '0' && s[i] - '0' < 10){
            num += s[i];
        }
        else if (s[i] == ','){
            if (num == "")
                continue;
            if (!dat[stoi(num)])
                dat[stoi(num)] = 1;
            tmp.push_back(stoi(num));
            num = "";
        }
        else if (s[i] == '}'){
            if (tmp.size() > 0 && num.size() == 0){
                comb.push_back(tmp);
                tmp.clear();
            }
            else if (num.size() > 0){
                tmp.push_back(stoi(num));
                num = "";
                comb.push_back(tmp);
                tmp.clear();
            }
        }
    }
    
    sort(comb.begin(), comb.end(), cmp);
    memset(dat, 0, sizeof(dat));
    
    for (auto arr : comb){
        for (auto num : arr){
            if (!dat[num]){
                answer.push_back(num);
                dat[num]++;
            }
        }
    }
    
//     for (auto num : answer)
//         cout << num << ' '; 
    return answer;
}