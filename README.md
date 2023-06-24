# bluewhite
[![Apply/Destroy bluewhite eks](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-eks.yml/badge.svg)](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-eks.yml)
[![CI CD](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-CICD.yml/badge.svg)](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-CICD.yml)
[![Apply/Destroy bluewhite ecr](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-ecr.yml/badge.svg)](https://github.com/shaypi/bluewhite/actions/workflows/Bluewhite-ecr.yml)

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
