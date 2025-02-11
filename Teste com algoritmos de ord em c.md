Código usado para testar tempo de execução de determinados algoritmos de ordenação(bubble, insertion, etc) em c

Completo
```
//usando a maior parte do moddle xd
#include <stdio.h>
#include <stdlib.h>     /* necess�rio p/ as fun��es rand() e srand() */
#include <time.h>   	/* for clock_t, clock(), CLOCKS_PER_SEC      */

#define TAMANHO 5000 //tamanho a ordenar
int vet[TAMANHO];
FILE *arq;
char filename[30]="c:arq_teste.txt";

int gera_arquivo_numeros(int tam)
{
	int i;
	arq = fopen(filename, "wt+");
	if (arq == NULL)
		return(-1);		/* falha na abertura do arquivo */
	else
		{
			/* arquivo aberto com sucesso */
			srand(time(NULL));
			for (i=0; i < tam; i++)
			{
						/* gerando 5000 valores aleat�rios na faixa de 0 a 10000 */
				vet[i] = rand() % 10000;
				if (i!=4999)
					fprintf(arq, "%d,", vet[i]);
				else
					fprintf(arq, "%d", vet[i]);
			}
			return 0;

		}
	fclose (arq);
}

void le_arquivo(int TAM){	/* faz a abertura do arquivo e leitura de uma quantidade de numeros */ 
	int i;
	arq = fopen(filename, "arq_teste.txt");
	if (arq == NULL)
		return(-1);		/* falha na abertura do arquivo */
	else
		{
			/* arquivo aberto com sucesso */
			srand(time(NULL));
			for (i=0; i < TAM; i++)
			{
						/* lendo 5000 valores aleat�rios na faixa de 0 a 10000 */
				fscanf(arq, "%d", &vet[i]);
			}

		}
	fclose (arq);
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

void insercao (int tam){
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

void selecao (){
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
		&vetor = vet;
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

 
int main(int argc, char *argv[]) {
	int i, j, c;
	int temp;
	int ww;
		
	//se necessário gerar o arquivo - gera_arquivo_numeros(5000);
	le_arquivo(TAMANHO);

	double time_spent = 0.0; 	/* to store the execution time of code */
	
	printf('Escola o algoritmo de ordenacao: \n');
	printf('1 - Bubble Sort\n');
	printf('2 - Selection Sort\n');
	printf('3 - Insertion Sort\n');
	printf('4 - Merge Sort\n');
	printf('5 - Quick Sort\n');
	scanf('%d', &c);
	system('cls');

	printf("\n\nVetor antes de ser ordenado ==> ");
	for (i=0; i<TAMANHO; i++) printf(" %d ", vet[i]);

	clock_t begin = clock();		/* tempo inicial */

	switch(c)
	{
		case 1:
		for ( ww=0; ww<1000; ww++) bubble();
		break;

		case 2:
		for ( ww=0; ww<1000; ww++) selection(TAMANHO);
		break;

		case 3:
		for ( ww=0; ww<1000; ww++) insertion();
		break;

		case 4:
		for ( ww=0; ww<1000; ww++) merge(0, TAMANHO-1);
		break;

		case 5:
		for ( ww=0; ww<1000; ww++) quick(((TAMANHO/2)-1), TAMANHO/2);
		break;
	}
		
	clock_t end = clock();		/* tempo final */

	/* 	calculate elapsed time by finding difference (end - begin) and
      		 dividing the difference by CLOCKS_PER_SEC to convert to seconds */
	time_spent += (double)(end - begin) / CLOCKS_PER_SEC;

	printf("\n\nVetor ordenado ==> ");
	for (i=0; i<TAMANHO; i++) printf(" %d ", vet[i]);
	
	printf("\nO tempo gasto foi de %f seconds", time_spent);
	printf("\n\n");
	
	system ("PAUSE");
	return 0;
}
```

PARA TESTES
```
aaaa
```
