#FUNCIONES DEL ADD_TWO
#
#float add_float(float a, float b) {
#  return a + b;
#}
#
#int add_int(int a, int b) {
#  return a + b;
#}
#
#int add_float_ref(float *a, float *b, float *c) {
#  *c = *a + *b;
#  return 0;
#}
#
#int add_int_ref(int *a, int *b, int *c) {
#  *c = *a + *b;
#  return 0;
#}
#
import ctypes as C
math = C.CDLL('./libmymath.so')

a = math.add_int (3,4)

print 'probando el add_int(3,4) = ', a

math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]

b = math.add_float(3,4)

print 'probando el add_float(3,4) = ', b

tres_int = C.c_int(3)
cuatro_int = C.c_int(4)
res_int = C.c_int()

math.add_int_ref(C.byref(tres_int),C.byref(cuatro_int),C.byref(res_int))

c = res_int.value

print 'probando el add_int_ref = ', c

tres_float = C.c_float(3)
cuatro_float = C.c_float(4)
res_float = C.c_float()

math.add_float_ref(C.byref(tres_float),C.byref(cuatro_float),C.byref(res_float))

d = res_float.value

print 'probando el add_float_ref = ', d

#FUNCIONES DE ARRAYS
#
#int add_int_array(int *a, int *b, int *c, int n) {
#  int i;
#  for (i = 0; i < n; i++) {
#    c[i] = a[i] + b[i];
#  }
#  return 0;
#}
#
#float dot_product(float *a, float *b, int n) {
#  float res;
#  int i;
#  res = 0;
#  for (i = 0; i < n; i++) {
#    res = res + a[i] * b[i];
#  }
#  return res;
#}


