In this practice project, I utilized Django, a robust web framework renowned for its efficiency in constructing backend logic. Leveraging Django's built-in functionalities streamlined the development process, 
enhancing productivity and ensuring code reliability.
--------------------------------------------------
Key features employed include:

Django Admin Panel: Utilized the powerful Django Admin Panel to effortlessly manage and administer data entities such as products.
This intuitive interface facilitates seamless data manipulation, enhancing administrative efficiency.
Django ORM (Object-Relational Mapper): Leveraged Django's ORM to define the Product model, establishing a clear mapping between Python objects and database tables. 
This abstraction layer simplifies database interactions, promoting code clarity and maintainability.Developer Server: Deployed
 Django's built-in developer server to facilitate rapid development and testing. This lightweight server environment offers a convenient 
 platform for iterative development, enabling quick feedback and debugging.The project workflow entailed the following steps:

Model Creation: Defined the Product model with specified fields to accurately represent product data. 
This model serves as the backbone of the application, facilitating seamless data management.Migration Generation: Generated database
migrations to synchronize the model changes with the underlying database schema. 
This ensures consistency between the application's data model and the database structure.API Endpoint Implementation: Implemented a dedicated function in views.py to 
handle API requests and responses for the Product endpoint. This function efficiently processes incoming requests and returns 
JSON responses, adhering to RESTful principles.URL Configuration: Configured URL patterns in urls.py to map the defined view functionality to the corresponding endpoints. 
This routing mechanism directs incoming requests to the appropriate view functions, ensuring proper request handling.Integration with Project URLs: Integrated the app's URLs
into the project's main urls.py file, enabling access to the application's functionality through the server. This central routing mechanism ensures seamless navigation within the application.
Furthermore, to enrich the database with meaningful data, I added 10 dummy items to the Product database via the Django Admin Panel. Additionally, to automate the updating of the created_at field 
upon new product additions, a signal was implemented, ensuring data integrity and consistency.

For administrative access, the following credentials are provided:

Username: aousaf
Password: 123456789