#include <stdio.h>
int um_de_dois (int num1, int num2); //declaração da função//
int main () {
int a = 100; // definição de variáveis locais//
int b = 20;
int ret_um;ret_um = um_de_dois(a, b);//chamada da função//
printf("O valor é: %d\n",ret_um);
return 0;
}

int  um_de_dois (int num1, int num2){
int result; // declaração de variáveis locais //
if (num1 > num2)
    result = num1;
else
   result = num2;
 return result;
}
