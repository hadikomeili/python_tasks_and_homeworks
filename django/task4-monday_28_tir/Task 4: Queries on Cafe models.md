# Maktab 52 - Django
## Task 4: Queries on Cafe models

----    
According to implemented models, use django queries to write some Model methods:  

1. `Order.filter_by_menuitem(menu_item)` : Filter Order objects by the menu item.
1. `MenuItem.filter_by_category(category)` : Filter Menu items by categories
1. `Order.filter_by_menuitem_category(category)` : Filter Orders by the menu item category.
1. `Order.today_orders()` : Filter Orders of today.
1. `Order.month_orders()` : Filter Orders of this month.
1. `MenuItem.max_price()` : find Maximum price of Menu items
1. `MenuItem.avg_price()` : find Average price of Menu items
1. `Orders.sum_cost(table)` : find Sum of Orders cost of a Table
1. `Orders.sum_today_cost()` : find Sum of today Orders cost
1. `Order.change_status(self, new_status)` : Change status of the order
1. `Table.add_order(self, menu_item, num)` : Add new order on the table
1. `Table.total_price(self)` : Calculate current orders total price on the table.

**Note:** Write your methods, similar to methods above, fit to your project models design. 