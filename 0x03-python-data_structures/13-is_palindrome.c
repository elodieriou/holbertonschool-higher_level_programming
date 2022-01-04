#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int check_listint(listint_t *head1, listint_t *head2);

/**
 * is_palindrome - function that chacks if a singly linked list is a palindrome
 * @head: a pointer to a pointer pointed to the beginning of a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node1 = *head, *node2 = *head, *prev = *head;
	listint_t *tmp = NULL, *mid = NULL;
	int result;

	if (head)
		return (1);

	while (node1 && node2->next)
	{
		node2 = node2->next->next;
		prev = node1;
		node1 = node1->next;
	}

	if (node2 != NULL)
	{
		tmp = node1;
		node1 = node1->next;
	}

	prev->next = NULL;
	reverse_listint(&node1);
	mid = node1;
	node2 = *head;

	result = check_listint(*head, mid);
	reverse_listint(&mid);

	if (tmp != NULL)
	{
		prev->next = tmp;
		tmp->next = mid;
	}

	return (result);
}

/**
 * reverse_listint - function that reverse a linked list
 * @head: a pointer to a pointer pointed to the beginning of a linked list
 * Return: the beginning of a linked list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL,  *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	*head = prev;
	return (*head);
}

/**
 * check_listint - function that check if two node have same data
 * @head1: a pointer to the beginning of the first list
 * @head2: a pointer to the beginning of the second list
 * Return: 0 if it isn't a palindrome, 1 if it is a palindrome
 */
int check_listint(listint_t *head1, listint_t *head2)
{
	listint_t *tmp1 = head1, *tmp2 = head2;

	while (tmp1 && tmp2)
	{
		if (tmp1->n != tmp2->n)
			return (0);
		tmp1 = tmp1->next;
		tmp2 = tmp2->next;
	}
	if (tmp1 == NULL && tmp2 == NULL)
		return (1);
	return (0);
}
