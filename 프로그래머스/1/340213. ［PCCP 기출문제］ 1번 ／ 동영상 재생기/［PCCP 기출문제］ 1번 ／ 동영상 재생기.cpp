#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int videoLen, pos, opStart, opEnd;

bool IsOp(int position) {
    if (opStart <= position && position < opEnd) 
        return true;
    else 
        return false;
}

string solution(string video_len, string position, string op_start, string op_end, vector<string> commands) {
    //초로 초기화
    videoLen = 60 * stoi(video_len.substr(0, 2)) + stoi(video_len.substr(3, 5));
    pos = 60 * stoi(position.substr(0, 2)) + stoi(position.substr(3, 5));
    opStart = 60 * stoi(op_start.substr(0, 2)) + stoi(op_start.substr(3, 5));
    opEnd = 60 * stoi(op_end.substr(0, 2)) + stoi(op_end.substr(3, 5));

    if (IsOp(pos)) {
        pos = opEnd;
    }

    for(string& comm : commands) {
        if (comm == "next") {
            pos = min(videoLen, pos + 10);
            if (IsOp(pos)) {
                pos = opEnd;
            }
        }
        else if (comm == "prev") {
            pos = max(0, pos - 10);
            if (IsOp(pos)) {
                pos = opEnd;
            }
        }
    }

    // 시간 변환
    int tmp;
    tmp = pos / 60;
    string mm = (tmp < 10 ? "0" : "") + to_string(tmp);
    tmp = pos % 60;
    string ss = (tmp < 10 ? "0" : "") + to_string(tmp);
    string result = mm + ":" + ss;
    
    return result;
}