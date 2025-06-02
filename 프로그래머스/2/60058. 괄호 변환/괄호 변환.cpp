/*
작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로 작성됨

모든 괄호를 뽑아서 올바른 순서대로 배치된 문자열을 알려주자


*/

#include <string>
#include <vector>
#include <iostream>

using namespace std;

string getString(string p){
    if (p == "")
        return "";
    
    string u = "";
    string v = "";
    string ret = "";
    
    cout << p << '\n';
    
    int l = 0, r = 0;
    int flag = 0;
    for (auto s : p){
        if (!flag){
            if (s == '(')
                l++;
            else
                r++;
            u += s;
            if (l == r)
                flag = 1;
        }
        else {
            v += s;   
        }
    }
    
    cout << u << ' ' << v << '\n';
    
    // 올바른 괄호 문자열인지 체크
    vector<char> stack_list;
    flag = 0;
    for (auto s : u){
        if (s == '(')
            stack_list.push_back(s);
        else {
            if (stack_list.empty()){
                flag = 1;
                break;
            }
        }
    }
    
    cout << flag << '\n';
    // u가 올바른 괄호 문자열이라면
    if (!flag){
        ret += u;
        ret += getString(v);
    }
    else {
        ret += '(';
        ret += getString(v);
        ret += ')';
        
        u.erase(0, 1);
        u.erase(u.size() - 1, 1);
        
        for (auto s : u){
            if (s == '(')
                ret += ')';
            else
                ret += '(';
        }
    }
    
    return ret;
}


string solution(string p) {
    string answer = "";
    
    answer = getString(p);
    
    return answer;
}