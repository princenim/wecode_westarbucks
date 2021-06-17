from django.db import models


#데이타베이스 안의 테이블 만들기
class Menu(models.Model):
    name = models.CharField(max_length=20) #db 필드 , column
    class Meta:
        db_table = 'menus' # 테이블 이름 

class Category(models.Model):
    name = models.CharField(max_length=20) 
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE) #menu_id

    class Meta:
        db_table = 'categories' # 테이블 이름

class Product(models.Model):
    name     = models.CharField(max_length=100) #db 필드 
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
            db_table = 'products' # 테이블 이름


# ------------------------------------------

# 알러지
class Allergy(models.Model):
    name = models.CharField(max_length=20) # 알러지 테이블 추가
    class Meta:
        db_table = 'allergy' # 테이블이름


# 드링크
class Drink(models.Model):
    name =  models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) #category_id

    class Meta:
        db_table = 'drink' # 테이블 이름


    