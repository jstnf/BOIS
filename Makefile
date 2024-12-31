docker:
	@docker build -t bois .
run:
	@docker run --env-file=.env bois
