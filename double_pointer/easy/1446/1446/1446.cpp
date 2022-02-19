#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
	int maxPower(string s) {
		int length = (int)s.size();
		if (length == 1) return 1;
		int max = 0;
		int i = 0;
		for (int j = 1; j < s.size(); j++) {
			if (s[j] != s[j - 1]) {
				max = j - i > max ? j - i : max;
				i = j;
			}
		}
		return  length - i > max ? length - i : max;
	}
};

int main(){
	Solution s;
	cout << s.maxPower("leeetcodeeeeeee");
}

