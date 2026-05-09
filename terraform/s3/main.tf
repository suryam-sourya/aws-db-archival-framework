resource "aws_s3_bucket" "archive_bucket" {
  bucket = "aws-db-archival-framework-bucket"

  tags = {
    Name        = "AWS Database Archival Bucket"
    Environment = "Production"
    Project     = "AWS Database Archival Framework"
  }
}

resource "aws_s3_bucket_versioning" "archive_versioning" {
  bucket = aws_s3_bucket.archive_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}
