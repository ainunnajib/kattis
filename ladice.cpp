#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> vi;

class UnionFind {                                // OOP style
private:
  vi p, rank, setSize, taken;                           // vi p is the key part
  int numSets;
public:
  UnionFind(int N) {
    p.assign(N, 0); for (int i = 0; i < N; ++i) p[i] = i;
    rank.assign(N, 0);                           // optional speedup
    setSize.assign(N, 1);                        // optional feature
    taken.assign(N, 0);
    numSets = N;                                 // optional feature
  }

  int findSet(int i) { return (p[i] == i) ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

  int numDisjointSets() { return numSets; }      // optional
  int sizeOfSet(int i) { return setSize[findSet(i)]; } // optional

  void unionSet(int i, int j) {
    if (isSameSet(i, j)) return;                 // i and j are in same set
    int x = findSet(i), y = findSet(j);          // find both rep items
    if (rank[x] > rank[y]) swap(x, y);           // keep x 'shorter' than y
    p[x] = y;                                    // set x under y
    if (rank[x] == rank[y]) ++rank[y];           // optional speedup
    setSize[y] += setSize[x];                    // combine set sizes at y
    taken[y] += taken[x];
    --numSets;                                   // a union reduces numSets
  }
  
  bool takeslot(int i) {
	int x = findSet(i);
	if (setSize[x] > taken[x]) { taken[x] = taken[x] + 1; return true; }
	else return false;  
  }
};


int main(){
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
