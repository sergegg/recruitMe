#!/bin/bash

curl "http://localhost:8000/recruitMe/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
