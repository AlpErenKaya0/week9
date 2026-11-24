from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()


if rank == 0:
    random_generated_number = random.randint(1, 10)
    comm.send(random_generated_number, dest=1, tag=0)
elif rank == 1:
    given_number = comm.recv(source=0, tag=0)
    guessed_number = int(input("Guess a number (1-10):"))
    if guessed_number == given_number:
        print("Congratz!")
    else:
        print(f"Nope! The number was {given_number}.")