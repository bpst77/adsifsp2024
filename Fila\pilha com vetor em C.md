Fila
```
#include <stdio.h>
#include <conio.h>
#define max 8

int main()
{
int fila[max], n, m, a, resp=1, ini=0, fim=0;

for(a=0;a<max;a++)
  	{
  		fila[a]=NULL;
  	};
  	
  do
  {
	system("cls");
	printf("Menu da fila:\n");
	printf("2 para inserir, 3 para remover\n");
	printf("4 para ver a fila toda, 5 para procurar valor\n\n");
	printf("Digite o que quer fazer:\n");
	scanf("%i",&m);
	
	switch(m)
	{
		case 2:
		if (fim==max)
		printf("A fila esta cheia");
		else
		{
		if (fila[0]!=NULL)
		fim=fim+1;
		printf("\n");
		printf("Digite o valor que quer inserir:\n");
		scanf("%d",&fila[fim]);
		};
		break;
		
		case 3:
		if (fila[ini]==NULL || fim==ini)
		printf("\nA fila esta vazia");
		else
		{
		fim = fim-1;
		printf("1 elemento removido");
		for (a=0; a<=max-1; a++)
		{
		fila[a] = fila[a+1];
		};
		fila[fim+1]=NULL;
		};
		break;
		
		case 4:
		printf("\nSituacao atual da fila\n");
		
		for (a=0; a<max; a++)
		{
		printf("%i ",fila[a]);
		};
		printf("\n");
		break;
		
		case 5:
		printf("\nQual o valor que deseja procurar?\n");
		scanf("%i",&n);
		
		for(a=0; a<max; a++)
		{
		if (fila[a]==n)
		printf("O valor %i está presente na posição %i da fila\n",&n,&a);
		};
		break;
		
		default:
		printf("\nNumero invalido\n");
	};
	
  printf("\n");		
  printf("Digite 1 para continuar:\n");
  scanf("%d",&resp);

  }while(resp==1);

};
```
Pilha
```
#include <stdio.h>
#include <stdlib.h>
#define max 8

int main()
{
int pilha[max], m, a, resp=1, topo=0;

for(a=0;a<max;a++)
  	{
  		pilha[a]=0;
  	};
  	
  do
  {
	system("cls");
	printf("Menu da pilha:\n");
	printf("2 para inserir, 3 para remover\n");
	printf("4 para ver o elemento no topo, 5 para verificar estado da pilha\n\n");
	printf("Digite o que quer fazer:\n");
	scanf("%i",&m);
	
	switch(m)
	{
		case 2:
		if (topo==max)
		printf("A pilha esta cheia");
		else
		{
        topo+=1;
		printf("Digite o valor que quer inserir:\n");
		scanf("%d",&pilha[topo]);
		};
		break;
		
		case 3:
		if (topo==0)
		printf("\nA pilha esta vazia!");
		else
		{
		pilha[topo]=0;
        topo -= 1;
		printf("1 elemento removido");
		};
		break;
		
		case 5:
		printf("\nSituacao atual da pilha\n");
		
		if (topo==max) printf("A pilha esta cheia!\n");
        else if (topo==0) printf("A pilha esta vazia!\n");
        else printf("A pilha nao esta vazia nem cheia!\n");
		break;
		
		case 4:
        printf("\nO elemento que esta no topo atualmente é %d",pilha[topo]);
		break;
		
		default:
		printf("\nNumero invalido\n");
	};
	
  printf("\n");		
  printf("Digite 1 para continuar:\n");
  scanf("%d",&resp);

  }while(resp==1);

};
```
