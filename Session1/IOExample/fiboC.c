


#include <stdio.h>


int fib3(int n){
  int a = 0;
  int b = 1;
  
  for(int i = 1; i < n; i++){
    int t = a + b;
    a = b;
    b = t;
  }
  return b;
}

int main(){
  int n;
  scanf("%d", &n);
  printf("%d\n", fib3(n));
  return 0;
}
