# Database chatbot
This chatbot uses LangChain Agent, LLM and SQLDatabaseToolkit. Agent uses LLM to decide what to do and uses SQLDatabaseToolkit to get results

# Getting started 
1) Get OpenAI API key add it to config.toml 
2) Use makeFile to get chatbot up and running.
3) Get Mysql up and running on docker and populate data using .sql in the repo. Or connect to existing Mysql instance by adding connection string to config.toml 
4) Hit localhost:5000 will take you to search form, and you can search database. 

# Notes
1) Does not perform DML. 
2) Handles SQL injection.
3) Can answer questions which require joins. And can perform aggregate functions on data.
4) Can tell how to join tables.
5) Understanding the table structure helps write good prompts.
6) Formatting can off for responses.
7) SQL generated to get answers are not always optimized. 
8) Uses SQLAlchemy under the hood.
9) Watch the console output to see how Agent is deciding what to do .
