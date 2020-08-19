# Introduction

This is a repository that describes a simple data lake structure for Amazon Web Services.

# How it works

This follows the serverless data lake architecture for Amazon Web Services: `dist/script.py` loads data into S3. AWS Glue then crawls and generates databases and tables. Data is now available to be queried by AWS Athena and/or visualized by your tool of choice.

# How to run it

...

# References

[AWS Blog (pt-br)](https://aws.amazon.com/pt/blogs/aws-brasil/usando-python-shell-e-pandas-no-aws-glue-para-processar-datasets-pequenos-e-medios/)