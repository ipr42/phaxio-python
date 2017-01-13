
swagger-codegen-cli.jar:
	wget http://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.2.1/swagger-codegen-cli-2.2.1.jar -O swagger-codegen-cli.jar

swagger-generate: swagger-codegen-cli.jar
	java -jar swagger-codegen-cli.jar generate -i ./spec/api.yaml -o ./phaxio -l python -t ./modified_templates
	# delete all the stuff it creates that we don't need
	rm -rf ./phaxio/test
	rm -rf ./phaxio/docs
	rm ./phaxio/.gitignore
	rm ./phaxio/.travis.yml
	rm ./phaxio/git_push.sh
	rm ./phaxio/LICENSE
	rm ./phaxio/README.md
	rm ./phaxio/requirements.txt
	rm ./phaxio/setup.py
	rm ./phaxio/test-requirements.txt
	rm ./phaxio/tox.ini

test:
    python setup.py test

pip-publish:
    python setup.py sdist upload
    python setup.py bdist upload


	
	

