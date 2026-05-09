# AWS Database Archival Framework

Enterprise-grade AWS archival framework for MongoDB Atlas and PostgreSQL using Amazon S3, Glacier, Lambda, ECS, and EventBridge for scalable cost optimization.

---

## Overview

This project demonstrates a production-ready cloud archival strategy that helps organizations:

- Reduce database infrastructure costs
- Archive historical records automatically
- Improve scalability and database performance
- Implement secure long-term storage
- Maintain retrieval and recovery workflows

The framework focuses on retaining only recent operational data in databases while moving older records to low-cost archival storage tiers.

---

## Architecture

```mermaid
graph LR
 subgraph "Active Database"
 M[MongoDB Atlas<br/>(last 7 days)]
 P[RDS PostgreSQL<br/>(last 7 days)]
 end
 
 subgraph "Archive Pipeline"
 S[EventBridge<br/>(Weekly Schedule)]
 J[ECS/Lambda Job<br/>(Export & Transform)]
 B[S3 Bucket<br/>(Archive)]
 G[Glacier Storage<br/>(Lifecycle Target)]
 end
 
 M -->|Delete >7d| J
 P -->|Delete >7d| J
 S --> J
 J --> B
 B --> G
```

---

## Tech Stack

- AWS Lambda
- Amazon ECS Fargate
- Amazon EventBridge
- Amazon S3
- Amazon Glacier
- MongoDB Atlas
- PostgreSQL RDS
- Python
- Pandas
- PyArrow
- CloudWatch
- IAM
- KMS

---

## Workflow

1. EventBridge triggers archival jobs weekly
2. Export records older than 7 days
3. Convert records to Parquet format
4. Compress archive files
5. Upload to Amazon S3
6. Transition to Glacier using lifecycle policies
7. Validate archive integrity
8. Delete archived records from source databases

---

## Key Features

- Automated archival pipeline
- Cost optimization strategy
- S3 lifecycle automation
- Glacier archival tiers
- Secure IAM-based access
- Encryption using SSE-KMS
- Monitoring with CloudWatch
- Rollback and recovery workflows
- Enterprise-grade architecture

---

## Example Export Commands

### MongoDB Export

```bash
mongoexport --uri="$ATLAS_URI" --collection=mycoll \
 --query='{ "createdAt": { "$lt": { "$date": {"$numberLong": "<timestamp7days>"} } } }' \
 --out=archive.json
```

### PostgreSQL Export

```bash
PGPASSWORD=$PASS psql -h $RDS_HOST -U $USER -d $DB \
 -c "\\copy (SELECT * FROM events WHERE created_at < now() - interval '7 days') TO 'events.csv' CSV"
```

---

## Cost Optimization Benefits

| Component | Before | After | Savings |
|---|---|---|---|
| MongoDB Atlas | ~$1,195/mo | ~$182/mo | ~85% |
| RDS PostgreSQL | ~$42/mo | ~$27/mo | ~36% |
| Glacier Storage | High DB Storage | Ultra-low archival storage | Significant |

---

## Security Best Practices

- Least privilege IAM roles
- Private subnet database access
- S3 bucket policy restrictions
- CloudTrail auditing
- KMS encryption
- Atlas PrivateLink / VPC Peering

---

## Future Improvements

- Athena querying on archived data
- QuickSight dashboards
- Terraform infrastructure automation
- Real-time streaming archival
- AI-driven cost optimization

---

## Repository Structure

```bash
.
├── architecture/
├── scripts/
├── lifecycle-policies/
├── monitoring/
├── diagrams/
├── docs/
└── README.md
```

---

## Author

Suryam Sourya  
Cloud & DevOps Engineer

---

## Why This Project Matters

This project demonstrates:

- Cloud architecture design
- AWS cost optimization
- DevOps automation
- Data lifecycle management
- Security implementation
- Scalable archival pipelines
- Enterprise-grade infrastructure workflows
