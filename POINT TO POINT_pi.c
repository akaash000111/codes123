from mpi4py import MPI
import random
comm=MPI.COMM_WORLD
rank=comm.Get_rank()
size=comm.Get_size()
n=-1
#number of points to use for Monte Carlo simulation
if(rank==0):
    n=int(input("Enter the number of points to use for Monte Carlo simulation"))
    for i in range(1,size):
        comm.send(n, dest=i)
#calculate the start and end indices for this process
if(rank!=0):
    n=comm.recv(source=0)
start_index = rank*(n // size)
end_index = (rank + 1)*(n // size)
#initialize the count of points inside the circle 
inside_count = 0
#generate random points and count the number inside the circle 
for i in range (start_index, end_index):
    x = random.uniform(-1.0, 1.0)
    y = random.uniform (-1.0, 1.0)
    if x*x + y*y <= 1.0:
        inside_count += 1
if(rank==0):
    total_inside_count=inside_count
#print(total_inside_count)
    comm.send(inside_count,dest=rank+1)
if rank !=0:
    total_inside_count = inside_count 
    partial_inside_count = comm.recv(source=rank-1)
    total_inside_count += partial_inside_count
#print(total_inside_count)
    comm.send(total_inside_count, dest=(rank+1)%size)

if rank == 0:
    total_inside_count=comm.recv(source=size-1)
    pi = 4.0 * total_inside_count / n 
    print("Finally in the root process PI VALUE CALCULATION")
    print("pi =", pi)
#calculate pi and print the result
