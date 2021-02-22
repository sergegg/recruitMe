from django.db import models
from django.contrib.auth import get_user_model

class RecruitMe(models.Model):
  name = models.CharField(max_length=100)
  date_of_birth = models.DateField()
  resume_Url = models.URLField(max_length=350)
# extra_skills = models.CharField(max_length=250)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def as_dict(self):
    """Returns dictionary version of the user's information"""
    return {
      'id': self.id,
      'full_name': self.full_name,
      'resume_url': self.resume_Url
  }

class Comment(models.Model):
  post = models.ForeignKey(RecruitMe, related_name="comments", on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  body = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  def as_dict(self):
    """returns a dictionary of the comment"""
    return {
      'post': self.post,
      'name': self.name,
      'body': self.body
    }
