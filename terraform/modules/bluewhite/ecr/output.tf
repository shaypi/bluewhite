output "ecr_repository_name" {
  description = "The name of the repository."
  value       = aws_ecr_repository.repo.name
}
