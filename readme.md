# Fast-Food-Fast API
This is a Food Ordering App where users can order fast foods

[![Build Status](https://travis-ci.org/MuhweziDeo/Andela-Weekone-Fast-Food-Fast.svg?branch=160364084-api-endpoints)](https://travis-ci.org/MuhweziDeo/Andela-Weekone-Fast-Food-Fast)

[![Coverage Status](https://coveralls.io/repos/github/MuhweziDeo/Andela-Weekone-Fast-Food-Fast/badge.svg?branch=160364084-api-endpoints)](https://coveralls.io/github/MuhweziDeo/Andela-Weekone-Fast-Food-Fast?branch=160364084-api-endpoints)

[![Maintainability](https://api.codeclimate.com/v1/badges/85578458cdbe4b22ab63/maintainability)](https://codeclimate.com/github/MuhweziDeo/Andela-Weekone-Fast-Food-Fast/maintainability)



## Getting Started
- To Run Locally git clone https://github.com/MuhweziDeo/Andela-Weekone-Fast-Food-Fast.git

- To access and use app on Postman, Use URL 
https://fast-foods-api.herokuapp.com/



## App Features
| EndPoint  | Function |
| ------------- | ------------- |
|GET /orders   | Get all the orders |
|GET /orders/orderId| Fetch a specific order  |
|POST /orders|Place a new order.  |
|PUT /orders/orderId|Update the status of an order. |


## Tools Used
- Flask[Python Web Framwork]
- Flask-Restplus[Flask extension for Building RestApis]
- Pytest[Testing Framework]


## Requirements
- In the directory with cloned repository there is a requirements.txt with all packages needed to run and test the app locally

## Installation 
- cd in directory with cloned respository
- Run 'pip3 install -r requirements.txt' to install recommended packages for python3 in terminal
- If you are using python 2 'run pip install -r requirements.txt' in terminal
- open terminal
- run "git checkout 160364084-api-endpoints"
- run "python/python3(depending on python version) run.py" to start server
- In browser navigate to https://localhost:5000 to access app

## Running Tests
- cd into directory with cloned repository
- open a terminal window
- Run 'py.test --cov' in terminal

## Break Down of Tests
1. Test_create_order
- Tests if an order has beeen created successfully

2. Test_get_order
- Tests if order with a specific orderID can be returned
3. Test_get_orders
- Tests if all created orders created can be returned

4. Test_update_order
- Tests if an order status can be successfully updated

## Authors
- Muhwezi Deo