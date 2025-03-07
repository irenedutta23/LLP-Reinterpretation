# This file was automatically created by FeynRules 2.3.26
# Mathematica version: 11.2.0 for Mac OS X x86 (64-bit) (September 11, 2017)
# Date: Mon 20 May 2019 19:27:44



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
l2 = Parameter(name = 'l2',
               nature = 'external',
               type = 'real',
               value = 0.0,
               texname = '\\lambda _2',
               lhablock = 'Higgs',
               lhacode = [ 1 ])

l3 = Parameter(name = 'l3',
               nature = 'external',
               type = 'real',
               value = 0.0,
               texname = '\\lambda _3',
               lhablock = 'Higgs',
               lhacode = [ 2 ])

lR7 = Parameter(name = 'lR7',
                nature = 'external',
                type = 'real',
                value = 0.0,
                texname = '\\text{lR7}',
                lhablock = 'Higgs',
                lhacode = [ 3 ])

cosbma = Parameter(name = 'cosbma',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '',
                   lhablock = 'Higgs',
                   lhacode = [ 5 ])

xi = Parameter(name = 'xi',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\xi',
               lhablock = 'SFVINPUTS',
               lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011663900000000002,
               texname = '\\text{Gf}',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.118,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

GDR1x1 = Parameter(name = 'GDR1x1',
                   nature = 'external',
                   type = 'real',
                   value = 0.1,
                   texname = '\\text{GDR1x1}',
                   lhablock = 'YukawaGDR',
                   lhacode = [ 1, 1 ])

GDR2x2 = Parameter(name = 'GDR2x2',
                   nature = 'external',
                   type = 'real',
                   value = 0.0,
                   texname = '\\text{GDR2x2}',
                   lhablock = 'YukawaGDR',
                   lhacode = [ 2, 2 ])

GDR3x3 = Parameter(name = 'GDR3x3',
                   nature = 'external',
                   type = 'real',
                   value = 0.0,
                   texname = '\\text{GDR3x3}',
                   lhablock = 'YukawaGDR',
                   lhacode = [ 3, 3 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

mhc = Parameter(name = 'mhc',
                nature = 'external',
                type = 'real',
                value = 500.,
                texname = '\\text{mhc}',
                lhablock = 'MASS',
                lhacode = [ 37 ])

mh1 = Parameter(name = 'mh1',
                nature = 'external',
                type = 'real',
                value = 125.,
                texname = '\\text{mh1}',
                lhablock = 'MASS',
                lhacode = [ 25 ])

mh2 = Parameter(name = 'mh2',
                nature = 'external',
                type = 'real',
                value = 500.,
                texname = '\\text{mh2}',
                lhablock = 'MASS',
                lhacode = [ 35 ])

mh3 = Parameter(name = 'mh3',
                nature = 'external',
                type = 'real',
                value = 500.,
                texname = '\\text{mh3}',
                lhablock = 'MASS',
                lhacode = [ 36 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

whc = Parameter(name = 'whc',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{whc}',
                lhablock = 'DECAY',
                lhacode = [ 37 ])

Wh1 = Parameter(name = 'Wh1',
                nature = 'external',
                type = 'real',
                value = 4.2e-3,
                texname = '\\text{Wh1}',
                lhablock = 'DECAY',
                lhacode = [ 25 ])

Wh2 = Parameter(name = 'Wh2',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wh2}',
                lhablock = 'DECAY',
                lhacode = [ 35 ])

Wh3 = Parameter(name = 'Wh3',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{Wh3}',
                lhablock = 'DECAY',
                lhacode = [ 36 ])

mixh = Parameter(name = 'mixh',
                 nature = 'internal',
                 type = 'real',
                 value = '1.5707963267948966 - cmath.acos(cosbma)',
                 texname = '\\text{mixh}')

TH3x3 = Parameter(name = 'TH3x3',
                  nature = 'internal',
                  type = 'real',
                  value = '1',
                  texname = '\\text{TH3x3}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

GD1x1 = Parameter(name = 'GD1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GDR1x1',
                  texname = '\\text{GD1x1}')

GD2x2 = Parameter(name = 'GD2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GDR2x2',
                  texname = '\\text{GD2x2}')

GD3x3 = Parameter(name = 'GD3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GDR3x3',
                  texname = '\\text{GD3x3}')

GL1x1 = Parameter(name = 'GL1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{GL1x1}')

GL2x2 = Parameter(name = 'GL2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{GL2x2}')

GL3x3 = Parameter(name = 'GL3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{GL3x3}')

GU1x1 = Parameter(name = 'GU1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{GU1x1}')

GU2x2 = Parameter(name = 'GU2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{GU2x2}')

l7 = Parameter(name = 'l7',
               nature = 'internal',
               type = 'complex',
               value = 'lR7',
               texname = '\\lambda _7')

lI5 = Parameter(name = 'lI5',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{lI5}')

lI6 = Parameter(name = 'lI6',
                nature = 'internal',
                type = 'real',
                value = '0',
                texname = '\\text{lI6}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = '\\text{MW}')

TH1x1 = Parameter(name = 'TH1x1',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos(mixh)',
                  texname = '\\text{TH1x1}')

TH1x2 = Parameter(name = 'TH1x2',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.sin(mixh)',
                  texname = '\\text{TH1x2}')

TH2x1 = Parameter(name = 'TH2x1',
                  nature = 'internal',
                  type = 'real',
                  value = '-cmath.sin(mixh)',
                  texname = '\\text{TH2x1}')

TH2x2 = Parameter(name = 'TH2x2',
                  nature = 'internal',
                  type = 'real',
                  value = 'cmath.cos(mixh)',
                  texname = '\\text{TH2x2}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

mu2 = Parameter(name = 'mu2',
                nature = 'internal',
                type = 'real',
                value = 'mhc**2 - (l3*vev**2)/2.',
                texname = '\\text{mu2}')

GU3x3 = Parameter(name = 'GU3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((xi*ymt*cmath.sqrt(2))/vev)',
                  texname = '\\text{GU3x3}')

l1 = Parameter(name = 'l1',
               nature = 'internal',
               type = 'real',
               value = '-(-(mh1**2*cmath.cos(mixh)**2) - mh2**2*cmath.sin(mixh)**2)/(2.*vev**2)',
               texname = '\\lambda _1')

l4 = Parameter(name = 'l4',
               nature = 'internal',
               type = 'real',
               value = '(2*mh1**2 + 2*mh2**2 + 4*mh3**2 - 8*mhc**2 + 2*(-mh1**2 + mh2**2)*cmath.cos(2*mixh))/(4.*vev**2)',
               texname = '\\lambda _4')

lR5 = Parameter(name = 'lR5',
                nature = 'internal',
                type = 'real',
                value = '(2*(mh1**2 + mh2**2 - 2*mh3**2) - 2*(mh1 - mh2)*(mh1 + mh2)*cmath.cos(2*mixh))/(8.*vev**2)',
                texname = '\\text{lR5}')

lR6 = Parameter(name = 'lR6',
                nature = 'internal',
                type = 'real',
                value = '((-mh1**2 + mh2**2)*cmath.cos(mixh)*cmath.sin(mixh))/vev**2',
                texname = '\\text{lR6}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

mu1 = Parameter(name = 'mu1',
                nature = 'internal',
                type = 'real',
                value = '-(l1*vev**2)',
                texname = '\\text{mu1}')

l5 = Parameter(name = 'l5',
               nature = 'internal',
               type = 'complex',
               value = 'complex(0,1)*lI5 + lR5',
               texname = '\\lambda _5')

l6 = Parameter(name = 'l6',
               nature = 'internal',
               type = 'complex',
               value = 'complex(0,1)*lI6 + lR6',
               texname = '\\lambda _6')

mu3 = Parameter(name = 'mu3',
                nature = 'internal',
                type = 'complex',
                value = '-(l6*vev**2)/2.',
                texname = '\\text{mu3}')

I1a11 = Parameter(name = 'I1a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(GU1x1)',
                  texname = '\\text{I1a11}')

I1a22 = Parameter(name = 'I1a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(GU2x2)',
                  texname = '\\text{I1a22}')

I1a33 = Parameter(name = 'I1a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(GU3x3)',
                  texname = '\\text{I1a33}')

I2a11 = Parameter(name = 'I2a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GD1x1',
                  texname = '\\text{I2a11}')

I2a22 = Parameter(name = 'I2a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GD2x2',
                  texname = '\\text{I2a22}')

I2a33 = Parameter(name = 'I2a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GD3x3',
                  texname = '\\text{I2a33}')

I3a11 = Parameter(name = 'I3a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(GD1x1)',
                  texname = '\\text{I3a11}')

I3a22 = Parameter(name = 'I3a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(GD2x2)',
                  texname = '\\text{I3a22}')

I3a33 = Parameter(name = 'I3a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complexconjugate(GD3x3)',
                  texname = '\\text{I3a33}')

I4a11 = Parameter(name = 'I4a11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GU1x1',
                  texname = '\\text{I4a11}')

I4a22 = Parameter(name = 'I4a22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GU2x2',
                  texname = '\\text{I4a22}')

I4a33 = Parameter(name = 'I4a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'GU3x3',
                  texname = '\\text{I4a33}')

I5a33 = Parameter(name = 'I5a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I5a33}')

I6a33 = Parameter(name = 'I6a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I6a33}')

I7a33 = Parameter(name = 'I7a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt',
                  texname = '\\text{I7a33}')

I8a33 = Parameter(name = 'I8a33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb',
                  texname = '\\text{I8a33}')

