#include <iostream>
#include <vector>
#include <list>
using namespace std;


class MyHashSet {
private:
	vector<list<int>> data;
	static const int base = 769;
	static int hash(int key) {
		return key % base;
	}
public:
	/** Initialize your data structure here. */
	MyHashSet(): data(base) {}

	void add(int key) {
		int h = hash(key);
		/*若该元素已在表中，则返回*/
		for (auto it = data[h].begin(); it != data[h].end(); it++) {
			if ((*it) == key) {
				return;
			}
		}
		data[h].push_back(key);
	}

	void remove(int key) {
		int h = hash(key);
		for (auto it = data[h].begin(); it != data[h].end(); it++) {
			if ((*it) == key) {
				data[h].erase(it);
				return;
			}
		}
	}

	/** Returns true if this set contains the specified element */
	bool contains(int key) {
		int h = hash(key);
		for (auto it = data[h].begin(); it != data[h].end(); it++) {
			if ((*it) == key) {
				return true;
			}
		}
		return false;
	}
};

int main(){
	MyHashSet myHashSet = MyHashSet();
	myHashSet.add(1);      // set = [1]
	cout<<myHashSet.contains(1); // 返回 True
	myHashSet.add(2);      // set = [1, 2]
	cout<<myHashSet.contains(3); // 返回 False ，（未找到）
	myHashSet.add(2);      // set = [1, 2]
	cout<<myHashSet.contains(2); // 返回 True
	myHashSet.remove(2);   // set = [1]
	cout<<myHashSet.contains(2); // 返回 False ，（已移除）
}

