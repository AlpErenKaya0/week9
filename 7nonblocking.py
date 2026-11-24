from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

DATA_TAG = 0

if rank == 0:
    data = list(range(1000))
    req = comm.isend(data, dest=1, tag=DATA_TAG)    # starts sending, returns
    local = sum(x * x for x in range(1_000_000))    # useful work meanwhile
    req.wait()  # now data may be changed
    print(f"Rank 0 finished, local result {local}")
elif rank == 1:
    req = comm.irecv(source=0, tag=DATA_TAG)  # posts the receive
    print("Rank 1 does other work while the message travels")
    data = req.wait() # blocks until it arrives
    print(f"Rank 1 received {len(data)} numbers")
