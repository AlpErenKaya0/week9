from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

TAG = 0
other = 1 - rank   # run with exactly 2 processes

# Version A: deadlock, both ranks wait first
# message = comm.recv(source=other, tag=TAG)
# comm.send(f"hello from {rank}", dest=other, tag=TAG)

# Version B: unsafe, works only while messages are buffered
# comm.send("x" * 10_000_000, dest=other, tag=TAG)
# message = comm.recv(source=other, tag=TAG)

# Version C: safe, the order of the calls depends on the rank
if rank == 0:
    comm.send(f"hello from {rank}", dest=other, tag=TAG)
    message = comm.recv(source=other, tag=TAG)
else:
    message = comm.recv(source=other, tag=TAG)
    comm.send(f"hello from {rank}", dest=other, tag=TAG)

print(f"Rank {rank} received a message of length {len(message)}")
