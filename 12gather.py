from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

my_value = rank * rank

all_values = comm.gather(my_value, root=0)

if rank == 0:
    print(f"Root collected: {all_values}")