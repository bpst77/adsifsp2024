#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

/*
1 calcular conta baseado em consumo e tipo de cliente
2 3 valores aleatórios mostrados dependendo da opção escolhida
3 conversos de segundos para o padrão hh:mm:ss com parametros de referência
4 consultor de situação de alunos(aprovado, reprovado) com gravação em arquivo

OBS: o 4 usa um diretório para imprimir os arquivos okak
*/

float calcularConta(int cons, char tipo){
    int res, cons2;

    switch (tipo){
    case 'r':
        res = 5 + (cons*0.05);
        break;

    case 'c':
        cons2 = cons-80;
        if (cons >= 80) res = 80;
        else res = 80 + (cons2*0.25);
        break;

    case 'i':
        cons2 = cons-80;
        if (cons >= 100) res = 800;
        else res = 800 + (cons2*0.04);
        break;

    default:
        printf("\n"); printf("\n");
        printf("Opcao invalida!");
        break;
    }

    return res;
}

void conta(){
    int cons; char tipo; float res;
    printf("Usando o calculador de conta de agua");
    printf("\n"); printf("\n");

    printf("Digite a quantidade consumida, em metros cubicos: ");
    scanf("%i", &cons);

    printf("\n");
    printf("Lista: residencial, comercial e industrial");
    printf("\n");
    printf("Digite qual o tipo de cliente(r/c/i): ");
    scanf(" %c", &tipo);

    res = calcularConta(cons, tipo);

    printf("\n");
    printf("O valor da conta deste cliente sera de RS %.2f", res);
}

typedef struct nums{int a, b, c;} nums;

int aleat(){
    return rand() % 1000; //limite de 0 a 1000
}

void gerarNums(nums *Nums){
    srand(time(NULL));
    Nums->a = aleat(); Nums->b = aleat(); Nums->c = aleat();

    printf("\n");
    printf("Nums gerados: "); 
    printf("a) %i, b) %i, c) %i",Nums->a,Nums->b,Nums->c);
}

