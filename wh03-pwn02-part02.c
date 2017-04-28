#include <stdio.h>
#include <time.h>

int main()
{
        srand(time(0));
        printf("%d\n%d\n",576,rand());
        return 0;
}

/* gcc wh03-pwn02-part02.c; ./a.out |  nc 103.237.98.32 25032

I have two secret numbers, I like you guessing them. Are you ready?

        The first challenge: guessing one,
Enter your number:Well done! The secret numer is 576. Pass challenge 2 to get the flag

        Challenge 2: Guessing the second
Now,Guessing the second one. I use srand() function in C with argument time(0).
Enter your number:
Amazing !You are right. Flag is: Life_is_a_story_make_yours_the_best_seller.
*/
