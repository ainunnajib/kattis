#include <iostream>
using namespace std;

int main()
{
  int t;
  cin >> t;

  int l[t];
  for (int i = 0; i < t; i++)
  {
    cin >> l[i];
  }

  int s[t], x;
  bool valid;
  for (int a = 0; a < 10001; a++)
  {
    for (int b = 0; b < 10001; b++)
    {
      valid = true;
      for (int i = 0; i < t-1; i++)
      {
        x = l[i];
        x = (a*x + b) % 10001;
        s[i] = x;
        x = (a*x + b) % 10001;
        if (l[i+1] != x)
        {
          valid = false;
          break;
        }
      }
      if (valid)
      {
        x = (a*x + b) % 10001;
        s[t-1] = x;
        for (int i = 0; i < t; i++)
        {
          cout << s[i] << endl;
        }
        break;
      }
    }
    if (valid) break;
  }
}
