from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core
from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_iam as iam
)
from os import path

class LambdaDataEngStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = _lambda.Function(
            scope=self,
            id="lambdaLeoCdk",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset(path.join("lambda_data_eng/code")),
            timeout=cdk.Duration.seconds(amount=30),
            handler="lambda_handler.handler"
        )

        bucket = s3.Bucket(
            scope=self,
            id="bucket-mercado-bitcoin",
            bucket_name="leo-data-lake-raw-data",
        )

        fn.add_to_role_policy(statement=iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=[
                "s3:PutObject",
                "s3:ListBucket",
                "s3:PutObjectAcl",
            ],
            resources=[
                bucket.bucket_arn,
                f"{bucket.bucket_arn}/*"
            ]
        ))
