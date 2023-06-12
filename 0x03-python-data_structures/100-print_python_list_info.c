#include <Python.h>

/**
 * print_python_list_info - a C function that prints some basic info
 * about Python lists
 * @p: the PyObject list
 **/

void print_python_list_info(PyObject *p)
{
	int size, alloc, x;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	x = 0;
	while (x < size)
	{
		printf("Element %d: ", x);

		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);

		x++;
	}
}
