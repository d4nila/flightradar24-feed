# flightradar24-feed
✈️ PoC that you can get LiveFeed from Flightradar24 using gRPC

The function `LiveFeed` returns a list of all aircraft belonging to the "Military and Government" category on Flightradar24, I also uploaded a proto file, you can change the request data to your own.
You can also substitute any `flightId` from the list with a link, for example, `https://www.flightradar24.com/32ae4d7e`, and by visiting it, you will see the aircraft belonging to this `flightId`.
## requirements
```
pip install grpcio grpcio-tools
```
## some contributors
Thanks a lot to [teidesu](https://t.me/teidumb) for reverse engineering.
