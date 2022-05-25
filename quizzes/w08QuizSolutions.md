# SEI Week 8 Assessment - Answer Key

## Django Routes

1. Which is the correct route using Django urls?
    ``` python
    path('/index', views.index, name='index')
    path('index/', views.index, name='index')
    path('/index/', views.index, name='index')
    ```

    ### Solution:

    ```python
    path('index/', views.index, name='index')
    ```

2. Write the Django route using the `path()` function for viewing the detail page for a cat. The route may reference a CBV or a View Function.

    ### Solution:

    ```python
    path('cats/<int:cat_id>/', views.cats_detail, name='detail')
    ```
    or
    ```python
    path('cats/<int:pk>/', views.CatDetail.as_view(), name='detail')
    ```

## Django Models and Admin Functionality

3. After you create a model, what two terminal commands must you run in terminal to synchronize the databases's schema with the app's models?

    ### Solution:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

4. Before the admin portal can interact with a particular model, that model must first be r_______ in the admin.py module.

    ### Solution:

    ```
    register
    ```

## Django One to Many Relationships 

5. In a `Trip --< Route` relationship, which Entity/Model will need to hold the foreign key?

    ### Solution:

    ```
    Route (the many/belongs-to side)
    ```

6. In the `models.ForeignKey()` method, why is `on_delete=models.CASCADE` required?

    ### Solution:

    ```
    It ensures that all child objects/records are deleted when their parent is deleted preventing orphaned objects/records.
    ```

## Django Many to Many Relationships

7. When creating a Many-to-Many relationship using `models.ManyToManyField()`, Django will automatically/transparently create a ____ table in the database necessary to implement a M:M relationship in a relational database.

    ### Solution:

    ```
    join
    ```

8. Assuming a Trip >--< Tag relationship and the following code:

    ```python
    trip.tag_set.add(<arg>)
    ```
    
    What **two** "things" can you provide for `<arg>`?  (1/2 point each)

    ### Solution:

    ```
    A tag object/instance or its id
    ```

## Django Authentication and Authorization

9. What piece of code is used to access the logged in user in a view function?

    ### Solution:

    ```python
    request.user
    ```

10. How are view functions "protected" from anonymous users in Django?

    ### Solution:

    ```python
    # By using the `login_required` decorator

    @login_required
    def trip_create(request):
    ```
