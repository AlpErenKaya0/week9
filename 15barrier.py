from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

time.sleep(rank)
print(f"Rank {rank} arrived")

comm.Barrier()

print(f"Rank {rank} continues")