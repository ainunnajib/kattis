#include <iostream>
#include <math.h>
using namespace std;

int main()
{
  int n, m;
  cin >> n >> m;

  bool valid[1048576];
  int MAX = pow(2, n);
  for (int i = 0; i < MAX; i++) valid[i] = true;

  int a, b, x;
  for (int _ = 0; _ < m; _++)
  {
    cin >> a >> b;
    a--;
    b--;
    x = pow(2, a) + pow(2, b);
    for (int i = 0; i < MAX; i++)
      if ((x & i) == x) valid[i] = false;
  }

  int count = 0;
  for (int i = 0; i < MAX; i++) if (valid[i]) count++;
  cout << count << endl;
}
