from mpi4py import MPI

comm = MPI.COMM_WORLD
rank, p = comm.Get_rank(), comm.Get_size()

# Rank i prepares one personal message for every rank j
send = [f"m{rank},{j}" for j in range(p)]

recv = comm.alltoall(send) # recv[j] is the message rank j sent to me

print(f"Rank {rank} sent {send}")
print(f"Rank {rank} got {recv}")

# The same with point-to-point calls (pairwise exchange, p - 1 steps):
mine = [None] * p
mine[rank] = send[rank]
for step in range(1, p):
    dest, src = (rank + step) % p, (rank - step) % p
    mine[src] = comm.sendrecv(send[dest], dest=dest, source=src)
assert mine == recv
