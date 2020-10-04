#include <iostream>
#include <bitset>

using namespace std;

int main()
{
  int _;
  long n, q, i, x;
  _ = scanf("%ld %ld\n", &n, &q);

  bitset<50000001> isnotprime;
  isnotprime[0] = 1;
  for (i = 2; i <= n; i++)
  {
    if (i%2 == 0 and i > 2) continue;
    if (!isnotprime[int(i/2)])
      for (x = i*i; x <= n; x += i)
        if (x % 2 == 1)
          isnotprime[int(x/2)] = 1;
  }

  long count = 1;
  for (i = 3; i <= n; i += 2)
    if (!isnotprime[int(i/2)])
      count++;

  if (n > 1) printf("%ld\n", count);
  else printf("0\n");

  for (i = 0; i < q; i++)
  {
    _ = scanf("%ld\n", &x);
    if (x == 2) printf("1\n");
    else if (x % 2 == 0) printf("0\n");
    else printf("%d\n", (1 - isnotprime[int(x/2)]));
  }
}
