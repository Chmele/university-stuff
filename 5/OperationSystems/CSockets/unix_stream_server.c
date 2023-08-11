#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <unistd.h>
#include <sys/time.h>

#define SOCK_PATH  "tpf_unix_sock.server"
#define DATA "Hello from server"

int main(void){
    int server_sock, client_sock, len, rc;
    int bytes_rec = 0;
    struct sockaddr_un server_sockaddr;
    struct sockaddr_un client_sockaddr;     
    char buf[1024*1024];
    int backlog = 10;
    memset(&server_sockaddr, 0, sizeof(struct sockaddr_un));
    memset(&client_sockaddr, 0, sizeof(struct sockaddr_un));
    memset(buf, 0, 1024*1024);                
    
    server_sock = socket(AF_UNIX, SOCK_STREAM, 0);
    server_sockaddr.sun_family = AF_UNIX;   
    strcpy(server_sockaddr.sun_path, SOCK_PATH); 
    len = sizeof(server_sockaddr);
    
    unlink(SOCK_PATH);
    rc = bind(server_sock, (struct sockaddr *) &server_sockaddr, len);
    struct timeval stop, start;
    gettimeofday(&start, NULL);
    rc = listen(server_sock, backlog);
    printf("socket listening...\n");
    client_sock = accept(server_sock, (struct sockaddr *) &client_sockaddr, (socklen_t *)&len);
    
    len = sizeof(client_sockaddr);
    rc = getpeername(client_sock, (struct sockaddr *) &client_sockaddr, (socklen_t *)&len);

    printf("waiting to read...\n");
    bytes_rec = recv(client_sock, buf, sizeof(buf), 0);
    gettimeofday(&stop, NULL);
    printf("\ntook %lu us\n for type AF_UNIX", (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec); 
    printf("DATA RECEIVED = %s\n", buf);

    
    memset(buf, 0, 1024*1024);
    strcpy(buf, DATA);      
    rc = send(client_sock, buf, strlen(buf), 0);
    printf("Data sent!\n");
    close(client_sock);
    close(server_sock);
    return 0;
}