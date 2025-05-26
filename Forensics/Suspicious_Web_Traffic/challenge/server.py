#!/usr/bin/python3

import random
import os
import threading
import socketserver
import time
import sys

class Service(socketserver.BaseRequestHandler):

    def handle(self):
        self.send(f'''👋 Welcome to the Wireshark Packet Capture Challenge! 🕵️ In this challenge, you will be asked a series of questions based on the Wireshark packet capture included with this challenge.''')
        self.send("")

        while True:
            self.send("❓ Question 1: What is the first website that the user visited? Look carefully — the user visited both HTTP and HTTPS websites. Please enter the entire domain name including the protocol (http:// or https://).")

            if self.receive("https://espn.com"):
                self.send("✅ Correct! 🎉")
                self.send("")
                break
            else:
                self.send("❌ Incorrect. Please try again.")
                self.send("")

        while True:
            self.send("❓ Question 2: There was only one HTTP request made in the packet capture. To which IP address did the user make the request?")
            
            if self.receive("143.244.222.115"):
                self.send("✅ Correct! 🎉")
                self.send("")
                break
            else:
                self.send("❌ Incorrect. Please try again.")
                self.send("")
        
        while True:
            self.send("❓ Question 3: What is the host associated with this IP address? Please enter the entire domain name including the protocol (http://).")

            if self.receive("http://waynestateuniversity-ctf24-ustreasuryhack.chals.io"):
                self.send("✅ Correct! 🎉")
                self.send("")
                break
            else:
                self.send("❌ Incorrect. Please try again.")
                self.send("")

        while True:
            self.send("❓ Question 4: What is the response code that was sent back from the server in the HTTP response?")

            if self.receive("301"):
                self.send("✅ Correct! 🎉")
                self.send("")
                break
            else:
                self.send("❌ Incorrect. Please try again.")
                self.send("")

        while True:
            self.send("❓ Question 5: What cloud provider service was most likely used to create this packet capture? To find this, research where some of the common IP addresses originate from. Submit the name of the provider as one word, with only the first letter capitalized.")

            if self.receive("Digitalocean"):
                self.send("✅ Correct! 🎉")
                self.send("")
                break
            else:
                self.send("❌ Incorrect. Please try again.")
                self.send("")

        self.send("🏁 Wow! Great job analyzing this packet capture. Here is your flag: WSUCTF{1_am_a_Wireshark_m4ster}")

    def send(self, string, newline=True):
        if newline:
            string += "\n"
        self.request.sendall(string.encode())
    
    def receive(self, expectedResponse, prompt="> "):
        self.send(prompt, newline=False)
        response = self.request.recv(4096).strip()
        return response.decode().lower() == expectedResponse.lower()


class ThreadedService(socketserver.ThreadingMixIn, socketserver.TCPServer, socketserver.DatagramRequestHandler):
    pass

def main():
    port = int(sys.argv[2])
    host = str(sys.argv[1])
    server = ThreadedService((host, port), Service)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    print("🚀 Server started on port", port)

    while True:
        time.sleep(60)

if __name__ == "__main__":
    main()