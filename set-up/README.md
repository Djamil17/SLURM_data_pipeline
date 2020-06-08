![NIH](https://github.com/Djamil17/SLURM_data_pipeline/blob/master/pics/nih-logo.png)

## Contents 
- [Setup Requisites](#Setup-Requisites)
- [Deploying Project](#Project)
- [Deploying VPC](#VPC)
- [Set up of Deployement Models](#Deployement-Models)
  * [1:N](#Definition)
  * [Hybrid](#Definition)


## Setup Requisites 

You will need the following to deploy a Slurm cluster:

* 1. **slurm-gcp git** 
* 2. **Project**
* 3. **VPC** 



## Steps 

#### Enter and Configure GCP Shell 

First, enter the shell 

While Google Cloud can be operated remotely from your laptop, we will be using Google Cloud Shell, a command line environment running in the Cloud. To access it look at the right-corner toolbar of the GCP GUI, then click the button , which is pointed out by a red box here . 

![shell button](https://lh3.googleusercontent.com/SEkKuha3_UnmalYcbfuJvV3IyW84QkhXC6moHxSiuu01Amew60AgAxekonf8MKVkWu_-7LqQ3jvrdjdUrL3oFG9IUgYuB1f5p0OYRONpwtmogd0OMto2FGIRSuzaSCFFeWjulWhT)

Wait a minute or so for the shell to initialize , the result should look something like: 

![shell_screen](https://lh4.googleusercontent.com/QkHNPQKihCmsREufnwE2sBS1sKWXi2vUsKdXA6ijCqEsLwQXK2ngbhJUEda87HGKjh9L1SXiz2FIciMqBAk35v6MVVsTsXQTCehR2-bxAxpjDBbJYxJWlwqAMOJw1uc3QFCvfFqQ)

Now you want to connect to the desired project. If you are not so already you can change it with the following:

```Bash

$ gcloud config set project <PROJECT_ID>

````
The command output is :

```Bash

Updated property [core/project].

```

#### Download the Slurm Deployment Configuration
In the Cloud Shell session, execute the following command to clone (download) the Git repository that contains the Slurm for Google Cloud Platform deployment-manager files:

```Bash
git clone https://github.com/Djamil17/slurm-gcp.git
```

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






#### deploying VPC 
