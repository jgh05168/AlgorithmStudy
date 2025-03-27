/*
채팅창에 누군가 들어오고 나갈 때마다 닉네임이 출력된다.
[닉네임 변경 방법]
1. 방을 나간 후, 새로운 닉네임으로 들어온다
2. 채팅방에서 닉네임을 변경한다.

- 나갔다가 닉네임 바꿔서 다시 들어올 경우, 기존에 채팅방에 남아있던 이름도 바뀐 이름으로 변경된다.
- 중복 닉네임 허용

풀이 : 해시맵
길이 <= 10만
uid 정보가 주어짐 => 해시맵에 닉네임 정보와 함께 저장
enter 나올 땐 uid 정보 변경 & result에 uid 저장
leave에는 uid 정보 변경하지 말고 그냥 놔두기
change도 uid 변경
*/

#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<string, string> log_info;

vector<string> solution(vector<string> records) {
    vector<string> answer;
    vector<pair<int, string>> uid_list;
    
    // 기록 확인하기
    for (auto record : records){
        // 문자열 split
        int start = 0;
        int end;
        string tmp;
        vector<string> record_list;
        while ((end = record.find(' ', start)) != -1 ){
            int str_len = end - start;
            tmp = record.substr(start, str_len);
            record_list.push_back(tmp);
            start = end + 1;
        }
        tmp = record.substr(start);
        record_list.push_back(tmp);
        
        // 분기 시작
        if (record_list[0] == "Enter"){
            log_info[record_list[1]] = record_list[2];
            uid_list.push_back({1, record_list[1]});
        }
        else if (record_list[0] == "Leave"){
            uid_list.push_back({2, record_list[1]});
        }
        else {
            log_info[record_list[1]] = record_list[2];
        }
    }
    
    // 결과 출력하기
    string tmp;
    for (auto log : uid_list){
        tmp = log_info[log.second];
        if (log.first == 1) {
            tmp += "님이 들어왔습니다.";
            answer.push_back(tmp);
        }
        else {
            tmp += "님이 나갔습니다.";
            answer.push_back(tmp);
        }
    }
    
    return answer;
}   