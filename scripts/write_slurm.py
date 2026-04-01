#!/usr/bin/env python3
# write_slurm.py
# This script prints a slurm script template

import argparse

###------------- accept and parse command line arguments
# create an argument parser object
parser = argparse.ArgumentParser(description="This script prints a slurm script template")

# add a positional argument, in this case, the name of the job 
parser.add_argument("job_name", help="Name of job")

# add a add a positional argument, in this case, the number of hours 
parser.add_argument("number_of_hours", help="Number of hours")

# add a add a positional argument, in this case, the number of the queue
parser.add_argument("queue_name", help="Name of the queue")

# add a add a positional argument, in this case, users' email
parser.add_argument("email", help="Your email")

# parse the arguments
args = parser.parse_args()

print("#!/bin/bash")
print("#SBATCH --job-name=" + args.job_name)
print("#SBATCH --time=" + args.number_of_hours)
print("#SBATCH -p " + args.queue_name)
print("#SBATCH -q cloud")
print("#SBATCH -N 1")
print("#SBATCH -n 1")
print("#SBATCH -c 1")
print("#SBATCH --output=%x.%j.out")
print("#SBATCH --error=%x.%j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=" + args.email)
print("")
print("module purge")
print("module load blast")
print("")
print("cd $SLURM_SUBMIT_DIR")
print("blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn")