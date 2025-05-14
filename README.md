# The Gang Gets Generated

A simple text generator that takes in descriptions of episodes from It's Always Sunny in Philadelphia and uses a simple Markov-Chain based generator to produce "new" episode descriptions.

The app is built on a simple fastAPI implementation, containerized using Docker.

To build and execute:

```bash
docker build -t sunny-generator .
docker run -p 8000:8000 sunny-generator
```