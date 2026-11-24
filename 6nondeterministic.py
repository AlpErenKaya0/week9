from mpi4py import MPI
import random
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

RESULT_TAG = 0

if rank == 0:
    for _ in range(size - 1):
        status = MPI.Status()
        result = comm.recv(source=MPI.ANY_SOURCE, tag=RESULT_TAG, status=status)
        print(f"Received {result} from rank {status.Get_source()}")
else:
    time.sleep(random.uniform(0.1, 1.0)) # simulate work of random length
    comm.send(rank * rank, dest=0, tag=RESULT_TAG)
