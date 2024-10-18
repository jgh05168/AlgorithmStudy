#include <stdio.h>

int main(void)
{
	int a, b;

	while (scanf("%d %d", &a, &b) != EOF)
	{
		if ((0 < a < 10) && (0 < b < 10))
			printf("%d\n", a + b);
		else
			break;
	}

	return 0;
}