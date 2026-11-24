from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

my_value = rank + 1

total = comm.allreduce(my_value, op=MPI.SUM)

print(f"Rank {rank} knows the total: {total}")