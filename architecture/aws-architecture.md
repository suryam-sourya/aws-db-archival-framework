# AWS Architecture

## Components

- MongoDB Atlas
- PostgreSQL RDS
- EventBridge Scheduler
- AWS Lambda
- ECS Fargate
- Amazon S3
- Amazon Glacier
- CloudWatch
- IAM & KMS

## High Level Flow

1. Scheduler triggers archival jobs
2. Data older than retention window exported
3. Data transformed into compressed Parquet format
4. Files uploaded into Amazon S3
5. Lifecycle rules move archives into Glacier
6. Monitoring and alerts handled using CloudWatch
