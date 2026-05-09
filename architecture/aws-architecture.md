# AWS Architecture

## Core Services

- MongoDB Atlas
- PostgreSQL RDS
- AWS Lambda
- ECS Fargate
- Amazon EventBridge
- Amazon S3
- Amazon Glacier
- Amazon CloudWatch
- AWS IAM
- AWS KMS

## Architecture Objectives

- Reduce operational database storage costs
- Improve database query performance
- Enable automated archival workflows
- Provide secure long-term retention
- Support disaster recovery operations
- Maintain observability and monitoring

## High-Level Workflow

1. EventBridge triggers scheduled archival jobs
2. Lambda or ECS tasks export historical records
3. Exported datasets converted into compressed Parquet format
4. Archive objects uploaded into Amazon S3
5. Lifecycle policies transition objects into Glacier
6. CloudWatch monitors execution metrics and failures
7. Archived data can be restored when required

## Security Controls

- IAM least privilege access
- SSE-KMS encryption
- Private networking
- CloudTrail audit logging
- Secure lifecycle management
