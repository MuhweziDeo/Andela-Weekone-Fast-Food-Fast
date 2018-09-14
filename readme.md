# Fast-Food-Fast API

[![Build Status](https://travis-ci.org/MuhweziDeo/Andela-Weekone-Fast-Food-Fast.svg?branch=160364084-api-endpoints)](https://travis-ci.org/MuhweziDeo/Andela-Weekone-Fast-Food-Fast)

[![Coverage Status](https://coveralls.io/repos/github/MuhweziDeo/Andela-Weekone-Fast-Food-Fast/badge.svg?branch=160364084-api-endpoints)](https://coveralls.io/github/MuhweziDeo/Andela-Weekone-Fast-Food-Fast?branch=160364084-api-endpoints)

[![Maintainability](https://api.codeclimate.com/v1/badges/85578458cdbe4b22ab63/maintainability)](https://codeclimate.com/github/MuhweziDeo/Andela-Weekone-Fast-Food-Fast/maintainability)

# Api is Hosted ON
https://fast-foods-api.herokuapp.com/

## Getting Started
- To Run Locally git clone https://github.com/MuhweziDeo/Andela-Weekone-Fast-Food-Fast.git

## App Features
| EndPoint  | Function |
| ------------- | ------------- |
|GET /orders   | Get all the orders |
|GET /orders/orderId| Fetch a specific order  |
|POST /orders|Place a new order.  |
|PUT /orders/orderId|Update the status of an order. |



## Requirements
- In the directory with cloned repository there is a requirements.txt with all packages needed to run and test the app locally

## Installation 
- Run pip3 install -r requirements.txt(python3) to install recommended packages for python3
- If you are using python 2 run pip install -r requirements.txt 
- After packages are installed run python/python3 run.py to run server for the application
- In browser navigate to https://localhost:5000 to access app

## Running Tests
- Run py.test --cov in terminal

## Break Down of Tests
- [!Test_create_order]
Tests if an order has beeen created successfully

- Test_get_order
Tests if order with a specific orderID can be returned

- Test_get_orders
Tests if all created orders created can be returned

-Test_update_order
Tests if an order status can be successfully updated