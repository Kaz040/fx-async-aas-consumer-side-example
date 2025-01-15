# fx-async-aas-consumer-side-example
This repository is used to develop consumer side Async Asset Administration Shell project. This is PoC implementation. 

The data flow in this project requires events that take place at the data provider side(factory operator). The events used are defined in [Fraunhofer's FA³ST Service documentation (MessageBus Section)](https://faaast-service.readthedocs.io/en/latest/interfaces/message-bus.html#id4).

This repo has a docker compose file that contains a subscriber application and an assx server docker image that are deployed together. All that is needed to do is just to **run** docker compose up through your cli. 

