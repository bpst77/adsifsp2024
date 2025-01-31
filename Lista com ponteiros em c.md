Lista com ponteiros (e alocação dinâmica: malloc()/free()) em c
```
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

struct cel{
	int dado;
	struct cel * prox;
		  };

typedef struct cel cel;

void add(cel * lista, int * N)
{
	cel * temp, *temp2;
	
	temp = (cel *) malloc(sizeof(cel));
	temp->prox = NULL;

	printf("Digite o valor a ser inserido: "); scanf("%d", &temp->dado);

	if (lista->prox==NULL) lista->prox = temp;
	else {temp2 = lista->prox;
		  while (temp2->prox != NULL) temp2 = temp2->prox;
		  temp2->prox = temp;
		 }
	*N+=1;
	printf("\nElemento adicionado");
}

void rem(cel * lista, int * N)
{
	if (lista->prox == NULL) {printf("Lista vazia!\n"); return;}
	else if (*N==1) {free(lista->prox); lista->prox = NULL; *N-=1; printf("Elemento removido\n"); return;}
	cel * temp, * temp2, * temp3;
	temp = lista->prox;
	int a=0, b=0;

	printf("Digite a posicao a ser removida: "); scanf("%d", &a);

		if (a<1 || a>*N) printf("Posicao invalida!\n");
		else if (a==*N)
		{
			while(b!=a-1) temp = temp->prox;
			temp2 = temp->prox;
			temp->prox = NULL;
			free(temp2);
			*N-=1;
			printf("Elemento removido\n");
		}
		else
		{
			while(b!=a-1) temp = temp->prox;
			temp2 = temp->prox->prox;
			temp3 = temp->prox;
			temp->prox = temp2;
			free(temp3);
			*N-=1;
			printf("Elemento removido\n");
		}
}

void imp(cel * lista)
{
	printf("\n");
	cel * temp = lista->prox;
	int a=0;

	while (temp != NULL)
	{
		printf("Elemento %d: %d\n", a+1, temp->dado);
		temp = temp->prox;
		a++;
	}
}

int main()
{
	struct cel * lista = (cel *) malloc(sizeof(cel));
	lista->prox = NULL;
	int m=0, n=0, w=1; int *N = &n;

	do{
	system("cls");
	printf("Menu da lista\n");
	printf("1 - Adicionar elemento\n");
	printf("2 - Remover elemento\n");
	printf("3 - Imprimir lista\n");
	printf("Digite a opcao desejada: "); scanf("%d", &m);
	switch(m)
	{
		case 1:
		add(lista, N);
		break;

		case 2:
		rem(lista, N);
		break;

		case 3:
		imp(lista);
		break;

		default:
		break;
	}
	printf("\nDigite 0 para sair: "); scanf("%d", &w);
	}while(w != 0);

	free(lista);
	return 0;
}
```
