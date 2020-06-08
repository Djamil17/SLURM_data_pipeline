

Add, Update, and Delete Resources Using Terraform
You can manage your IaaS and PaaS resources on Oracle Cloud at Customer by using the Terraform configuration that you used originally to create the resources.

Add Resources

Define the required resources in the configuration, and run terraform apply.

Update Resources

Edit the attributes of the resources in the configuration, and run terraform apply.

Delete Resources

To delete a specific resource, run the following command:

```Copyterraform destroy -target=resource_type.resource_name```

For example, to delete just the VM in the configuration that you applied earlier, run this command:

```Copyterraform destroy -target=opc_compute_instance.default```

At the "Do you really want to destroy" prompt, enter yes.

Terraform displays the status of the operation, as shown in the following example. For each resource, Terraform shows the status and the time taken for the operation.

```Copy Destroy complete! Resources: 1 destroyed```

To delete all the resources, run terraform destroy.

To delete specific resources permanently, remove the resources from the configuration, and then run terraform apply.

Re-create Resources

To re-create any resources that you deleted previously but didn’t remove from the configuration, run terraform apply.
