# news_paper

>>> from django.contrib.auth.models import User
>>> user1 = User.objects.create_user('Viktor')       
>>> user1
<User: Viktor>
>>> user2 = User.objects.create_user('Anastasia')    
>>> user2
<User: Anastasia>


>>> from news.models import Author 
>>> Author.objects.create(user=user1)   
<Author: Viktor>
>>> Author.objects.create(user=user2) 
<Author: Anastasia>


>>> from news.models import Category
>>> Category.objects.create(name='Статья') 
<Category: Статья>
>>> Category.objects.create(name='Новость')
<Category: Новость>
>>> Category.objects.create(name='Спорт')
<Category: Спорт>
>>> Category.objects.create(name='Образование')
<Category: Образование>


>>> from news.models import Post
>>> author=Author.objects.get(id=3)
>>> Post.objects.create(author=author, post_or_news='PS', title='New Post Day', text='Есть много вариантов Lorem Ipsum, но большинство из них имеет не всегда приемлемые модификации') 
<Post: New Post Day>
>>> author=Author.objects.get(id=4) 
>>> Post.objects.create(author=author, post_or_news='PS', title='For anyone!', text='Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum')  
<Post: For anyone!>
>>> Post.objects.create(author=author, post_or_news='NS', title='Tomorrow come today', text='Его популяризации в новое время послужили публикация листов Letraset с образцами Lorem Ipsum в 60-х годах')
<Post: Tomorrow come today>


>>> Post.objects.get(id=2).post_category.add(Category.objects.get(id=4))
>>> Post.objects.get(id=4).post_category.add(Category.objects.get(id=3))


>>> Comment.objects.create(post=Post.objects.get(id=2),author=User.objects.get(id=1), text='Это круто!')   
<Comment: Это круто!>
>>> Comment.objects.create(post=Post.objects.get(id=4),author=User.objects.get(id=5), text='Здорово!')
<Comment: Здорово!>
 >>> Comment.objects.create(post=Post.objects.get(id=4),author=User.objects.get(id=6), text='Очень хорошо')
<Comment: Очень хорошо>
>>> Comment.objects.create(post=Post.objects.get(id=4),author=Author.objects.get(id=3).user, text='Нормально')   
<Comment: Нормально>



>>> Post.objects.get(id=2).like()
1
>>> Post.objects.get(id=2).like()
2
>>> Post.objects.get(id=4).like() 
1
>>> Post.objects.get(id=4).vote
1
>>> Post.objects.get(id=2).vote
2
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=1).dislike()
>>> Comment.objects.get(id=3).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=4).like()
>>> Comment.objects.get(id=1).rate
-1
>>> Comment.objects.get(id=2).rate
2
>>> Comment.objects.get(id=3).rate
1
>>> Comment.objects.get(id=4).rate
4
