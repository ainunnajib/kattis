#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
  unordered_map<int, int> d;
  unordered_map<int, int> x;

  int n;
  cin >> n;
  string l[100000];

  for (int i=0; i<n; i++) {
    cin >> l[i];
  }
  int a = 0, b = 0;
  for (int i=0; i<n-1; i++) {
    cin >> a >> b;
    a--;
    b--;

    if (x.count(a) == 0) x[a] = a;
    if (x.count(b) == 0) x[b] = b;

    d[x[a]] = b;
    x[a] = x[b];
  }

  cout << l[a];
  while (d.count(a) > 0)
  {
      a = d[a];
      cout << l[a];
  }
}
