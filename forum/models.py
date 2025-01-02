from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return f"{self.id},{self.title}"
    

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(Category, self).save(*args, **kwargs)

    # def get_url(self):
    #     return reverse("posts", kwargs={
    #         "slug":self.slug
    #     })

    # @property
    # def num_posts(self):
    #     return Post.objects.filter(categories=self).count()
    
    # @property
    # def last_post(self):
    #     return Post.objects.filter(categories=self).latest("date")


class Topic(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # content = HTMLField()
    # categories = models.ManyToManyField(Category)
    # date = models.DateTimeField(auto_now_add=True)
    # approved = models.BooleanField(default=False)
    # hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    #     related_query_name='hit_count_generic_relation'
    # )
    # tags = TaggableManager()
    # comments = models.ManyToManyField(Comment, blank=True)
    # closed = models.BooleanField(default=False)
    # state = models.CharField(max_length=40, default="zero")
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id},{self.title}"

    # def get_url(self):
    #     return reverse("detail", kwargs={
    #         "slug":self.slug
    #     })

    # @property
    # def num_comments(self):
    #     return self.comments.count()

    # @property
    # def last_reply(self):
    #     return self.comments.latest("date")


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:100]

    