# Personal Budgeting

The goal of this project is to create a personal budgeting app that allows users to track their income and expenses, and view their spending habits.

## Description

User can enter income and expense detail on user interface. This information will be stored on database. This project also allows user to view previous entries and to visualize the user's budget data. 

![gui](images/gui.png)

![pie charts](images/charts.png)

## Getting Started

### Dependencies

* You can find all the libraries and version information used on this project in requirements.txt.
* It is required Python 3.10.9 or greater versions.

### Installing

* The following command will install the packages according to the configuration file
* $ pip3 install -r requirements.txt

### Executing program

* First I created a database to store user’s budget data. model.py file includes sql queries in order to create a table,
  insert data to table and query user’s entries. "create_connection" function helps to connect sqlite database and 
  "create_table" function uses sql_create_budget_table query in order to initialize database. For this project we created
  just one table which is budget table. But If we need to create more table we can add sql queries for these tables, 
  and it is too easy adding new tables.

```
  def initialize_db():
    """ initialize db"""
      conn = create_connection(filename)
      if conn is not None:
          create_table(conn, sql_create_budget_table)
      else:
          print("Error! cannot create the database connection.")
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)