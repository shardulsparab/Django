from django.db import models

class Candidate(models.Model):
    CandidateID = models.CharField(max_length=20)
    CandidateName = models.CharField(max_length=20)
    Contact = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)

