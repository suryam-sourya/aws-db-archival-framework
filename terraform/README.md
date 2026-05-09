# Terraform Infrastructure

This directory contains Infrastructure as Code configurations for deploying the AWS Database Archival Framework.

## Terraform Modules

- S3 archival bucket
- Lambda archival processor
- IAM execution roles
- CloudWatch monitoring

## Deployment Workflow

1. Initialize Terraform
2. Review execution plan
3. Apply infrastructure changes
4. Validate deployed resources

## Recommended Commands

```bash
terraform init
terraform plan
terraform apply
```
