#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
	string replaceSpace(string s) {
		int count = 0; // space num
		int length = (int)s.size();
		for (int i = 0; i < length; i++) {
			if (s[i] == ' ') count++;
		}
		s.resize(length + 2 * count);
		for (int i = length - 1,  j = (int)s.size() - 1; i < j; i--, j--) {
			if (s[i] != ' ') s[j] = s[i];
			else {
				s[j] = '0';
				s[j - 1] = '2';
				s[j - 2] = '%';
				j -= 2;
			}
		}
		return s;
	}
};

int main(){
	Solution s;
	cout << s.replaceSpace("We are happy");
}


