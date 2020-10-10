#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> vi;

class UnionFind {
private:
  vi p, rank, setSize, taken;
  int numSets;
public:
  UnionFind(int N) {
    p.assign(N, 0); for (int i = 0; i < N; ++i) p[i] = i;
    rank.assign(N, 0);
    setSize.assign(N, 1);
    taken.assign(N, 0);
    numSets = N;
  }

  int findSet(int i) { return (p[i] == i) ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

  int numDisjointSets() { return numSets; }
  int sizeOfSet(int i) { return setSize[findSet(i)]; }

  void unionSet(int i, int j) {
    if (isSameSet(i, j)) return;
    int x = findSet(i), y = findSet(j);
    if (rank[x] > rank[y]) swap(x, y);
    p[x] = y;
    if (rank[x] == rank[y]) ++rank[y];
    setSize[y] += setSize[x];
    taken[y] += taken[x];
    --numSets;
  }

  bool takeslot(int i) {
	int x = findSet(i);
	if (setSize[x] > taken[x]) { taken[x] = taken[x] + 1; return true; }
	else return false;
  }
};


int main()
{
	int n, l, a, b;
	cin >> n >> l;

	UnionFind u(l);

	for (int i = 0; i < n; i++)
	{
		cin >> a >> b;
		a--;
		b--;

		u.unionSet(a, b);
		bool success = u.takeslot(a);
		if (success) { cout << "LADICA" << endl; }
		else { cout << "SMECE" << endl; }
	}
}
