# bluewhite2
[![Apply/Destroy bluewhite eks](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-eks.yml/badge.svg)](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-eks.yml)
[![CI CD](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-CICD.yml/badge.svg)](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-CICD.yml)
[![Apply/Destroy bluewhite ecr](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-ecr.yml/badge.svg)](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-ecr.yml)

# Getting Started

## Deployment Process

The deployment process for the Bluewhite project involves several GitHub Actions runners:

- [Bluewhite-eks.yml](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-eks.yml): This runner creates the EKS VPC and IAM stack.
- [Bluewhite-ecr.yml](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-ecr.yml): This runner sets up the ECR stack for future use.
- [Bluewhite-CICD.yml](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-CICD.yml): This runner handles image creation, pushes it to the ECR, and updates the Kubernetes deployment with the latest image.

Once the deployment is successful, you need to update the label `env=bluewhite` on two nodes. Use the following command:

```bash
kubectl label nodes ip-10-0-17-50.eu-west-1.compute.internal ip-10-0-17-7.eu-west-1.compute.internal env=bluewhite
```

Make sure to replace ip-10-0-17-50.eu-west-1.compute.internal and ip-10-0-17-7.eu-west-1.compute.internal with the actual IP addresses of the nodes you want to label.

## Directory Structure:

```
.
|-- README.md
|-- app
|   |-- Dockerfile
|   |-- app.py
|   |-- bluewhite.yaml
|   |-- requirements.txt
|   `-- sa.yaml
`-- terraform
    |-- environments
    |   `-- test
    |       |-- bluewhite
    |       |   |-- backend.tf
    |       |   |-- bluewhite.tfvars
    |       |   |-- config
    |       |   |-- config.tf.bkp
    |       |   |-- main.tf
    |       |   |-- output.tf
    |       |   `-- variables.tf
    |       `-- ecr
    |           |-- backend.tf
    |           |-- main.tf
    |           |-- main.tfvars
    |           `-- variables.tf
    `-- modules
        `-- bluewhite
            |-- aws-vpc
            |   |-- main.tf
            |   |-- output.tf
            |   `-- variables.tf
            |-- ecr
            |   |-- ecr.tf
            |   |-- kms.tf
            |   |-- output.tf
            |   `-- variables.tf
            |-- eks
            |   |-- cluster.tf
            |   |-- data.tf
            |   |-- iam-autoscaler.tf
            |   |-- iam-autoscaling-policy.json
            |   |-- iam-oidc.tf
            |   |-- iam.tf
            |   |-- lt.tf
            |   |-- ng.tf
            |   |-- output.tf
            |   |-- sg.tf
            |   |-- userdata.tf
            |   `-- variables.tf
            `-- sg
                |-- main.tf
                |-- output.tf
                `-- variables.tf
```
