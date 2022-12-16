from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название группы тестов')
    description = models.CharField(max_length=50, verbose_name='Описание группы')
    slug = models.SlugField(unique=True, verbose_name='URL-ярлык')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Набор тестов'
        verbose_name_plural = 'Наборы тестов'


class Test(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название теста')
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='groups',
    )
    # questions = models.ManyToManyField(
    #     Question,
    #     #through='TestQuestion',
    #     #related_name='test_questions'
    # )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test = models. ForeignKey(
        Test,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='tests',
    )
    name = models.TextField(verbose_name='Вопрос')
    # answer = models.ManyToManyField(
    #     Answer,
    #     through='QuestionAnswer',
    #     related_name='answer1')

    def __str__(self) -> str:
        return self.name

    # def next_question(self, test_id):
    #     next_question = Question.objects.filter(test_id=test_id, id__gt=self.id).order_by('id').first()
    #     if next_question:
    #         return reverse('test_detail', kwargs={'test_id': test_id, 'id': next_question.id})

    def get_next(self):
        return Question.objects.filter(id__gt=self.id).order_by('id').first()

    # def get_absolute_url(self):
    #     return reverse('topics:test_detail', args=[str(self.id)])

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    name = models.CharField(max_length=150, verbose_name='Вариант ответа')
    question = models.ForeignKey(
        Question,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='answers',
    )
    check = models.BooleanField(default=False, verbose_name="Правильный ответ")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Ответы'


class TestQuestion(models.Model):
    question = models.ForeignKey(
        Question,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    test = models.ForeignKey(
        Test,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self) -> str:
        return f'{self.question}'

    class Meta:
        verbose_name = 'Тест-вопрос'
        verbose_name_plural = 'Тесты-вопросы'


class QuestionAnswer(models.Model):
    test = models.ForeignKey(
        Test,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='test'
    )
    question = models.ForeignKey(
        Question,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='question'
    )
    answer = models.ForeignKey(
        Answer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='answer'
    )
    check = models.BooleanField(default=False, verbose_name="Правильный ответ")

    def __str__(self) -> str:
        return f'{self.question}'

    class Meta:
        verbose_name_plural = 'Создать тест (вопросы и ответы)'

