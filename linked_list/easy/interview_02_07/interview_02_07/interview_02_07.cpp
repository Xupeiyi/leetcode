#include <iostream>

struct ListNode {
	int val;
	ListNode* next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}
	void print() {
		ListNode* curr = this;
		while (curr != NULL) {
			std::cout << curr->val << "->";
			curr = curr->next;
		}
		std::cout << std::endl;
	}
};

int findLength(ListNode* head) {
	int len = 0;
	while (head != NULL) {
		head = head->next;
		len++;
	}
	return len;
}
/*
class Solution {
public:
	ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
		// 1. find  length difference of list1 and list2
		int lenA = findLength(headA);
		int lenB = findLength(headB);
		int diff = lenB - lenA;
		
		// 2.  move the head of the longer list diff elements ahead
		while (diff > 0) {
			headB = headB->next;
			diff--;
		}
		while (diff < 0) {
			headA = headA->next;
			diff++;
		}
		// 3. move headA and headB together, 
		// if they point at the same node, return true
		while (headA != NULL) {
			if (headA == headB) {
				return headA;
			}
			headA = headA->next;
			headB = headB->next;
		}
		return NULL;
	}
};
*/

class Solution {
public:
	ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
		ListNode* a = headA;
		ListNode* b = headB;
		while (a != b)
		{
			a = a != nullptr ? a->next : headB;
			b = b != nullptr ? b->next : headA;
		}
		return a;
	}
};



int main(){
	Solution s;
	
	ListNode* n0 = new ListNode(5);
	ListNode* n1 = new ListNode(4, n0);
	ListNode* n2 = new ListNode(8, n1);
	// list a
	ListNode* n3 = new ListNode(1, n2);
	ListNode* n6 = new ListNode(4, n3);
	ListNode* n7 = new ListNode(2, n6);
	n7->print();

	// list b
	ListNode* n4 = new ListNode(1, n2);
	ListNode* n5 = new ListNode(0, n4);
	n5->print();

	s.getIntersectionNode(n3, n5)->print();
}

