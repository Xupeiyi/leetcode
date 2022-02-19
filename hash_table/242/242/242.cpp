#include <iostream>
#include <map>
#include <string>

using namespace std;

map<char, size_t> count(string s) {
	map<char, size_t> res;
	for (auto it = s.begin(); it != s.end();it++) {
		res[*it] ++;
	}
	return res;
}

class Solution {
public:
	bool isAnagram(string s, string t) {
		map<char, size_t> count_s = count(s);
		map<char, size_t> count_t = count(t);
		if (count_s.size() != count_t.size()) {
			return false;
		}
		for (auto it = count_s.begin(); it != count_s.end(); it++) {
			char key = it->first;
			if (count_s[key] != count_t[key]) {
				return false;
			}
		}
		return true;
	}
};


int main(){
	Solution s;
	cout << s.isAnagram("abcdefa", "aabcdef") <<endl;
	cout << s.isAnagram("abc", "abd") << endl;
}

