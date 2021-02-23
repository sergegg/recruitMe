curl "http://localhost:8000/recruitMe/${ID}" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "recruitMe": {
      "full_name": "'"${NAME}"'",
      "date_of_birth": "'"${DOB}"'",
      "resume_Url": "'"${RESUME}"'",
      "extra_skills": "'"${SKILLS}"'"
    }
  }'

echo
