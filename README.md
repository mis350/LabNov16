# Car Application

Project name is vehicles, app name is cars
admin username: test
admin password: 1234

Check the image attached to see the ER diagram 

The models and admin have been setup 

Explore the views, templates, urls

Today:
1. Modify the admin for Person & Car to:

   - Enable search on **name** or **model**. 

2. Modify the greeting page to complete the following queries.

   - **`list_bmw_cars`**:  To list all cars which belongs to "BMW MOTORS". Order by car **Price** (Descending Order) 
   - **`list_2020_cars`**:  To list all cars which have a make after or equal to the year of 2020. Order by Purchased Date (Ascending Order)
   - **`list_cars_purchased_2021`**:  To list all cars purchased between the dates of May 2021 & December 2021.
   - **`list_cars_purchased_november`**:  To list all cars purchased on the month of November.
   - **`list_cars_purchased_by_Abdullah_Ahmed`**: List all cars owned by **"Abdullah Ahmed"**.

3. Create a view to search for a car based on their **license_id**. Search must be done on the URL.

4. In **read_cars.html** templates, make the license of each car into a link that opens the corresponding **License ID** detailed view when clicked.