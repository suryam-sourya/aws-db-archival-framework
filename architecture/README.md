# Architecture Overview

This directory contains architecture diagrams, deployment references, workflow explanations, and AWS infrastructure design documents for the AWS Database Archival Framework.

## Core Components

- MongoDB Atlas
- PostgreSQL RDS
- AWS Lambda
- ECS Fargate
- Amazon EventBridge
- Amazon S3
- Amazon Glacier
- CloudWatch
- IAM & KMS

## High-Level Workflow

1. EventBridge schedules archival workflows
2. Lambda or ECS jobs export historical records
3. Data converted into compressed Parquet format
4. Archive objects uploaded into Amazon S3
5. Lifecycle policies move objects into Glacier storage
6. CloudWatch monitors archival health and failures

## Architecture Goals

- Reduce database storage costs
- Improve database performance
- Automate archival workflows
- Enable secure long-term retention
- Support disaster recovery operations
- Provide enterprise-grade monitoring
