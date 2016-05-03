#include <stdlib.h>
#include <stdio.h>

#include "main.h"

Array *createArray(unsigned int size) {
  Array *a = (Array*)malloc(sizeof(Array));
  a->size = size;
  a->data = (double*)malloc(sizeof(double)*size);
  return a;
}

int destroyArray(Array *array) {
  free(array->data);
  free(array);
  return 0;
}

int main() {
  Array *array = createArray(5);
  int i = array->size;
  while(i-- > 0) {
    array->data[i] = rand();
    printf("%f\n", array->data[i]);
  }
  destroyArray(array);
}
