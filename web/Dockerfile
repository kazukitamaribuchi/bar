FROM node:17.0.0-alpine

WORKDIR /usr/src/bar/web/
RUN apk update
RUN apk upgrade
RUN apk add \
	net-tools \
	sudo \
	bzip2 \
	curl \
	gcc \
	git \
	vim

RUN yarn global add @vue/cli@5.0.4
