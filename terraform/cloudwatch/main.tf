resource "aws_cloudwatch_log_group" "archive_logs" {
  name              = "/aws/archive/framework"
  retention_in_days = 30
}

resource "aws_cloudwatch_metric_alarm" "lambda_errors" {
  alarm_name          = "archive-lambda-errors"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "Errors"
  namespace           = "AWS/Lambda"
  period              = 300
  statistic           = "Sum"
  threshold           = 1
  alarm_description   = "Alarm for Lambda archival failures"
}
