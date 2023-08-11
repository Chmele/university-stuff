#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/time.h>
#include <poll.h>


void INET_TCP(){
	struct timeval stop, start;
    gettimeofday(&start, NULL);
    char* hello = "Hello";
    struct sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(6060);
    int addrlen = sizeof(address);
    char buffer[1024*1024] = {0};
    int tcp = socket(AF_INET, SOCK_STREAM, 0);
    bind(tcp, (struct sockaddr*)&address, addrlen);
    listen(tcp, 3);
    int new_socket = accept(tcp, (struct sockaddr*)&address, (socklen_t*)&addrlen);
    read(new_socket, buffer, 1024);
    printf("%s\n", buffer);
    send(new_socket, hello, strlen(hello), 0);
    gettimeofday(&stop, NULL);
    printf("\ntook %lu us\n for type AF_INET", (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec); 
}

int main(){
	INET_TCP();
}