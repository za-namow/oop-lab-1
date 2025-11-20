This lab focuses on teaching you how to apply object-oriented programming concepts by building a simple data-processing system. You work with real datasets and create classes that behave like a tiny database engine, allowing you to load, filter, combine, and analyze information. The goal is to understand how objects interact, how data flows between them, and how methods can transform that data.

The project is organized into a few key parts. You have CSV files containing city and country data, a DataLoader class to read those files, a Table class that represents each dataset, and a DB class that stores and manages the tables. The main script ties everything together by performing operations such as filtering cities, calculating averages, and joining tables.

Each class has a clear design role. DataLoader handles file input and converts CSV rows into Python dictionaries. Table acts like a mini version of a SQL table, with methods for filtering rows, aggregating values, and joining with other tables. DB serves as a simple memory-based storage system where you can insert tables and retrieve them by name, similar to how a real database works.

To test your code, you run the main Python file, which triggers all the data operations and prints the results. You’ll see outputs such as lists of cities in a specific country, temperature statistics, non-EU countries, and joined tables combining city and country data. This confirms that your classes work together properly.

Overall, the lab helps you understand how to structure programs using classes of OOP