/*
set 사용해서 체크해주기
*/

#include <vector>
#include <unordered_set>

using namespace std;

int solution(vector<int> nums) {
    int answer = 0;
    int cnt = 0;
    unordered_set<int> hash;
    
    for(int i=0; i<nums.size(); i++) {
        hash.insert(nums[i]);
    }
    
    if(nums.size() / 2 < hash.size()) {
        answer = nums.size() / 2;
    }
    else answer = hash.size();
    
    return answer;
}