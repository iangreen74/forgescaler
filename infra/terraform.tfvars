zone_id                = "Z08292101AIKD0GPBKQE9" # ← correct zone ID
alias_zone_id          = "Z2FDTNDATAQYW2"
cloudfront_domain_name = "d3p3jpf4x470r.cloudfront.net" # Replace with your actual one if different
domain_name            = "forgescaler.com"
availability_zones     = ["us-east-1a", "us-east-1b"] # ✅

vpc_cidr_block_v2 = "10.123.0.0/16"

public_subnet_cidrs_v2 = [
  "10.123.1.0/24",
  "10.123.2.0/24"
]

private_subnet_cidrs_v2 = [
  "10.123.101.0/24",
  "10.123.102.0/24",
  "10.123.103.0/24"
]
