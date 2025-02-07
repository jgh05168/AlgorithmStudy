#include <iostream>
#include <unordered_map>
 
using namespace std;
 
int main(){
    
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int test_case;
    cin >> test_case;
    for(int t = 0; t<test_case; t++){
       
        int n;
        cin >> n;
        int answer =  1;
        
        if(n==0) answer = 0;
        else{
            unordered_map<string, int> umap;
            
            for(int i = 0; i<n; i++){
                string name, type;
                cin >> name >> type;
                if(umap.find(type) != umap.end()){          //이미 맵에 해당 종류 있으면
                    int cnt = umap[type];   //value
                    umap[type] = cnt+1;                     //그 종류의 가짓수 1 증가
                }
                else{
                    umap[type] = 1;
                   // umap.insert(make_pair(type,1));         //없으면 1로 초기화해서 추가
                }
            }
           
            unordered_map<string,int>::iterator it;
            for(it = umap.begin(); it!=umap.end(); it++){
                answer *= (it->second) + 1;
            }
            answer -= 1;
        }
        
        cout << answer << "\n";
    
    }
    
    return 0;
}