#include <iostream>

struct ListNode {
	int val;
	ListNode* next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
	ListNode* detectCycle(ListNode* head) {

		ListNode* slow = head;
		ListNode* fast = head;

		do {
			if (fast == NULL || fast->next == NULL) {
				return NULL;
			}
			slow = slow->next;
			fast = fast->next->next;
		} while (slow != fast);

		ListNode* curr = head;
		while (curr != slow) {
			curr = curr->next;
			slow = slow->next;
		}
		return curr;
	}
};


int main(){
	Solution s;
	ListNode* n0 = new ListNode(-4);
	ListNode* n1 = new ListNode(0, n0);
	ListNode* n2 = new ListNode(2, n1);
	ListNode* n3 = new ListNode(3, n2);
	n0->next = n3;
	ListNode* n5 = new ListNode(5, n3);

	ListNode* ans = s.detectCycle(n5);
	std::cout << ans->val << std::endl;
}

