from django.db import models
from django.contrib.auth import get_user_model

class recruitMe(models.Model):
  full_name = models.charField(max_length=100)
  date_of_birth = models.DateField()
  resume_Url = models.URLField(max_length=350)
  extra_skills = models.charField(max_length=250)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def as_dict(self):
    """Returns dictionary version of the user's information"""
    return {
      'id': self.id,
      'full_name': self.full_name,
      'resume_url': self.resume_Url,
      'skills': self.extra_skills
  }
