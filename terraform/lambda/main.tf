resource "aws_lambda_function" "archive_processor" {
  function_name = "aws-db-archive-processor"
  role          = aws_iam_role.lambda_execution_role.arn
  runtime       = "python3.11"
  handler       = "lambda_function.lambda_handler"

  filename         = "lambda.zip"
  source_code_hash = filebase64sha256("lambda.zip")

  timeout = 300

  environment {
    variables = {
      ARCHIVE_BUCKET = "aws-db-archival-framework-bucket"
    }
  }
}
