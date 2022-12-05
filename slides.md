---
theme: seriph
background: >-
  https://images.unsplash.com/photo-1547499681-28dece7dba00?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=1080&ixid=MnwxfDB8MXxyYW5kb218MHw5NDczNDU2Nnx8fHx8fHwxNjY5Mzc5Mjkz&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1920
class: text-center
highlighter: shiki
lineNumbers: true
info: |
  ## Backend communication design patterns
  TechTack session.
drawings:
  persist: false
css: unocss
title: TechTalks
---

# TechTalks
## Software architecture and communication design patterns
 
 <span class="px-2 py-1 rounded">Monday, Decemper 5 · 10:30AM – 12:00PM</span> 
<div class="pt-12">
  <a href="https://meet.google.com/hph-gjkr-hbg" target="_blank" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Join with Google Meet <carbon:arrow-right class="inline"/>
  </a>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/OsamaHaikal/Software-architecture-and-communication-design-patterns/tree/master/codeExamples" target="_blank" alt="GitHub"
    class="text-xl icon-btn opacity-50 !border-none !hover:text-white">
    Code Examples
    <carbon-logo-github />

  </a>
</div>


---
layout: two-cols
image: >-
  https://images.unsplash.com/photo-1616362258782-7511b61686ea?crop=entropy&cs=tinysrgb&fit=crop&fm=jpg&h=1080&ixid=MnwxfDB8MXxyYW5kb218MHw5NDczNDU2Nnx8fHx8fHwxNjY5Mzc5ODkx&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1920
---

# Table of contents

<Toc />


<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>


---

# Tier

Tier defines the physical separation of components in an application or a service. This separation is at a component level, not the code level(layers).

These layers are at the code level. The difference between layers and tiers is that layers represent the conceptual/logical organization of the code, whereas tiers represent the physical separation of components.

What about Django MVT?

`Model, View, and Template are the three layers`

Two tier apps implements the client server arch, the business logic is either on the Client side or `database` side.

In a three-tier application, the user interface, business logic, and the database all reside on different machines and, thus, have different tiers. They are physically separated.

<!--
Difference Between Layers and Tiers - Baeldung:
https://www.baeldung.com/cs/layers-vs-tiers#:~:text=On%20the%20other%20hand%2C%20the,tiers%2C%20we%20mean%20its%20topology.
-->

---

# Example Of N tier architecture
<img src="https://i.ytimg.com/vi/qbDkBPpmjJM/maxresdefault.jpg">


---

# Client-server communication

The architecture works on a request-response model. The client sends the request to the server for information and the server responds with it.

The user interface runs on the client. In very simple terms, a client is a gateway to our application. 


|     |     |
| --- | --- |
| Thin | Thick|
| <kbd>just the user interface of the application. It contains no business logic of any sort.</kbd>| <kbd>holds all or some part of the business logic.</kbd>


---

# Request Response Model

A will send a request to B

|	|	|
|---|---|
|A|B|
must be able to parse/understand the response| must be able to parse the request

So client and server must define a structure for the request and response ( protocol, message format) for serialization and derserialziation proess

( request, response waiting example)
HTTP request

```py{2,3}
GET / HTTP1.1
Headers
BODY
```

<!--
=
-->

---
class: px-20
---

# Is it enough?

Questions:

what if client disconnect?

what if server can not handle the request right now?

what if the request requires long process?

and a lot of limitations of this model

can i do work while waiting?

Ex: 
1. whenever a user publish new video, we need to notify all folowers

imagine the client needs to ask the server multiple times if there are a new notification or not? how many useless requests and empty responses we will get?


---
preload: false
---

# HTTP PUSH

So we can say that if the server holds the information then make sense that server should push the info as soon as it is availalbe without waiting the client to ask.


