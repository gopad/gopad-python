#!/usr/bin/env bash
set -eo pipefail

if [ -L "${0}" ]
then
    ROOT=$(realpath -e "$(dirname "$(readlink -e "${0}")")/..")
else
    ROOT=$(realpath -e "$(dirname "${0}")/..")
fi

SPEC_VERSION="1.0.0-alpha1"
SPEC_DOWNLOAD=${SPEC:-https://dl.gopad.eu/openapi/${SPEC_VERSION}.yaml}

curl -sSLo "${ROOT}/hack/wrapped-client.sh" \
    https://raw.githubusercontent.com/OpenAPITools/openapi-generator/master/bin/utils/openapi-generator-cli.sh && \
    chmod +x "${ROOT}/hack/wrapped-client.sh"

pushd "${ROOT}" >/dev/null
    echo "> deleting library folder"
    rm -rf gopad openapitools.json

    OPENAPI_GENERATOR_VERSION=7.13.0 "${ROOT}/hack/wrapped-client.sh" \
        generate \
        -c openapi.yml \
        -g python \
        --git-repo-id gopad-python \
        --git-user-id gopad \
        --http-user-agent "gopad-python/${SPEC_VERSION}" \
        -i "${SPEC_DOWNLOAD}" \
        -o . \
        -t hack/openapi/templates \
        --strict-spec true
popd >/dev/null
