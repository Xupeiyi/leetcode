#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
	string reverseStr(string s, int k) {
		for (size_t i = 0; i < s.size(); i += 2 * k) {
			size_t start = i;
			size_t end = i + k - 1 < s.size() ? i + k - 1 : s.size()-1;
			while (start < end) {
				char tmp = s[start];
				s[start] = s[end];
				s[end] = tmp;
				start++;
				end--;
			}
		}
		return s;
	}
};

int main(){
	Solution s;
	cout << s.reverseStr("abcdefg", 10);
}

