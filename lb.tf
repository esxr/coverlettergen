# provision the load balancer
resource "aws_lb" "coverlettergen" {
  name               = "coverlettergen"
  internal           = false
  load_balancer_type = "application"
  subnets            = data.aws_subnets.private.ids
  security_groups    = [aws_security_group.coverlettergen_lb.id]
}

# define the internal side of the load balancer
resource "aws_lb_target_group" "coverlettergen_server" {
  name        = "coverlettergenserver"
  port        = 8080
  protocol    = "HTTP"
  vpc_id      = aws_security_group.coverlettergen.vpc_id
  target_type = "ip"
  health_check {
    path                = "/api/v1/health"
    port                = "8080"
    protocol            = "HTTP"
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 20
    interval            = 22
    matcher             = "200-399"
  }
}

# define the external side of the load balancer
resource "aws_lb_listener" "coverlettergen_server" {
  load_balancer_arn = aws_lb.coverlettergen.arn
  port              = "80"
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.coverlettergen_server.arn
  }
}

# define the security group of the balancer
resource "aws_security_group" "coverlettergen_lb" {
  name        = "coverlettergenlb"
  description = "coverlettergen Security Group"
  ingress {
    from_port   = 80
    to_port     = 80
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
