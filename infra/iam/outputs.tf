output "agents_role_arn" {
  description = "ARN of the IAM role for Forgemind agents"
  value       = aws_iam_role.forgemind_agents.arn
}
