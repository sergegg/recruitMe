#!/bin/bash

curl "http://localhost:8000/recruitMe/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "recruitMe": {
      "name": "'"${NEWNAME}"'",
      "date_of_birth": "'"${NEWDOB}"'",
      "resume_Url": "'"${NEWRESUME}"'"
    }
  }'

echo
