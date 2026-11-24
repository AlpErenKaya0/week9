from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    numbers = [10 * i for i in range(size)]
else:
    numbers = None

my_number = comm.scatter(numbers, root=0)

print(f"Rank {rank} got: {my_number}")