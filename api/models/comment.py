# from django.db import models
# from .recruitMe.py import RecruitMe
#
# class Comment(models.Model):
#   post = models.ForeignKey('RecruitMe', related_name="comments", on_delete=models.CASCADE)
#   name = models.CharField(max_length=100)
#   body = models.TextField()
#   date_added = models.DateTimeField(auto_now_add=True)
#
#   def as_dict(self):
#     """returns a dictionary of the comment"""
#     return {
#       'post': self.post,
#       'name': self.name,
#       'body': self.body
#     }
