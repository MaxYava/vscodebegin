#include <iostream>
#include <locale>

float a, b, c;
char d;
int p;
int main()
{

    while (p != 2)
    {
        printf("1 = calculator \n 2 - exit \n");
        scanf("%d", &p);
        switch (p)
        {
        case 1:
        {
            float c;
            printf("First number ");
            scanf("%d", &a);
            printf("Action with numbers ");
            scanf("%s", &d);
            printf("Second number ");
            scanf("%d", &b);
            if (d == '+')
                c = a + b;
            if (d == '-')
                c = a - b;
            if (d == '*')
                c = a * b;
            if (d == '/')
                c = a / b;
            system("cls");
        }
        case 2:
        {
            break;
        }
        }
        printf("Result = %2.f \n", c);
    }
}