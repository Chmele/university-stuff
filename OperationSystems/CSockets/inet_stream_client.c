#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#include <arpa/inet.h>

int main(int argc, char const* argv[])
{
	struct sockaddr_in serv_addr;
	char* hello = "Hello from client";
	char buffer[1024] = { 0 };
	int sock = socket(AF_INET, SOCK_STREAM, 0);

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(6060);
	inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);
    int client_fd = connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
	send(sock, hello, strlen(hello), 0);
	read(sock, buffer, 1024);
	printf("%s\n", buffer);
	close(client_fd);
	return 0;
}
