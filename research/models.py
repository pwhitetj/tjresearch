from django.db import models

# Create your models here.


#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')


#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.id, filename)

class Project(models.Model):
    title = models.CharField(max_length=1024)
    abstract = models.TextField(max_length=32767)
    paper = models.FileField(upload_to=user_directory_path)
    director = models.ForeignKey('LabDirector')
    def __str__(self):
        return self.title

class Student(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.EmailField()
    student_id = models.CharField(max_length=10)
    cookie = models.TextField(max_length=1000)
    project = models.ForeignKey(Project)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

class ResearchLab(models.Model):
    lab_name = models.CharField(max_length=50)
    lab_description = models.TextField(max_length=1000)

    def __str__(self):
        return self.lab_name

class LabDirector(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.EmailField()
    lab = models.ForeignKey(ResearchLab)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)
