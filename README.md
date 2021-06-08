# Kiril - Stat service

[GitHub](https://github.com/Anton6896/Kiril)

* Create service by `api/create` data must be positive in format (if obj found by date , will be agregated)

```
{
    "views":1,
    "clicks":2, 
    "cost":45.36,
    "date": "2021-01-15"
}
```

views, clicks is positive integer cost is decimal number (in us dollars), .0-99 max cents available

return : {"msg": "entry created"}, status=200. or appropriate error message {"msg": "some error"}

* Showing statistics by date `api/show_by_date ` date must be in format 'yyyy-mm-dd'

```
{
    "start_date":"2021-1-10",
    "end_date":"2021-1-23",
    "order":"clicks"
}
```

have additional feature is ordering by one of the values (views,clicks,cost,date)

* user can delete all data from table by `api/remove_all`

```
{
    "answer":"yes"
}
```

if answer yes data will be deleted

i am showed how to connect in settings.py to postgres todo is :

1. install [psycopg2](https://pypi.org/project/psycopg2/)
2. crete settings separator folder with 2 settings (one for local one for product)
3. in new `settings/__init__.py` check the system working place for adjust appropriate settings file data [example](https://github.com/Anton6896/django-one-1/tree/main/root/settings)
