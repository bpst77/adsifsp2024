### Teste para experimentar os algoritmos e observar o tempo levado para conclusão

Códigos usados para testar determinados algoritmos de ordenação(bubble, insertion, etc) em C:  
Créditos para [Daniel Viana](https://treinaweb.com.br/blog/conheca-os-principais-algoritmos-de-ordenacao)

Para testar cada um
```
//usando a maior parte do moddle xd
#include <stdio.h>
#include <stdlib.h>     /* necess�rio p/ as fun��es rand() e srand() */

#define TAMANHO 10 //tamanho a ordenar
int vet[TAMANHO];

void gerar_vetor(int tam)
{
	int i;
	srand(time(NULL));
	for (i=0; i < tam; i++) vet[i] = rand() % 10000;

}

//arrumar aqui os algoritmos
void bubble(){
	int j, i, temp;
	for (i=0; i<TAMANHO-1; i++){
	for (j=0; j<TAMANHO-i-1; j++){
		if (vet[j] > vet[j+1]){
			temp = vet[j];
			vet[j] = vet[j+1];
			vet[j+1] = temp;
			}
		}
	}
}

void insertion (){
	int i, j, x;
	for (i=2; i<=TAMANHO; i++){
		x = vet[i];
		j=i-1;
		vet[0] = x; 
		while (x < vet[j]){
			vet[j+1] = vet[j];
			j--;
		}
		vet[j+1] = x;
		}
	}

void selection (){
		int i, j, min, x;
		for (i=1; i<=TAMANHO-1; i++){
			min = i;
		for (j=i+1; j<=TAMANHO; j++){
				if (vet[j] < vet[min])
				min = j;
		}
		x = vet[min];
		vet[min] = vet[i];
		vet[i] = x;
		}
	}

void mergeSort(int posicaoInicio, int posicaoFim) {
		int i, j, k, metadeTamanho, *vetor, *vetorTemp;
		vetor = vet;
		if(posicaoInicio == posicaoFim) return;
		metadeTamanho = (posicaoInicio + posicaoFim ) / 2;
	
		mergeSort(posicaoInicio, metadeTamanho);
		mergeSort(metadeTamanho + 1, posicaoFim);
	
		i = posicaoInicio;
		j = metadeTamanho + 1;
		k = 0;
		vetorTemp = (int *) malloc(sizeof(int) * (posicaoFim - posicaoInicio + 1));
	
		while(i < metadeTamanho + 1 || j  < posicaoFim + 1) {
			if (i == metadeTamanho + 1 ) { 
				vetorTemp[k] = vetor[j];
				j++;
				k++;
			}
			else {
				if (j == posicaoFim + 1) {
					vetorTemp[k] = vetor[i];
					i++;
					k++;
				}
				else {
					if (vetor[i] < vetor[j]) {
						vetorTemp[k] = vetor[i];
						i++;
						k++;
					}
					else {
						vetorTemp[k] = vetor[j];
						j++;
						k++;
					}
				}
			}
	
		}
		for(i = posicaoInicio; i <= posicaoFim; i++) {
			vetor[i] = vetorTemp[i - posicaoInicio];
		}
		free(vetorTemp);
	}
	
void quick(int esq, int dir){
		int pivo = esq, i,ch,j;         
		for(i=esq+1;i<=dir;i++){        
			j = i;                      
			if(vet[j] < vet[pivo]){     
				ch = vet[j];               
				while(j > pivo){           
					vet[j] = vet[j-1];      
					j--;                    
				}
				vet[j] = ch;               
				pivo++;                    
			}
		}
		if(pivo-1 >= esq){              
			quick(esq,pivo-1);      
		}
		if(pivo+1 <= dir){              
			quick(pivo+1,dir);      
		}
	 }

 
int main() {
	int i, c;
		
	gerar_vetor(TAMANHO);
	
	printf("Escola o algoritmo de ordenacao: \n");
	printf("1 - Bubble Sort\n");
	printf("2 - Selection Sort\n");
	printf("3 - Insertion Sort\n");
	printf("4 - Merge Sort\n");
	printf("5 - Quick Sort\n");
	scanf("%d", &c);
	system("cls");

	printf("\nVetor antes de ser ordenado ==> ");
	for (i=0; i<TAMANHO; i++) printf(" %d ", vet[i]);


	switch(c)
	{
		case 1:
		bubble();
		break;

		case 2:
		selection();
		break;

		case 3:
		insertion();
		break;

		case 4:
		mergeSort(0, TAMANHO-1);
		break;

		case 5:
		quick(0, TAMANHO-1);
		break;
	}

	printf("\n\nVetor ordenado ==> ");
	for (i=0; i<TAMANHO; i++) printf(" %d ", vet[i]);

	return 0;
}
```

Completo
```
#include <stdio.h>
#include <stdlib.h>     /* necess�rio p/ as fun��es rand() e srand() */
#include <time.h>   	/* for clock_t, clock(), CLOCKS_PER_SEC      */

#define TAMANHO 10 //tamanho a ordenar
int vet[TAMANHO];

void gerar_vetor(int tam)
{
	int i;
	srand(time(NULL));
	for (i=0; i < tam; i++) vet[i] = rand() % 10000;

}

//arrumar aqui os algoritmos
void bubble(){
	int j, i, temp;
	for (i=0; i<TAMANHO-1; i++){
	for (j=0; j<TAMANHO-i-1; j++){
		if (vet[j] > vet[j+1]){
			temp = vet[j];
			vet[j] = vet[j+1];
			vet[j+1] = temp;
			}
		}
	}
}

void insertion (){
	int i, j, x;
	for (i=2; i<=TAMANHO; i++){
		x = vet[i];
		j=i-1;
		vet[0] = x; 
		while (x < vet[j]){
			vet[j+1] = vet[j];
			j--;
		}
		vet[j+1] = x;
		}
	}

void selection (){
		int i, j, min, x;
		for (i=1; i<=TAMANHO-1; i++){
			min = i;
		for (j=i+1; j<=TAMANHO; j++){
				if (vet[j] < vet[min])
				min = j;
		}
		x = vet[min];
		vet[min] = vet[i];
		vet[i] = x;
		}
	}

void mergeSort(int posicaoInicio, int posicaoFim) {
		int i, j, k, metadeTamanho, *vetor, *vetorTemp;
		vetor = &vet;
		if(posicaoInicio == posicaoFim) return;
		metadeTamanho = (posicaoInicio + posicaoFim ) / 2;
	
		mergeSort(posicaoInicio, metadeTamanho);
		mergeSort(metadeTamanho + 1, posicaoFim);
	
		i = posicaoInicio;
		j = metadeTamanho + 1;
		k = 0;
		vetorTemp = (int *) malloc(sizeof(int) * (posicaoFim - posicaoInicio + 1));
	
		while(i < metadeTamanho + 1 || j  < posicaoFim + 1) {
			if (i == metadeTamanho + 1 ) { 
				vetorTemp[k] = vetor[j];
				j++;
				k++;
			}
			else {
				if (j == posicaoFim + 1) {
					vetorTemp[k] = vetor[i];
					i++;
					k++;
				}
				else {
					if (vetor[i] < vetor[j]) {
						vetorTemp[k] = vetor[i];
						i++;
						k++;
					}
					else {
						vetorTemp[k] = vetor[j];
						j++;
						k++;
					}
				}
			}
	
		}
		for(i = posicaoInicio; i <= posicaoFim; i++) {
			vetor[i] = vetorTemp[i - posicaoInicio];
		}
		free(vetorTemp);
	}
	
void quick(int esq, int dir){
		int pivo = esq, i,ch,j;         
		for(i=esq+1;i<=dir;i++){        
			j = i;                      
			if(vet[j] < vet[pivo]){     
				ch = vet[j];               
				while(j > pivo){           
					vet[j] = vet[j-1];      
					j--;                    
				}
				vet[j] = ch;               
				pivo++;                    
			}
		}
		if(pivo-1 >= esq){              
			quick(esq,pivo-1);      
		}
		if(pivo+1 <= dir){              
			quick(pivo+1,dir);      
		}
	 }

 
int main() {
	int i, c, ww;
		
	gerar_vetor(TAMANHO);

	double time_spent = 0.0; 	/* to store the execution time of code */
	
	printf("Escola o algoritmo de ordenacao: \n");
	printf("1 - Bubble Sort\n");
	printf("2 - Selection Sort\n");
	printf("3 - Insertion Sort\n");
	printf("4 - Merge Sort\n");
	printf("5 - Quick Sort\n");
	scanf("%d", &c);
	system("cls");

	clock_t begin = clock();		/* tempo inicial */

	switch(c)
	{
		case 1:
		for ( ww=0; ww<1000; ww++) bubble();
		break;

		case 2:
		for ( ww=0; ww<1000; ww++) selection();
		break;

		case 3:
		for ( ww=0; ww<1000; ww++) insertion();
		break;

		case 4:
		for ( ww=0; ww<1000; ww++) mergeSort(0, TAMANHO-1);
		break;

		case 5:
		for ( ww=0; ww<1000; ww++) quick(0, TAMANHO-1);
		break;
	}
		
	clock_t end = clock();		/* tempo final */

	/* 	calculate elapsed time by finding difference (end - begin) and
      		 dividing the difference by CLOCKS_PER_SEC to convert to seconds */
	time_spent += (double)(end - begin) / CLOCKS_PER_SEC;

	
	printf("\nO tempo gasto foi de %f seconds", time_spent);
	printf("\n\n");
	
	system ("PAUSE");
	return 0;
}
```
