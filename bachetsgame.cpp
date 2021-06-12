#include <iostream>
using namespace std;

int main() {
    int n, m;
    while(cin >> n >> m){
        int moves[10];
        for(int i=0; i<m; i++){
            cin >> moves[i];
        }

        bool dp[1000001];
        dp[0] = false;
        for(int i=1; i<=n; i++){
            dp[i] = false;
            for(int j=0; j<m; j++){
                if(i>=moves[j] && !dp[i-moves[j]]){
                    dp[i] = true;
                    break;
                }
            }
        }

        if(dp[n]){
            cout << "Stan wins" << endl;
        } else {
            cout << "Ollie wins" << endl;
        }
    }
}