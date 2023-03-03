### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  Python is typically used for backend while javascript is used typically for frontend. Python uses whitespace and indents to structure its code instead of brackets like JS. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  You can use the get() method, or a try/except block

- What is a unit test?
  It is a test used to test specific functions in a code and smaller units to make sure they are working independently 

- What is an integration test?
  Integration tests test how functions are working together and how they are interacting to make sure they are giving the correct outputs

- What is the role of web application framework, like Flask?
  Helps to build wabsites quick and efficiently by giving you a framework and structure to build off of instead of having to write everything from scratch

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  The route url parameter is used more for identifying a specific endpoint or if you are passing more complex information, where as the query parameters or more for modifying or filtering the information.

- How do you collect data from a URL placeholder parameter using Flask?
  You can define the placeholder using <> brackets

- How do you collect data from the query string using Flask?
  You would used request.args to get the data

- How do you collect data from the body of the request using Flask?
  You would use request.form

- What is a cookie and what kinds of things are they commonly used for?
  It is a small piece of data used to store information from the user such as preferences, login info, personalization or even shopping carts

- What is the session object in Flask?
  Allows storage of data on the server side instead of the users device by storing a cookie with session Id data then the actual session data is stored on the server

- What does Flask's `jsonify()` do?
  Converts python data into a json string 