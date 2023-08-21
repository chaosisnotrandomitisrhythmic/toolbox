#!/bin/bash

# Get list of running instance IDs
INSTANCE_IDS=$(aws ec2 describe-instances --filters Name=instance-state-name,Values=running --query "Reservations[*].Instances[*].InstanceId" --output text)

if [ -z "$INSTANCE_IDS" ]; then
    echo "No running EC2 instances found."
    exit 0
else
    echo "Stopping EC2 instances: $INSTANCE_IDS"
    aws ec2 stop-instances --instance-ids $INSTANCE_IDS
fi
