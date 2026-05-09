# Architecture Overview

This directory contains architecture diagrams and deployment references for the AWS Database Archival Framework.

## Components

- MongoDB Atlas
- PostgreSQL RDS
- AWS Lambda
- ECS Fargate
- EventBridge
- Amazon S3
- Amazon Glacier
- CloudWatch
- IAM & KMS

## Workflow

1. Weekly EventBridge schedule triggers archival job
2. Export records older than 7 days
3. Convert data into Parquet format
4. Compress and upload to S3
5. Lifecycle policy moves data into Glacier
6. Monitoring and validation handled via CloudWatch
