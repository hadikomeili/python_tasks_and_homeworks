# Maktab 52 - Django
## Task 5: Advanced models (Model Inheritance)

----
**A.** Implement a **abstract** model named `TimestampMixin` that contains 3 useful timestamp attributes:
1. Create timestamp: auto_now_add=True
2. Modify timestamp: auto_now=True
3. Delete timestamp: default=None, null=True, blank=True (useful on logical delete)

Then Write the `Timestamp.logical_delete(self)` method into the `TimestampMixin` that simulates the object deletion.


**B.** Implement `Cashier` model that extends from django built-in `User` and `TimestampMixin`  
Then add some extra attributes: 
1. Phone number
2. National code
3. Address

