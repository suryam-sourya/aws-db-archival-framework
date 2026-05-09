# Deployment Guide

## Overview

This guide explains how to deploy the AWS Database Archival Framework in a production-ready AWS environment.

## Prerequisites

- AWS Account
- Terraform Installed
- Python 3.11
- MongoDB Atlas Cluster
- PostgreSQL RDS Instance
- AWS CLI Configured

## Deployment Steps

### 1. Clone Repository

```bash
git clone https://github.com/suryam-sourya/aws-db-archival-framework.git
cd aws-db-archival-framework
```

### 2. Deploy Terraform Infrastructure

```bash
cd terraform/s3
terraform init
terraform apply
```

### 3. Configure Lambda Functions

- Package Lambda source
- Upload deployment package
- Configure environment variables

### 4. Configure Lifecycle Policies

Apply the lifecycle policy located in:

```bash
lifecycle-policies/glacier-policy.json
```

### 5. Enable Monitoring

- Import CloudWatch dashboard
- Configure alarms
- Enable notifications

## Validation

- Verify S3 archival uploads
- Validate Glacier transitions
- Confirm Lambda executions
- Review CloudWatch metrics
