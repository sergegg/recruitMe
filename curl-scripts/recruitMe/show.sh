#!/bin/bash

curl "http://localhost:8000/recruitMe/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
