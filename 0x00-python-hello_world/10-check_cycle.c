#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: a pointer to a linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node2 = list;

	if (list == NULL || list->next == NULL)
		return (0);
	node2 = list->next->next;
	list = list->next;
	while(list != NULL && list->next != NULL && node2 != NULL)
	{
		if (list == node2)
			return (1);
		list = list->next;
		node2 = node2->next->next;
	}
	return (0);
}
