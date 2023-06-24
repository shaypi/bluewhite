# bluewhite
The directory stracture:
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