resource "aws_ecs_cluster" "coverlettergen" {
  name = "coverlettergen"
}

# feed the credentials to the docker provider

# container definition
resource "aws_ecs_task_definition" "coverlettergen" {
  family                   = "coverlettergen"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = 1024
  memory                   = 2048
  execution_role_arn       = data.aws_iam_role.lab.arn

  container_definitions = <<DEFINITION
[
  {
    "image": "${local.server_image}",
    "cpu": 512,
    "memory": 1024,
    "name": "coverlettergen_server",
    "networkMode": "awsvpc",
    "portMappings": [
      {
        "containerPort": 8080,
        "hostPort": 8080
      }
    ],
    "environment": [
      {
        "name": "OPENAI_API_KEY",
        "value": "${local.envs.OPENAI_API_KEY}"
      },
      {
        "name": "CELERY_BROKER_URL",
        "value": "redis://${local.redis_address}:${local.redis_port}"
      },
      {
        "name": "CELERY_RESULT_BACKEND",
        "value": "redis://${local.redis_address}:${local.redis_port}"
      }
    ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/coverlettergen/server",
        "awslogs-region": "us-east-1",
        "awslogs-stream-prefix": "ecs",
        "awslogs-create-group": "true"
      }
    }
  },
  {
    "image": "${local.worker_image}",
    "cpu": 512,
    "memory": 1024,
    "name": "coverlettergen_worker",
    "networkMode": "awsvpc",
    "environment": [
      {
        "name": "OPENAI_API_KEY",
        "value": "${local.envs.OPENAI_API_KEY}"
      },
      {
        "name": "CELERY_BROKER_URL",
        "value": "redis://${local.redis_address}:${local.redis_port}"
      },
      {
        "name": "CELERY_RESULT_BACKEND",
        "value": "redis://${local.redis_address}:${local.redis_port}"
      }
    ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/coverlettergen/worker",
        "awslogs-region": "us-east-1",
        "awslogs-stream-prefix": "ecs",
        "awslogs-create-group": "true"
      }
    }
  }
]
DEFINITION
}

# scaling
resource "aws_ecs_service" "coverlettergen" {
  name            = "coverlettergen"
  cluster         = aws_ecs_cluster.coverlettergen.id
  task_definition = aws_ecs_task_definition.coverlettergen.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = data.aws_subnets.private.ids
    security_groups  = [aws_security_group.coverlettergen.id]
    assign_public_ip = true
  }

  # Connect the internal side of the load balancer
  # to the auto-scaling service
  load_balancer {
    target_group_arn = aws_lb_target_group.coverlettergen_server.arn
    container_name   = "coverlettergen_server"
    container_port   = 8080
  }

}

resource "aws_security_group" "coverlettergen" {
  name        = "coverlettergen"
  description = "coverlettergen Security Group"

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
