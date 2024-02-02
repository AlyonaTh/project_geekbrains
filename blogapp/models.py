from django.db import models


class Post(models.Model):
    """Post data"""
    title = models.CharField('Post Title', max_length=200)
    description = models.TextField('Post text')
    author = models.CharField('Author name', max_length=100)
    author_img = models.ImageField('Author image', upload_to='images/author')
    author_about = models.CharField('About author', max_length=500)
    date = models.DateTimeField('Publication date')
    img = models.ImageField('Image', upload_to='images/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    def get_summary(self):
        words = self.description.split()
        return f'{" ".join(words[:100])}...'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=50)
    comment_text = models.TextField('Comment', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Likes(models.Model):
    """Likes"""
    ip = models.CharField('IP-address', max_length=100)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)