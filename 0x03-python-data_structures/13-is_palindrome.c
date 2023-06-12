#include "lists.h"

listint_t *list_rev(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * list_rev - a C function that change the direction of the list.
 * @head: pointer to the beggining node of the list
 * Return: head of the reversed list
 */
listint_t *list_rev(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - a C function that verify if a list is a palindrome
 * @head: pointer to the head of list
 * Return: if a palindrome, 1, if not, 0
 **/

int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *rev = NULL;
	listint_t *mid = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast)
		slow = slow->next;

	rev = list_rev(&slow);
	mid = rev;

	while (rev && tmp)
	{
		if (rev->n != tmp->n)
		{
			list_rev(&mid);
			return (0);
		}
		rev = rev->next;
		tmp = tmp->next;
	}

	list_rev(&mid);

	return (1);
}
