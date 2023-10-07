# Build and push the server image to ECR
resource "aws_ecr_repository" "coverlettergen_server" {
  name = "coverlettergen_server"
}

resource "docker_image" "coverlettergen_server" {
  name = "${aws_ecr_repository.coverlettergen_server.repository_url}:latest"
  build {
    context    = "."
    dockerfile = "Dockerfile.server"
  }
}

resource "docker_registry_image" "coverlettergen_server" {
  name = docker_image.coverlettergen_server.name
}

output "ecr_repository_url_server" {
  value = aws_ecr_repository.coverlettergen_server.repository_url
}

#------------------------------------------------------------
# Build and push the worker image to ECR (with different build arguements)
resource "aws_ecr_repository" "coverlettergen_worker" {
  name = "coverlettergen_worker"
}

resource "docker_image" "coverlettergen_worker" {
  name = "${aws_ecr_repository.coverlettergen_worker.repository_url}:latest"
  build {
    context    = "."
    dockerfile = "Dockerfile.worker"
  }
}

resource "docker_registry_image" "coverlettergen_worker" {
  name = docker_image.coverlettergen_worker.name
}

output "ecr_repository_url_worker" {
  value = aws_ecr_repository.coverlettergen_worker.repository_url
}

#------------------------------------------------------------
