struct Array {
  double *data;
  unsigned int size;
};

typedef struct Array Array;

Array* createArray(unsigned int size);
