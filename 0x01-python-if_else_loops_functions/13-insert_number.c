#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - a C function that inserts number into
 * sorted singly-linked list
 * @head: pointer to the head of list
 * @number: number to be inserted
 *
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (1)
	{
		if (node && node->next && node->next->n < number)
		{
			node = node->next;
		}
		else
		{
			new_node->next = node->next;
			node->next = new_node;
			break;
		}
	}

	return (new_node);
}
