from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

NUMBER_TAG = 0
ATTEMPTS_TAG = 1

if rank == 0:
    random_generated_number = random.randint(1, 10)
    attempts = int(input("How many times he/she can guess the number? "))
    comm.send(random_generated_number, dest=1, tag=NUMBER_TAG)
    comm.send(attempts, dest=1, tag=ATTEMPTS_TAG)
elif rank == 1:
    given_number = comm.recv(source=0, tag=NUMBER_TAG)
    attempts = comm.recv(source=0, tag=ATTEMPTS_TAG)

    for remaining in range(attempts, 0, -1):
        guessed_number = int(input("Guess a number (1-10): "))
        if guessed_number == given_number:
            print("Congratz!")
            break
        if remaining - 1 > 0:
            print(f"Wrong! {remaining - 1} remained.")
    else:
        print(f"You cant guess anymore! The number was {given_number}.")