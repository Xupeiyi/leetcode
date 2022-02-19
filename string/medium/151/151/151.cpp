#include <iostream>
#include <string>

using namespace std;

void removeExtraSpaces(string& s) {
	size_t slow = 0;
	size_t fast = 0;

	// remove all spaces before the first letter
	while (s[fast] == ' ') {
		fast++;
	}

	while (fast < s.size()) {
		// s[fast] is not the first element of a sequence of spaces
		if (fast > 0 && s[fast] == s[fast - 1] && s[fast] == ' ') {
			fast++;
			continue;
		}
		s[slow++] = s[fast++];
	}

	// remove the space after the last letter (there will be at most one)
	if (slow > 0 && s[slow - 1] == ' ') {
		slow--;
	}

	s.resize(slow);
}


void reverseString(string& s, size_t start, size_t end) {
	if (start == end) {
		return;
	}

	while (start < end) {
		char tmp = s[start];
		s[start] = s[end];
		s[end] = tmp;
		start++;
		end--;
	}
}

class Solution {
public:
	string reverseWords(string s) {
		removeExtraSpaces(s);
		if (s.size() == 0) {
			return s;
		}
		reverseString(s, 0, s.size() - 1);
		size_t start = 0;
		size_t end = 0;
		while (end < s.size()) {
			// when end is at the end of a word
			if (end == s.size() - 1 || s[end+1] == ' ') {
				reverseString(s, start, end);
				end += 2;
				start = end;
			}
			else{
				end++;
			}
		}
		return s;
	}
};


int main(){
	Solution s;
	string a("F R I E  N   D    S  ");
	cout << s.reverseWords(a) << endl;
}