1. the client initiates a request 
2. Using this established connection, the server can send any new updated down to the client as soon as they are available. 
3. The client does not need to repeatedly request for updates from the server 
4. This helps to reduce the load on the network with the advantage that the updates are received in a timely manner. 
5. A drawback to this style is that the server has to maintain connection to the client which creates certain overhead on the server.


---

# Short/Long pooling

Usecase: request process time is long (export, upload) ( client can disconnect)

|||
|-|-|
Short Pooling|Long Pooling
client requets andserver respond with a key ( handler ) Server starts the process or put in a queue
client keeps asking (pooling) client keeps asking (pooling)
server keeps responding with no till get the result | server  keeps the connection open(with timeout)and waits
It is a breakdown of long req-res to multiple short req-res | It is based on getting the response. So, It is used for those applications that don’t want empty responses.

<!--
https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html#sqs-short-polling
-->

---

# SSE Server Sent Events

<img src="https://images.development.bytewax.io/sse_architecture_9a580e0ec8.jpg">

---
preload: false
---

Server

```js{all|2}
app.get("/stream", (req,res) => {
    res.setHeader("Content-Type", "text/event-stream");
    send(res);
})
```

Client

```js{all|5-6}
function rintMessage(message) {
  console.log(message)
}

let sse = new EventSource("http://localhost:8080/stream");
sse.onmessage = printMessage
```

---
title: Monloith
---

# Monloith

#### How can we have a loosly coupled monolith application?

Do you have boundaries?

A boundary is what this part of the codebase (business) is responsible for ( SOLID! ) ( the business capabilities and data access (RW)

<img src="https://cloud.google.com/static/architecture/images/microservices-architecture-introduction-monolithic-application.svg" width="600">
---
title: Message Broker and Queues
---

# Message Queue

### Recap
Can i do work while waiting?

Do i need to wait for other work to complete if i already done with my job

A message queue is a form of asynchronous service-to-service communication used in serverless and microservices architectures. Messages are stored on the queue until they are processed and deleted. Each message is processed only once, by a single consumer. Message queues can be used to decouple heavyweight processing, to buffer or batch work, and to smooth spiky workloads.


<img src="https://d1.awsstatic.com/product-marketing/Messaging/sqs_seo_queue.1dc710b63346bef869ee34b8a9a76abc014fbfc9.png">


---
title: RabbitMQ
---

# RabbitMQ ([docs](https://www.rabbitmq.com/), [tutorial](https://www.youtube.com/playlist?list=PLalrWAGybpB-UHbRDhFsBgXJM1g6T4IvO))

Message queuing fulfills this purpose by providing a means for services to push messages to a queue asynchronously and ensure that they get delivered to the correct destination. To implement a message queue between services, you need a message broker, think of it as a mailman, who takes mail from a sender and delivers it to the correct destination.

RabbitMQ consists of:
1. producer — the client that creates a message
2. consumer — receives a message
3. queue — stores messages
3. exchange — enables to route messages and send them to queues


---

The system functions in the following way:
1. producer creates a message and sends it to an exchange
2. exchange receives a message and routes it to queues subscribed to it
3. consumer receives messages from those queues he/she is subscribed to
One should note that messages are filtered and routed depending on the type of exchange.

<img width="700" src="https://miro.medium.com/max/1400/0*xHZPA79AzJ_3tyWP">

---
title: References
---
# References

### Youtube :
1. Architecture
https://www.youtube.com/playlist?list=PLThyvG1mlMzkQklYlHp_CdO5IEJ3i_ary

2. Loosely Coupled Monolith
https://www.youtube.com/playlist?list=PLThyvG1mlMznIDBtd5HadrmC5hayjpCtI

### Articles:
1. Monolith to MicroServices: 
https://cloud.google.com/architecture/microservices-architecture-introduction

2. Long pooling Queue in aws https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html#sqs-short-polling.

### Udemy: 
1. https://www.udemy.com/course-dashboard-redirect/?course_id=4953660


---
layout: center
---

#
thank you
