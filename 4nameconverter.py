from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

NAME_COUNT = 10
TO_RANK1_TAG = 0
TO_RANK2_TAG = 1
TO_RANK0_TAG = 2

TURKISH_MAP = str.maketrans("şŞıİğĞüÜöÖçÇ", "sSiIgGuUoOcC")

if rank == 0:
    original_names = []
    processed_names = []

    for i in range(NAME_COUNT):
        name = input(f"Enter name {i + 1}/{NAME_COUNT}: ")
        original_names.append(name)
        comm.send(name, dest=1, tag=TO_RANK1_TAG)
        processed = comm.recv(source=2, tag=TO_RANK0_TAG)
        processed_names.append(processed)

    print(f"Original names:  {original_names}")
    print(f"Processed names: {processed_names}")

elif rank == 1:
    for _ in range(NAME_COUNT):
        name = comm.recv(source=0, tag=TO_RANK1_TAG)
        no_spaces = "".join(name.split())
        comm.send(no_spaces, dest=2, tag=TO_RANK2_TAG)

elif rank == 2:
    for _ in range(NAME_COUNT):
        name = comm.recv(source=1, tag=TO_RANK2_TAG)
        converted = name.translate(TURKISH_MAP)
        comm.send(converted, dest=0, tag=TO_RANK0_TAG)