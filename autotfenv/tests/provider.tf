terraform {
  required_version = "~> 0.11.5"
}

provider "aws" {
  version = "~> 1.10.0"
  region  = "${var.region}"
}

provider "cloudflare" {
  version = "~> 0.1"
  email   = "${var.cloudflare_email}"
  token   = "${var.cloudflare_token}"
}

provider "archive" {
  version = "~> 1.0"
}

provider "local" {
  version = "~> 1.0"
}

provider "null" {
  version = "~> 1.0"
}

provider "template" {
  version = "~> 1.0"
}
