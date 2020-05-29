# SLURM_data_pipeline

Set up of Slurm Cluster using [Google Cloud Platform](https://cloud.google.com/blog/products/compute/hpc-made-easy-announcing-new-features-for-slurm-on-gcp). Stand-up by itself or integrate VM cluster with Biowulf.

![NIH](https://github.com/Djamil17/SLURM_data_pipeline/blob/master/pics/nih-logo.png)

![Slurm Image](https://github.com/Djamil17/SLURM_data_pipeline/blob/master/pics/slurm.max-400x400.png)


# Contents 
- [Motivation](#Motivation)
- [Slurm](#Slurm)
- [Slurm on Google Cloud Platform](#Slurm-on-Google-Cloud-Platform)
  * [History](#Definition)
- [Deployement Models](#Deployement-Models)
  * [Definition](#Definition)
  * [1:N](#Definition)
  * [Hybrid](#Definition)
- [Using the Documentation](#Using-Documentation)

## Motivation and History 

Scientific computation requires High-Performance Computing. This has often meant massive investment in *on-premise supercomputers".*** The NIH HPC group plans, manages and supports high-performance computing systems specifically for the intramural NIH community. The NIH has a supercomputing system which uses Slurm for cluster management, scheduling, and resource allocation. Slurm is a default in the HPC community. 

In recent years, for a number of reasons, the HPC community is becoming more interested in leveraging cloud services. This has often meant, not so much the elimination of costly hardware, software, development, and maintenance, but a supplementation of the on-premise super computer with cloud services (virtual machines and clusters). 

Therefore integrating slurm engine VM clusters with on-premise supercomputers is a major advance for scientific computation.  

## Slurm

Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters. Slurm requires no kernel modifications for its operation and is relatively self-contained. As a cluster workload manager, Slurm has three key functions. First, it allocates exclusive and/or non-exclusive access to resources (compute nodes) to users for some duration of time so they can perform work. Second, it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes. Finally, it arbitrates contention for resources by managing a queue of pending work. Optional plugins can be used for accounting, advanced reservation, gang scheduling (time sharing for parallel jobs), backfill scheduling, topology optimized resource selection, resource limits by user or bank account, and sophisticated multifactor job prioritization algorithms. For more on [Slurm](https://slurm.schedmd.com/overview.html). 

## Slurm GCP

Scripts and documentation developed from the following [Slurm-Git](https://github.com/SchedMD/slurm-gcp). 

Also, [slurm codeland](https://codelabs.developers.google.com/codelabs/hpc-slurm-on-gcp/#0). 

## History 

## Deployment Models

## How to Use the Documentation 
