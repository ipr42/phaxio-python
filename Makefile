
swagger-codegen-cli.jar:
	wget http://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.1/swagger-codegen-cli-2.2.1.jar -O swagger-codegen-cli.jar

swagger-generate: swagger-codegen-cli.jar
	java -jar swagger-codegen-cli.jar generate -i ./spec/api.yaml -o ./phaxio -l python -t ./modified_templates
