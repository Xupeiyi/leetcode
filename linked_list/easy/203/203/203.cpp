#include <cstdio>

 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
	ListNode* removeAll(const int& data, ListNode* current) {
		if (current == NULL) {
			return NULL;
		}
		if (data == current->val) {
			ListNode* ans = removeAll(data, current->next);
			delete current;
			return ans;
		}
		current->next = removeAll(data, current->next);
		return current;
	}
	ListNode* removeElements(ListNode* head, int val) {
		head = removeAll(val, head);
		return head;
	}
};