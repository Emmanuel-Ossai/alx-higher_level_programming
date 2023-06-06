#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - a C function that checks if a linked list contains cycle
 * @list: the list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	if (!list)
		return (0);

	listint_t *ptr1 = list;
	listint_t *ptr2 = list;

	do {
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;

		if (ptr2)
			ptr2 = ptr2->next;
		else
			break;
	} while (ptr2 && ptr1 && ptr2 != ptr1);

	return (ptr2 == ptr1);
}
