#include <iostream>
using namespace std;

int main() {
  int one, n;
  char slash;
  while (cin >> one >> slash >> n) {
    int ways = 0;
    int x = n + 1;
    int y = x;
    while(true) {
      if ((x*n) % (x-n) == 0) {
        y = x * n / (x-n);
        if (x <= y) {
          ways++;
        } else {
          break;
        }
      }
      if (x > y) {
        break;
      }
      x++;
    }
    cout << ways << endl;
  }
}
