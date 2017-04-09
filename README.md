# Copy-Move Detection on Digital Image using Python
This is a copy-move forgery detection script on digital images using Python Language.

## Features
### Server side:
  - Monitor all message's pakcet (sender, reciever, message content)
  - Real-time list of user online for easier management
  - Force kick a user by type ```kill [username]```
![Server screenshoot](/screenshot/06_server_monitoring.PNG?raw=true)

### Client side:
  - Send any message typed in message box, and it will be broadcasted to all user within the same group
  - Send private message typed in message box with a format ```@[username] [messages]```, and only both sender and receiver will be able to see the message
![Server screenshoot](/screenshot/05_client_otherUserJoined.PNG?raw=true)

## Getting Started
Make sure you already have [JDK 8](http://www.oracle.com/technetwork/java/javase/downloads/jdk-netbeans-jsp-142931.html) installed.
- To run: Simply execute the MultiChatGUIServer.jar for the server side, or execute MultiChatGUIClient.jar for the client side
- To modify: Import the source code to your prefered IDE, compile/build it, and run the JAR executable

## Starting
- Starting server
  1. Execute MultiChatGUIServer.jar
  2. Decide the port number to be used and fill it in port label (default port will be 1234)
  3. Click _Hidupkan_ to turn on the server
  4. All client's operation will be monitored and printed in server's log message label
  5. For terminating the service, click _Matikan_
- Starting client
  1. Execute MultiChatGUIClient.jar
  2. Decide the host and fill it in _Host_ label, also the port (default is 1234)
  3. Input your preferable username. If no username is typed, the system will automatically generate random guest user
  4. Click _Sambung_ to login to chat network
  5. Start chatting by typing your message on the message label and click _Kirim_ to send your message
  5. To quit, simply click quit button or type ``` /quit ``` in the message label
  
## Built With
* [Netbeans 8.2](http://www.oracle.com/technetwork/java/javase/downloads/jdk-netbeans-jsp-142931.html) - IDE
* [Java-JDK 8](http://www.oracle.com/technetwork/java/javase/downloads/jdk-netbeans-jsp-142931.html)

## Authors
* **Rahmat Nazali S** - [LinkedIn](https://www.linkedin.com/in/rahmat-nazali-salimi-43391a13b/) - [HackerRank](https://www.hackerrank.com/rahmatNazali)

## License
This project is licensed under the GPL License - see the [LICENSE.md](/LICENSE) file for details

## Important note
This is an implementation of a very simple but well functioned chatting application utilize local network, and so the message was not encrypted at all. This means that implementation for professional use should be avoided, since the messages may be easily sniffed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
