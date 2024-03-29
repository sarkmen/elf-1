from django.db import models

'''
    선생님께,
    엘프팀이 만드려고 하는 사이트는 yelp.com과 유사한 리뷰사이트입니다.
    models.py 의 주요 class는 하단에 위치한 Store, User, Review, Comment 입니다.

'''


class Area(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SubArea(models.Model):
    parent = models.ForeignKey(Area)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    parent = models.ForeignKey(Category)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Store(models.Model):
    ## 업체의 이름, 주소, 전화번호, 업체의 소개, 운영시간, 웹사이트
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    tel = models.CharField(max_length=20, blank=True)
    intro = models.TextField(max_length=500, blank=True)
    hours = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=200, blank=True)

    ## 업체에 대한 사진: user들이 업체에 대한 사진을 올리면 여기로 등록되도록함. 구현방법은 모르겠습니다.
    photo = models.ImageField(blank=True)

    ## 업체의 리뷰평점: 유저들이 새롭게 리뷰달 때마다 갱신됨. 최소 0점 최대 10점으로 구간제한 필요.
    store_rating = models.FloatField(default=0)

    ##area는 서울, 인천, 대전 등의 큰 구역, sub_area는 그 하위구역을 의미. 각 독립된 위젯으로 구현.
    ##각 하나의 업체는 단 한 개의 area와 sub_area를 가지므로 ForeignKey라고 생각.
    ##area와 sub_area가 어떤 관계를 갖도록 해야할지 잘 모르겠습니다.
    area = models.ForeignKey(Area)
    sub_area = models.ForeignKey(SubArea)

    ##하나의 업체는 여러가지의 category와 여러가지 sub_category에 속할 수 있음 (사실상 tag및 sub_tag와 유사)
    ##위와 마찬가지로 category와 sub_category 간의 관계 설정에 어려움을 겪고 있습니다.
    category = models.ManyToManyField(Category)
    sub_category = models.ManyToManyField(SubCategory)

    ## geoDjango 또는 google map을 이용한 지도상 표현... ㅠㅠㅠ


    def __str__(self):
        return self.name



class User(models.Model):
    ## 엘프닷컴'에서는 이메일 그자체를 아이디로 받고자 합니다. (gitlab 가입방식처럼)
    email = models.EmailField()

    ## 유저의 비밀번호, 활동상 닉네임, 프로필이미지, 자기소개, 가입일자, 유저가 팔로잉하는 사람의 수, 유저를 팔로우 하는 사람의 수
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    profile = models.ImageField(blank=True)
    intro = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    n_following = models.PositiveSmallIntegerField(default=0, blank=True)
    n_follower = models.PositiveSmallIntegerField(default=0, blank=True)

    ## category와 sub_category의 choices()에 해당하는 것들을 체크박스로 주어서 중복선택하게 하고 싶습니다.
    ## BooleanField가 적절한 것인지 확신이 서지 않습니다.
    interest = models.BooleanField()

    ##유저가 자주가는 곳을 지정할 수 있게합니다.
    area = models.ForeignKey(Area)
    sub_area = models.ForeignKey(SubArea)

    ## 유저가 작성한 총 리뷰의 수
    n_review = models.PositiveSmallIntegerField(default=0, blank=True)



    def __str__(self):
        return self.email



class Review(models.Model):
    ## 리뷰의 대상이 되는 store를 의미
    review_on = models.ForeignKey(Store)

    ## 리뷰에서 0점 ~ 10점의 평점을 매길 수 있음. 이 평점이 store의 평균평점 계산에 사용되어야 함.
    user_rating = models.PositiveSmallIntegerField()

    ## 리뷰의 내용, 사진, 작성자, 작성일시
    content = models.TextField(blank=True)
    photo = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    ## 리뷰의 '좋아요' 갯수
    n_like = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return self.content



class Comment(models.Model):
    ## 코멘트의 대상이 되는 review를 의미
    comment_on = models.ForeignKey(Review)

    ## 코멘트의 내용, 작성자, 작성일시
    content = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content