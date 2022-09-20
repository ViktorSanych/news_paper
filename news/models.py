from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.user.username     # было написано username

    def update_rating(self):
        posts_rating = sum([post.vote * 3 for post in self.post_set.all()])  # рЕЙТИНГИ ПОСТОВ АВТОРА
        author_comment_rating = sum([comment.rate for comment in self.comment_set.all()])  # comment ratings
        post_comment_ratings = sum([post.get_summary_comments_rating() for post in self.post_set.all()])
        self.rating = posts_rating + post_comment_ratings + author_comment_rating
        self.save()
        return self.rating



class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=255, unique=True, verbose_name='Название')

    def __str__(self):
        return self.name


class Post(models.Model):
    post = 'PS'
    news = 'NS'

    TITLE = [
        (post, "Статья"),
        (news, "Новость")
    ]

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    post_or_news = models.CharField(max_length=2, choices=TITLE, default=post, verbose_name='Статья')
    time_in = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    categories = models.ManyToManyField(Category, through='PostCategory', verbose_name='Темы')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    vote = models.IntegerField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.title

    def like(self):
        self.vote += 1
        self.save()
        return self.vote

    def dislike(self):
        self.vote -= 1
        self.save()
        return self.vote

    def preview(self):
        return f'{self.text[:124]}...'

    def get_summary_comments_rating(self):
        return sum([comment.rate for comment in self.comment_set.all()])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    post = models.ForeignKey(Post, on_delete=models.CASCADE)           # связь «один ко многим» с моделью Post;
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')   # связь «один ко многим» со встроенной моделью User
    text = models.TextField(max_length=255, verbose_name='Текст')                          # текст комментария;
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время записи')    # дата, время комментария;
    rate = models.DecimalField(default=0.0, max_digits=4, decimal_places=1, verbose_name='Рейтинг')         # рейтинг комментария.

    def __str__(self):
        return f'{self.text}'

    def like(self):
        self.rate += 1
        self.save()
        return self.rate

    def dislike(self):
        self.rate -= 1
        self.save()
        return self.rate


    # def __str__(self):
    #     return self.author
    #
    # def __str__(self):
    #     return self.text

    # def like(self):
    #     return self.get_queryset().filter(vote__gt=0)
    #
    # def dislike(self):
    #     return self.get_queryset().filter(vote__lt=0)
    #
    # def like(self):
    #     return self.get_queryset().filter(vote__gt=0)
    #
    # def dislike(self):
    #     return self.get_queryset().filter(vote__lt=0)
    #
    # def sum_rating(self):
    #     return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0
    #
    # def preview(self):
    #     pass