#!/usr/bin/env bash
set -eo pipefail

if [ -L $0 ]
then
    ROOT=$(realpath -e $(dirname $(readlink -e $0))/..)
else
    ROOT=$(realpath -e $(dirname $0)/..)
fi

SPEC=${SPEC:-https://dl.gopad.eu/openapi/1.0.0-alpha1.yml}

docker run --rm \
	-v ${ROOT}:/generate \
	openapitools/openapi-generator-cli:v5.4.0 \
	generate \
	-c /generate/openapi.yml \
	-g python \
	--git-repo-id gopad-python \
	--git-user-id gopad \
	--http-user-agent gopad-python/1.0.0-alpha1 \
	-i ${SPEC} \
	-o /generate \
	-t /generate/hack/openapi/templates \
	--strict-spec true
