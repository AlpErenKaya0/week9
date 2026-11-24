from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

my_value = rank + 1

total = comm.reduce(my_value, op=MPI.SUM, root=0)
biggest = comm.reduce(my_value, op=MPI.MAX, root=0)

if rank == 0:
    print(f"Sum: {total}, Max: {biggest}")