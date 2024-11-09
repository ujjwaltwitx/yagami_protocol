YAGAMI PROTOCOL

This is Yagami protocol. I still don't know what are the params that are must😂. This is still in initial phase. I am planning to make the support for METHODS similar to HTTP. For now the payload data is being sent in JSON format but I am planning to use protobuf as the later one encodes the data to binary and is faster than JSON. Although protobuf also has it's own limitations, it's better. As mentioned earlier this is still in early phase and I don't know most of the part that lies ahead to be implemented. I will implement them as I study the requirements. You can find a simple client and server program that I chatgpied to test the parser. There are not a lot of functionalities present in the parser other than parsing the request. Seasoned developers will find the request similar to a HTTP request.
Contributions and suggestions are greatly appreciated.

This is an example of a custom request that you can send from the client.

GET /endpoint YAGAMI/1.0
Content-Type: json
Content-Length: 648
Content-Encoding: gzip
Expires: Fri, 13 March 2024 ->(planning to change this to second since epoch)

{"data" : "Yagami begins"}
