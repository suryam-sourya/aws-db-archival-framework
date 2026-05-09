# Cost Analysis

## Estimated Monthly Savings

| Service | Before Optimization | After Optimization |
|---|---|---|
| MongoDB Atlas | High operational storage cost | Reduced hot storage usage |
| PostgreSQL RDS | Growing database storage | Optimized active dataset |
| Amazon S3 Glacier | Not utilized | Ultra-low archival storage |

## Optimization Strategy

- Retain only recent operational data
- Archive historical records weekly
- Use Glacier lifecycle transitions
- Compress archival datasets
- Use Parquet format for efficient storage

## Expected Benefits

- Reduced database storage costs
- Faster operational queries
- Lower infrastructure maintenance overhead
- Long-term compliance retention
- Improved disaster recovery readiness

## Recommended Storage Lifecycle

| Storage Tier | Retention Purpose |
|---|---|
| S3 Standard | Recent archives |
| Glacier Instant Retrieval | Frequently restored archives |
| Glacier Deep Archive | Long-term retention |
