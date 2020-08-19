# update wheel
python setup.py bdist_wheel

# update job files
aws s3 cp dist/script-0.1-py3-none-any.whl s3://$BUCKET/lib/
aws s3 cp dist/script.py s3://$BUCKET/scripts/

# create Glue job
# aws glue create-job --name script \
#     --role AWSGlueServiceRole-gluerole \
#     --command '{"Name" :  "pythonshell", "PythonVersion" : "3", "ScriptLocation" : "s3://$BUCKET/scripts/script.py"}' \
#     --default-arguments '{"--extra-py-files" : "s3://$BUCKET/lib/script-0.1-py3-none-any.whl"}'
