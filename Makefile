
swagger-generate:
	java -jar swagger-codegen-cli.jar generate -i ./spec/api.yaml -o ./phaxio -l python -t ./modified_templates
