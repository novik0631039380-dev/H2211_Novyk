import requests
import inspect

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunctioin(requests))

print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))