
?
inputPlaceholder*
shape:?????????*
dtype0
?
VariableConst*a
valueXBV"HF?'??I?>???w?<No<???????¥?<Bt??W??<?^?쁂?k<?xf???>?D?ט<X	U?*
dtype0
I
Variable/readIdentityVariable*
T0*
_class
loc:@Variable
C

Variable_1Const*
dtype0*!
valueB"3۽?Ps=v?B=
O
Variable_1/readIdentity
Variable_1*
T0*
_class
loc:@Variable_1
U
MatMulMatMulinputVariable/read*
transpose_a( *
transpose_b( *
T0
,
addAddMatMulVariable_1/read*
T0
 
softmaxSoftmaxadd*
T0
:
output/dimensionConst*
value	B :*
dtype0
S
outputArgMaxsoftmaxoutput/dimension*
T0*
output_type0	*

Tidx0 