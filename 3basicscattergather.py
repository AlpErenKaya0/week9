from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

NAMES_TAG = 0
PREFIXES = {1: "AA", 2: "BB"}

if rank == 0:
    names = ["abdul-hakeem", "ada", "ali", "azizul", "faaiz", "firas"]
    for dest in PREFIXES:
    #size ne işe yaramış oldu ? güvenlik kontrolü çünkü 
    # belki ben 200 processorle başlattım kodlarken 2 procc düşünmeme rağmen? 
    # olamaz mı? olabilir.
        if dest < size:
            comm.send(names, dest=dest, tag=NAMES_TAG)
    print(f"Rank 0 sent: {names}")

elif rank in PREFIXES:
    received = comm.recv(source=0, tag=NAMES_TAG)
    modified = [PREFIXES[rank] + name for name in received]
    print(f"Rank {rank} received: {received}")
    print(f"Rank {rank} modified: {modified}")
    