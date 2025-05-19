zone_id                = "Z08292101AIKD0GPBKQE9" # ← correct zone ID
alias_zone_id          = "Z2FDTNDATAQYW2"
cloudfront_domain_name = "d3p3jpf4x470r.cloudfront.net" # Replace with your actual one if different
domain_name            = "forgescaler.com"
availability_zones     = ["us-east-1a", "us-east-1b"] # ✅
private_subnet_cidrs = [
  "10.0.1.0/24",
  "10.0.2.0/24",
  "10.0.4.0/24", # Changed from 10.0.3.0/24 to avoid collision
]
