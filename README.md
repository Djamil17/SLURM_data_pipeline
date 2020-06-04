# SLURM_data_pipeline

Set up of Slurm Cluster using [Google Cloud Platform](https://cloud.google.com/blog/products/compute/hpc-made-easy-announcing-new-features-for-slurm-on-gcp). Stand-up by itself or integrate VM cluster with Biowulf.

![NIH](https://github.com/Djamil17/SLURM_data_pipeline/blob/master/pics/nih-logo.png)

![Slurm Image](https://github.com/Djamil17/SLURM_data_pipeline/blob/master/pics/slurm.max-400x400.png)


## Contents 
- [Motivation](#Motivation)
- [Slurm](#Slurm)
- [Slurm on Google Cloud Platform](#Slurm-on-Google-Cloud-Platform)
  * [History](#Definition)
- [Deployement Models](#Deployement-Models)
  * [Definition](#Definition)
  * [1:N](#Definition)
  * [Hybrid](#Definition)
- [Using the Documentation](#Using-Documentation)

### Motivation and History 

Scientific computation requires High-Performance Computing. This has often meant massive investment in *on-premise supercomputers".*** The NIH HPC group plans, manages and supports high-performance computing systems specifically for the intramural NIH community. The NIH has a supercomputing system which uses Slurm for cluster management, scheduling, and resource allocation. Slurm is a default in the HPC community. 

In recent years, for a number of reasons, the HPC community is becoming more interested in leveraging cloud services. This has often meant, not so much the elimination of costly hardware, software, development, and maintenance, but a supplementation of the on-premise super computer with cloud services (virtual machines and clusters). 

Therefore integrating slurm engine VM clusters with on-premise supercomputers is a major advance for scientific computation.  

### Slurm

Slurm is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters. Slurm requires no kernel modifications for its operation and is relatively self-contained. As a cluster workload manager, Slurm has three key functions. First, it allocates exclusive and/or non-exclusive access to resources (compute nodes) to users for some duration of time so they can perform work. Second, it provides a framework for starting, executing, and monitoring work (normally a parallel job) on the set of allocated nodes. Finally, it arbitrates contention for resources by managing a queue of pending work. Optional plugins can be used for accounting, advanced reservation, gang scheduling (time sharing for parallel jobs), backfill scheduling, topology optimized resource selection, resource limits by user or bank account, and sophisticated multifactor job prioritization algorithms. For more on [Slurm](https://slurm.schedmd.com/overview.html). 

### Slurm GCP

Scripts and documentation developed from the following [Slurm-Git](https://github.com/SchedMD/slurm-gcp). 

Also, [slurm codeland](https://codelabs.developers.google.com/codelabs/hpc-slurm-on-gcp/#0). 

### Deployment Models

### Install using Terraform (Beta)

To deploy, you must have a GCP account and either have the
[GCP Cloud SDK](https://cloud.google.com/sdk/downloads) and
[Terraform](https://www.terraform.io/downloads.html)
installed on your computer or use the GCP
[Cloud Shell](https://cloud.google.com/shell/).

Steps:
1. cd to tf/examples/basic
2. Edit the `basic.tfvars` file and specify the required values
3. Deploy the cluster
   ```
   $ terraform init
   $ terraform apply -var-file=basic.tfvars
   ```
4. Tearing down the cluster

   ```
   $ terraform destroy -var-file=basic.tfvars
   ```

   **NOTE:** If additional resources (instances, networks) are created other
   than the ones created from the default deployment then they will need to be
   destroyed before deployment can be removed.
   
You may want to review ```tf.vars``` files [here](https://learn.hashicorp.com/terraform/gcp/variables).

#### What and How to Edit basic.vars 

### Image-based Scaling
   The deployment will create a <cluster_name>-compute-\#-image instance, where
   \# is the index in the array of partitions, for each partition that is a base
   compute instance image. After installing necessary packages, the instance
   will be stopped and an image of the instance will be created. Subsequent
   bursted compute instances will use this image -- shortening the creation and
   boot time of new compute instances. While the compute image is running, the
   respective partitions will be marked as "down" to prevent jobs from
   launching until the image is created. After the image is created, the
   partition will be put into an "up" state and jobs can then run.

   **NOTE:** When creating a compute image that has gpus attached, the process
   can take about 10 minutes.

   If the compute image needs to be updated, it can be done with the following
   command:
   ```
   $ gcloud compute images create <cluster_name>-compute-#-image-$(date '+%Y-%m-%d-%H-%M-%S') \
                                  --source-disk <instance name> \
                                  --source-disk-zone <zone> --force \
                                  --family <cluster_name>-compute-#-image-family
   ```

   Existing images can be viewed on the console's [Images](https://console.cloud.google.com/compute/images)
   page.

### Installing Custom Packages
   There are two files, *custom-controller-install* and *custom-compute-install*, in
   the scripts directory that can be used to add custom installations for the
   given instance type. The files will be executed during startup of the
   instance types.
   
#### How to 

### Accessing Compute Nodes Directly

   There are multiple ways to connect to the compute nodes:
   1. If the compute nodes have external IPs you can connect directly to the
      compute nodes. From the [VM Instances](https://console.cloud.google.com/compute/instances)
      page, the SSH drop down next to the compute instances gives several
      options for connecting to the compute nodes.
   2. With IAP configured, you can SSH to the nodes regardless of external IPs or not.
      See https://cloud.google.com/iap/docs/enabling-compute-howto.
   3. Use Slurm to get an allocation on the nodes.
      ```
      $ srun --pty $SHELL
      [g1-login0 ~]$ srun --pty $SHELL
      [g1-compute-0-0 ~]$
      ```
