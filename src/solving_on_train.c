#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    FILE *fp_1 = fopen(*(argv + 1), "r");
    if (argc != 2) // its 2 cause a.out input
    {
        fprintf(stderr, "usage: cant open filename\n");
        exit(1);
    }

    for (int i = 0; i < 11; i++)
    {
        char line[401];

        fgets(line, 401, fp_1);

        fprintf(stdout, "%s", line);
    }

    fclose(fp_1);
    return 0;
}