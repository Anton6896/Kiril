# Kiril - Stat service


* Create service by ```api/create_new``` data must be positive in format
  ```
  {
    "views":1,
    "clicks":2, 
    "cost":45.36,
    "date": "2021-01-15"
  }
  ```
views, clicks is positive integer
cost is decimal number (in us dollars), .0-99 max cents available

return : {"msg": "entry created"}, status=200. 
or appropriate error message {"msg": "some error"}

* 