#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
int main(intargc, char **argv)
{
    int rank, size;
    int A[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int B[3][2] = {{7, 8}, {9, 10}, {11, 12}};
    intans[2][2] = {{0, 0}, {0, 0}};
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    if (size != 2)
    {
        printf("This example requires exactly two processes.\n");
        MPI_Abort(MPI_COMM_WORLD, 1);
    }
    if (rank == 0)
    {
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 3; j++)
                MPI_Send(&A[i][j], 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 2; j++)
                MPI_Send(&B[i][j], 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    }
    else
    {
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 3; j++)
                MPI_Recv(&A[i][j], 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 2; j++)
                MPI_Recv(&B[i][j], 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("A\n");
        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < 3; j++)
                printf("%d ", A[i][j]);
            printf("\n");
        }
        printf("\nB\n");
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 2; j++)
                printf("%d ", B[i][j]);
            printf("\n");
        }
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < 3; k++)
                    ans[i][j] = ans[i][j] + A[i][k] * B[k][j];
        printf("\nAnswer\n");
        for (int i = 0; i < 2; i++)
        {
            for (int j = 0; j < 2; j++)
                printf("%d ", ans[i][j]);
            printf("\n");
        }
    }
    MPI_Finalize();
    return 0;
}
