# Cloud Provider Limitations

## Spot Instance Interruptions

By nature, EC2 SPOT instances are cheaper because they can be taken back by AWS anytime. [Refer to the official AWS Documentation for more information.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)&#x20;

Due to the unpredictable nature of interruptions, e6data Clusters may not function correctly. Therefore, Spot instances are recommended only for non-critical workloads.

The following can occur depending on which e6data component was interrupted:

* Query execution failures
* Autoscaling failures
* Catalog creation & modification failures
