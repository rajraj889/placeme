from django.db import models
from django.contrib.auth.models import User
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    name    = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    #author = models.ForeignKey(User.email, on_delete= models.CASCADE,related_name='blog_posts')
    email=models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-created_on']
    #def __str__(self):
    #    return self.name
    def save(self):    
        self.slug ='Post-'+str(len(Post.objects.all())+1)
        self.status=1
        #self.author=User.objects.filter()
        #print(User,User.email)
        #x=get_user_model()
        #print(x)
        #self.author='rj8228'
        #print(self.name,self.slug)
        super(Post, self).save()
class study(models.Model):
    name    = models.CharField(max_length=200)
    college = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    p= models.SlugField(max_length=200)
    email=models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-created_on']
    def save(self):    
        self.slug ='stu-'+str(len(study.objects.all())+1)
        self.status=1
        self.p='s'
        super(study, self).save()

class company(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)#,editable=False)
    visit_date=models.DateField()
    no_recruited=models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_on']
    def save(self):    
        self.slug ='company-'+str(len(company.objects.all())+1)
        self.status=1
        super(company, self).save()
