# IAM Role for Forgemind Agents with Trust Policy

data "aws_iam_policy_document" "assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["eks.amazonaws.com", "ec2.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "forgemind_agents" {
  name               = var.role_name
  assume_role_policy = data.aws_iam_policy_document.assume_role.json

  tags = {
    Environment = "forgemind"
  }
}

resource "aws_iam_policy" "basic_s3_logs" {
  name        = "forgemind-basic-s3-logs"
  description = "Allow read/write access to memory logs bucket"
  policy      = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = ["s3:GetObject", "s3:PutObject"],
        Resource = ["arn:aws:s3:::forgemind-memory-logs/*"]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "attach_basic_policy" {
  role       = aws_iam_role.forgemind_agents.name
  policy_arn = aws_iam_policy.basic_s3_logs.arn
}
