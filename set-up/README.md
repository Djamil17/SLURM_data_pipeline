![NIH](https://github.com/Djamil17/SLURM_data_pipeline/blob/master/pics/nih-logo.png)



## Contents 
- [Setup Requisites](#Setup-Requisites)
- [Brush up on Terraform](#Terraform)
- [Enter and Configure GCP Shell](#GCP-shell)
- [Deploying VPC](#VPC)
- [Deploying Cluster](#Deploying-cluster)
- [Run MPI Job](#MPI)
- [Run Python Job](#Python)
- [Destroy Resources](#Destruction)

## Setup Requisites 

You will need the following to deploy a Slurm cluster:

* 1. **slurm-gcp git** 
* 2. **VPC** 

#### Enter and Configure GCP Shell

First, enter the shell 

While Google Cloud can be operated remotely from your laptop, we will be using Google Cloud Shell, a command line environment running in the Cloud. To access it look at the right-corner toolbar of the GCP GUI, then click the button , which is pointed out by a red box here . 

![shell button](https://lh3.googleusercontent.com/SEkKuha3_UnmalYcbfuJvV3IyW84QkhXC6moHxSiuu01Amew60AgAxekonf8MKVkWu_-7LqQ3jvrdjdUrL3oFG9IUgYuB1f5p0OYRONpwtmogd0OMto2FGIRSuzaSCFFeWjulWhT)

Wait a minute or so for the shell to initialize , the result should look something like: 

![shell_screen](https://lh4.googleusercontent.com/QkHNPQKihCmsREufnwE2sBS1sKWXi2vUsKdXA6ijCqEsLwQXK2ngbhJUEda87HGKjh9L1SXiz2FIciMqBAk35v6MVVsTsXQTCehR2-bxAxpjDBbJYxJWlwqAMOJw1uc3QFCvfFqQ)

Now you want to connect to the desired project. If you are not so already you can change it with the following:

```shell

$ gcloud config set project <PROJECT_ID>

````
The command output is :

```shell

Updated property [core/project].

```

#### Download the Slurm Deployment Configuration
In the Cloud Shell session, execute the following command to clone (download) the Git repository that contains the Slurm for Google Cloud Platform deployment-manager files:

```shell
git clone https://github.com/Djamil17/strides-slurm-gcp.git
```

After that enter into the downloaded git repository :

```shell
cd slurm-gcp
```

### Brushing up on Terraform

#### Add, Update, and Delete Resources Using Terraform
You can manage your IaaS and PaaS resources on Oracle Cloud at Customer by using the Terraform configuration that you used originally to create the resources.

#### Add Resources

Define the required resources in the configuration, and run:

```terraform apply```

#### Update Resources

Edit the attributes of the resources in the configuration, and run terraform apply.

#### Delete Resources

To delete a specific resource, run the following command:

```Copyterraform destroy -target=resource_type.resource_name```

For example, to delete just the VM in the configuration that you applied earlier, run this command:

```Copyterraform destroy -target=opc_compute_instance.default```

At the "Do you really want to destroy" prompt, enter yes.

Terraform displays the status of the operation, as shown in the following example. For each resource, Terraform shows the status and the time taken for the operation.

```Copy Destroy complete! Resources: 1 destroyed```

To delete all the resources, run terraform destroy.

To delete specific resources permanently, remove the resources from the configuration, and then run ```terraform apply```.

#### Re-create Resources

To re-create any resources that you deleted previously but didn’t remove from the configuration, run ```terraform apply```.

### Deploying VPC 

* 1. cd to tf/examples/reqs
* 2. Edit the basic.tfvars file and specify the required values
* 3. Deploy the VPC with the commands: 

```bash
$ terraform init
```

```bash
$ terraform apply -var-file=basic.tfvars
```

Once succesful you will see : 

```bash 
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

### Deploying Cluster 

* 1. cd to tf/examples/basic
* 2. Edit the basic.tfvars file and specify the required values
* 3. Optionally specify packages and program to download
* 4. Deploy the VPC with the commands: 

```bash
$ terraform apply -var-file=basic.tfvars
```

Once succesful you will see something like : 

```bash 
Apply complete! Resources: 9 added, 0 changed, 0 destroyed.
```

Verify that the vms were created. Use the lefthand tool-bar and navigate to Compute, then click VM instances. 

Under VM instances review the three virtual machine instances that have been created by the deployment manager. This includes:

* cluster-example-compute-0-image
* cluster-example-controller
* cluster-example-login0

The cluster-example-compute-0-image instance is only online for a short time to create the compute image used by the partition's auto-scaling nodes, and then it is shut down. If you'd like to make updates to the image used by compute nodes you can start this instance, make changes, and make another image in the Slurm cluster's image family to update that partition's image.

### Custom Software Installation

In scripts there is a script called ```startup.sh```, if you want to add a package add it to one of these :

```bash

PACKAGES=(
        'bind-utils'
        'environment-modules'
        'epel-release'
        'gcc'
        'git'
        'hwloc'
        'hwloc-devel'
        'libibmad'
        'libibumad'
        'lua'
        'lua-devel'
        'man2html'
        'mariadb'
        'mariadb-devel'
        'mariadb-server'
        'munge'
        'munge-devel'
        'munge-libs'
        'ncurses-devel'
        'nfs-utils'
        'numactl'
        'numactl-devel'
        'openssl-devel'
        'pam-devel'
        'perl-ExtUtils-MakeMaker'
        'python3'
        'python3-pip'
        'readline-devel'
        'rpm-build'
        'rrdtool-devel'
        'vim'
        'wget'
        'tmux'
        'pdsh'
        'openmpi'
        'yum-utils'
    )

PY_PACKAGES=(
        'pyyaml'
        'requests'
        'google-api-python-client'
    )


```

Do this before deploying the cluster. 

### Login to Slurm 

Go to the GCP shell and hit

```bash
gcloud compute ssh <cluster_name> --zone=<ZONE>
```

You will be logged in into the login virtual machine.

If this is the first time you have used cloud shell, you may see a message like the one below asking you to create an SSH key:

```bash 

WARNING: The public SSH key file for gcloud does not exist.
WARNING: The private SSH key file for gcloud does not exist.
WARNING: You do not have an SSH key for gcloud.
WARNING: SSH keygen will be executed to generate a key.
This tool needs to create the directory [/home/user/.ssh] before being
 able to generate SSH keys.

Do you want to continue (Y/n)?

```

Hit Y, then enter a passphrase. You will be prompted to enter the passphrase twice. *DO NOT LOSE THIS*. 

If the following message appears upon login:

```bash

*** Slurm is currently being installed/configured in the background. ***
A terminal broadcast will announce when installation and configuration is
complete.

/home on the controller will be mounted over the existing /home.
Any changes in /home will be hidden. Please wait until the installation is
complete before making changes in your home directory.
```
**THEN WAIT AND DO NOTHING**. **WAIT UNTIL YOU SEE THIS MESSAGE**. (approx 5-10 mins)

```bash
*** Slurm logindaemon installation complete ***

/home on the controller was mounted over the existing /home.
Either log out and log back in or cd into ~.
```

Once you see this message hit CTRL + C to end the task. Then 

```exit```

To exit the VM. 

### Entering Slurm 

Log back in through ssh: 

```bash
gcloud compute ssh cloud-example-login0 --zone=<ZONE>
```

Congrats! You are logged into your slurm login-node. 

### Tour of the Slurm CLI Tools

You're now logged in to your cluster's Slurm login node. This is the node that's dedicated to user/admin interaction, scheduling Slurm jobs, and administrative activity.

Let's run a couple commands to introduce you to the Slurm command line.

Execute the sinfo command to view the status of our cluster's resources:

```sinfo```

The output will look like: 

```bash

PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
debug*       up   infinite     10  idle~ g1-compute-0-[0-9]

```

Sample output of sinfo appears below. sinfo reports the nodes available in the cluster, the state of those nodes, and other information like the partition, availability, and any time limitation imposed on those nodes. Now hit:

```squeue```

to check if any jobs are running. As expected none. Here is the uneventful output.

```bash
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
```

### Run a Slurm Job and Scale the Cluster
Now that we have our Slurm cluster running, let's run a job and scale our cluster up.

While logged in to g1-login0, use your preferred text editor to create a new file "hostname_batch":

```bash
vi hostname_batch
```

Type "i" to enter insert mode. Now, copy and paste the following text into the file to create a simple sbatch script:

```bash
#!/bin/bash
#
#SBATCH --job-name=hostname_sleep_sample
#SBATCH --output=out_%j.txt
#
#SBATCH --nodes=2

srun hostname
sleep 60
```

Save and exit the code editor by pressing **escape** and typing ```:wq!```.

This script defines the Slurm batch execution environment and tasks. First, the execution environment is defined as bash. Next, the script defines the Slurm options first with the "#SBATCH" lines. The job name is defined as "hostname_sleep_sample". The output file is set as "output_%j.txt" where %j is substituted for the Job ID according to the Slurm Filename Patterns.

This output file is written by each compute node to a local directory, in this case the directory the sbatch script is launched from. In our example this is the user's /home folder, which is a NFS-based shared file system. This allows compute nodes to share input and output data if desired. In a production environment, the working storage should be separate from the /home storage to avoid performance impacts to the cluster operations.

Finally, the number of nodes this script should run on is defined as 2.

After the options are defined the executable commands are provided. This script will run the hostname command in a parallel manner through the srun command, and sleep for 60 seconds afterwards. You may also try modifying the script to execute a few other commands like date or whoami.

Execute the sbatch script using the sbatch command line:

```
sbatch hostname_batch
```
You will get 

```Submitted batch job 2
```

We can use the Job ID returned by the sbatch command to track and manage the job execution and resources. Execute the following command to view the Slurm job queue:

```squeue```

You will likely see the job you executed listed like below:

```
JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    2     debug hostname username  R       0:10      2 cluster-example-compute-0-[0-1]
```   
   
Since we didn't have any compute nodes provisioned, Slurm will automatically create compute instances according to the job requirements. The automatic nature of this process has two benefits. First, it eliminates the work typically required in a HPC cluster of manually provisioning nodes, configuring the software, integrating the node into the cluster, and then deploying the job. Second, it allows users to save money because idle, unused nodes are scaled down until the minimum number of nodes is running.

You can execute the sinfo command to view the Slurm cluster spinning up:

```bash
sinfo
```

This will show the nodes listed in squeue in the "mix#" state, meaning the nodes are being created:

```
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
debug*       up   infinite      8  idle~ cluster-example-compute-0-[2-9]
debug*       up   infinite      2  mix#  cluster-example-compute-0-[0-1]
```

You can also check the VM instances section in Google Cloud Console to view the newly provisioned nodes. It will take a few minutes to spin up the nodes and get Slurm installed before the job is allocated to the newly allocated nodes. Your VM instances list will soon resemble the following:

![vm_instances](https://github.com/Djamil17/strides-slurm-gcp/blob/master/set-up/Screen%20Shot%202020-06-08%20at%203.36.07%20PM.png)

Once a job is complete, it will no longer be listed in squeue, and the "alloc" nodes in sinfo will return to the "idle" state. Run "squeue" periodically until the job is completed, after a minute or two.

The output file out_%j.txt will have been written to your NFS-shared /home folder, and will contain the hostnames. Open or cat the output file (typically out_2.txt), it contents of the output file will contain:

```bash 
compute-example-compute-0-0
compute-example-compute-0-1
```
Great work, you've run a job and scaled up your Slurm cluster! If you check your VMs, you will see there are less. That is because it scaled down. 

### Run an MPI job

MPI is a standard for writing message-passing parrallel programs. Now let's run the "Hello-World" of MPI across our nodes. While logged in to ```cloud-example-login0```, use wget to download an MPI program written in the C programming language:

```bash
wget https://raw.githubusercontent.com/open-mpi/ompi/master/examples/hello_c.c
```
We'll use the "mpicc" tool to compile the MPI C code. Execute the following command on cloud-example-login0:

```bash
mpicc hello_c.c -o hello_c
```

Next, use your preferred text editor to create a new file "helloworld_batch":

```bash
vi helloworld_batch
```

Type i to enter the vi insert mode.

Copy and paste the following text into the file to create a simple sbatch script:

```bash
#!/bin/bash
#
#SBATCH --job-name=hello_world
#SBATCH --output=hello_world_%j.txt
#
#SBATCH --nodes=2

srun hello_c
```

Save and exit the code editor by pressing escape and typing ":wq!" without quotes.

Then execute the sbatch script using the ```sbatch``` command line:

```
sbatch helloworld_batch
```

Running sbatch will return a Job ID for the scheduled job, for example:

```
Submitted batch job 3
```

This will run the hostname command across 2 nodes, with one task per node, as well as printing the output to the hello_world_3.txt file.

```
Monitor squeue until the job has completed and no longer listed:
```

squeue
Once completed open or cat the latest output file (typically out_3.txt) and confirm it ran on cluster-example-compute-0-[0-1]:

```
Hello, world, I am 0 of 2, (Open MPI v3.1.7a1, package: Open MPI root@g1-controller Distribution, ident: 3.1.7a1, repo rev: v3.1.6-8-g6e2efd3, Unreleased developer copy, 141)

Hello, world, I am 1 of 2, (Open MPI v3.1.7a1, package: Open MPI root@g1-controller Distribution, ident: 3.1.7a1, repo rev: v3.1.6-8-g6e2efd3, Unreleased developer copy, 141)
```

After being idle for 5 minutes (configurable with the main.tf suspend_time field, or slurm.conf's SuspendTime field) the dynamically provisioned compute nodes will be de-allocated to release resources. You can validate this by running sinfo periodically and observing the cluster size fall back to 0:

JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
    2     debug hello_wo username  R       0:10      2 cluster-example-compute-0-[0-1]
    
Try spinning up more instances, up to your Quota allowed in the region you deployed the cluster in, and running different MPI applications.

### Running Python job 