void bubble_sort (int vetor[], int n, int cres) {
    int k, j, aux;

    if (cres == 1){
    for (k = 1; k < n; k++) {
        for (j = 0; j < n - 1; j++) {
            if (vetor[j] > vetor[j + 1]) {
                aux          = vetor[j];
                vetor[j]     = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }}
    else {
    for (k = 1; k < n; k++) {
        for (j = 0; j < n - 1; j++) {
            if (vetor[j] < vetor[j + 1]) {
                aux          = vetor[j];
                vetor[j]     = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }
    }
}

void seq_nums(){
    printf("Usando o ordenador de nums aleatorios");
    int x, n; nums Nums;

    printf("\n");
    gerarNums(&Nums);
    printf("\n");
    printf("\n");

    printf("Lista de ordenacao: 1) ordem crescente");
    printf("\n");
    printf("2) ordem decrescente; 3) maior no meio, menor por ultimo");

    printf("\n"); printf("\n");
    printf("Digite o tipo de ordenacao(1/2/3): ");
    scanf("%i", &x);

    int vet[3] = {Nums.a, Nums.b, Nums.c}; int mai=0, men=1001, nor;

    //processando
    switch (x)
    {
    case 1: bubble_sort(vet, 3, 1); break;
    case 2: bubble_sort(vet, 3, 0); break;

    case 3:
        for (n=0; n<3; n++){
            if (mai < vet[n]){mai = vet[n];}
            if (men > vet[n]){men = vet[n];} 
        }
        nor = Nums.a;
        if (nor == mai || nor == men) nor = Nums.b;
        if (nor == mai || nor == men) nor = Nums.c;

        vet[0] = nor; vet[1] = mai; vet[2] = men;
        break;
    }

    printf("\n");
    printf("Sua sequencia: %i, %i, %i", vet[0],vet[1],vet[2]);
    memset(vet, 0, 3);
}

void converter(int *x){
    int h0, m0, s0;

    s0 = *x % 60;
    m0 = *x / 60;

    if (m0 >= 60) {
        h0 = m0 / 60;
        m0 = m0 % 60; 
    }

    int s1 = 0, s2 = 0, m1 = 0, m2 = 0, h1 = 0, h2 = 0;

    s1 = s0 / 10; s2 = s0 % 10;
    m1 = m0 / 10; m2 = m0 % 10;
    h1 = h0 / 10; h2 = h0 % 10;

    printf("Conversao(HH:MM:SS): %i%i:%i%i:%i%i",h1,h2,m1,m2,s1,s2);
}

void conv_seg(){
    printf("Usando o conversor de segundos em horas!");
    printf("\n");printf("\n");

    int x = 0;
    printf("Digite quantos segundos quer converter: ");
    scanf("%i", &x);

    printf("\n");
    converter(&x);
}

struct aluno{char nom[20]; int med; struct aluno *prox;};

typedef struct aluno aluno;

void add_aluno(aluno **lista){
    printf("Adicionando aluno");
    printf("\n"); printf("\n");
    aluno *a = malloc(sizeof(aluno));

    printf("Digite o nome: ");
    scanf(" %s", a->nom);

    printf("Digite a media: ");
    scanf("%i", &a->med);

    a->prox = NULL;

    if (*lista == NULL){
        *lista = a;
    } else{
        aluno *temp = *lista;
        while (temp->prox != NULL){
            temp = temp->prox;
        }
        temp->prox = a;
    }
}

void relat_aluno(aluno **lista){
    printf("Imprimindo em alunos.txt");
    printf("\n\n");
    aluno *a = malloc(sizeof(aluno));
    a = *lista;
    
    FILE *arq = fopen("alunos.txt", "w");
    
    while (a != NULL)
    {
        fprintf(arq, "Nome do aluno: %s\n", a->nom);

        fprintf(arq, "Media: %i / Situacao: ", a->med);
        if (a->med >= 6){ fprintf(arq, "aprovado");}
        else if (a->med < 4){ fprintf(arq, "reprovado");}
        else { fprintf(arq, "em exame");}
        fprintf(arq, "\n\n");

        a = a->prox;
    }

    fclose(arq);
    printf("Arquivo criado!");
}

void sit_aluno(){
    int n = 1;
    printf("Usando o consultor de situacao de alunos");
    printf("\n\n");

    aluno *lista = NULL;

    while (n == 1){
        add_aluno(&lista);
        printf("\n");

        printf("Adicionar mais um aluno?(1/0): ");
        scanf("%i", &n);
        printf("\n");
    }
    printf("\n\n");

    relat_aluno(&lista);

    while (lista != NULL) {
        aluno *aux = lista;
        lista = lista->prox;
        free(aux);
    }
}

void escolherPro(int m){
    switch (m)
    {
    case 1:
        conta();
        break;

    case 2:
        seq_nums();
        break;

    case 3:
        conv_seg();
        break;
    
    case 4:
        sit_aluno();
        break;

    default:
        printf("\n");
        printf("Valor invalido");
        break;
    }
}

int main(){
    int m = 0, conf = 1;
    printf("Menu do programa");
    printf("\n"); printf("\n");

    printf("Lista:");
    printf("\n");
    printf("1) calcular conta");
    printf("\n");
    printf("2) sequencia de numeros");
    printf("\n");
    printf("3) conversor de segundos");
    printf("\n");
    printf("4) situacao de alunos");

    printf("\n");
    while (conf == 1)
    {
        printf("\n");
        printf("Escolha um dos programas(1/2/3/4): ");
        scanf("%i", &m);
        printf("\n");
        escolherPro(m);

        printf("\n"); printf("\n");
        printf("Continuar com outro programa?(1): ");
        scanf("%i", &conf);
        printf("\n");
    }
    
    return 0;
}