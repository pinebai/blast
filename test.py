import math
from param import Param
# soDistance = input("please enter the actual stand-off distance (D) [m]: ")
# neQuantity = input("please enter the net explosive quantity (Q) [kg]: ")

soDist = 25
neQty = 25
TNT_EQ_FIGURE = 1

TNT_EQ_Fig = None
while True:
    TNT_EQ_FigInput = input("select explosive type:\n1. TNT\n2.RDX (Cyclonite)\n3. HMX \n4. Nitroglycerin (liquid)\n"
                            "5. Compund B (60% RDX 40% TNT)\n6. Semtex\n7. 60% Nitroglycerin dynamite\n\n"
                            "your selected type: ")
    if TNT_EQ_FigInput == '1':
        print('\nyou have selected TNT')
        TNT_EQ_Fig = 1
        break
    elif TNT_EQ_FigInput == '2':
        print('\nyou have selected RDX')
        TNT_EQ_Fig = 1.185
        break
    elif TNT_EQ_FigInput == '3':
        print('\nyou have selected HMX')
        TNT_EQ_Fig = 1.256
        break
    elif TNT_EQ_FigInput == '4':
        print('\nyou have selected Nitroglycerin (liquid)')
        TNT_EQ_Fig = 1.481
        break
    elif TNT_EQ_FigInput == '5':
        print('\nyou have selected TNCompund BT')
        TNT_EQ_Fig = 1.148
        break
    elif TNT_EQ_FigInput == '6':
        print('\nyou have selected Semtex')
        TNT_EQ_Fig = 1.25
        break
    elif TNT_EQ_FigInput == '7':
        print('\nyou have selected 60% Nitroglycerin dynamite')
        TNT_EQ_Fig = 0.6
        break
    else:
        raise SystemExit("you should select from the options")

TNT_EQ_WT = neQty * TNT_EQ_Fig
sc_dist = soDist / math.pow(TNT_EQ_WT, 0.3333)
log_sc_dist = math.log(sc_dist, 10)
print('TNT equivalent wt [kg]: ', TNT_EQ_WT)
print('scaled distance [m]: ', soDist)
print('\n')


"""
    get Ps
"""
obj_ps = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        -0.214362789151,
        1.35034249993
    ],
    'const_u_surface': [
        -0.214362789151,
        1.35034249993
    ],

    'list_slope_u_air': [
        -1.69012801396,
        0.00804973591951,
        0.336743114941,
        -0.00516226351334,
        -0.0809228619888,
        -0.00478507266747,
        0.00793030472242,
        0.0007684469735
    ],

    'list_slope_u_surface': [
        -1.6958988741,
        -0.154159376846,
        0.514060730593,
        0.0988534365274,
        -0.293912623038,
        -0.0268112345019,
        0.109097496421,
        0.00162846756311,
        - 0.0214631030242,
        0.0001456723382,
        0.00167847752266,
    ],

    'const_y': [
        2.611368669,
        2.78076916577
    ],

    'limits': [
        {
            'lower_limit': 0.0531,
            'upper_limit': 40
        },
        {
            'lower_limit': 0.064,
            'upper_limit': 40
        }
    ]
}

ps = Param(obj_ps)
# ps_ys = ps.get_y()
# print('Y for air and surface', ps_ys)
ps_ft_results = ps.get_ft_results()
# print('ps ft result', ps_ft_results)
ps_alog_ys = ps.get_alog_y()
# print('ps_alog_ys', ps_alog_ys)

for idx, ft_result in enumerate(ps_ft_results):
    if ft_result == 0:
        raise SystemExit("filtered result: 0")
    else:
        p_s = ps_alog_ys[idx]
        p_s = round(p_s, 3)
        if idx == 0:
            print('Ps(air): ', p_s)
        else:
            print('Ps(surface)', p_s)

'''
    get Is F(I) for Air
'''

obj_is_f1 = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        2.34723921354,
        3.24299066475
    ],
    'const_u_surface': [
        2.06761908721,
        3.0760329666
    ],

    'list_slope_u_air': [
        -0.443749377691,
        0.168825414684,
        0.0348138030308,
        -0.010435192824
    ],

    'list_slope_u_surface': [
        -0.502992763686,
        0.171335645235,
        0.0450176963051,
        -0.0118964626402
    ],

    'const_y': [
        2.38830516757,
        2.52455620925
    ],

    'limits': [
        {
            'lower_limit': 0.0531,
            'upper_limit': 0.792
        },
        {
            'lower_limit': 0.0674,
            'upper_limit': 0.955
        }
    ]
}

is_f1 = Param(obj_is_f1)
is_f1_ft_result = is_f1.get_ft_results()
# print('is_f1 ft result', is_f1_ft_result)
is_f1_alog_ys = is_f1.get_alog_y()
# print('is_f1_alog_ys', is_f1_alog_ys)

'''
    get Is F(II) for Air
'''
obj_is_f2 = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        -1.75305660315,
        2.30629231803
    ],
    'const_u_surface': [
        -1.94708846747,
        2.40697745406
    ],

    'list_slope_u_air': [
        -0.40463292088,
        -0.0142721946082,
        0.00912366316617,
        -0.0006750681404,
        -0.00800863718901,
        0.00314819515931,
        0.00152044783382,
        -0.0007470265899
    ],

    'list_slope_u_surface': [
        -0.384519026965,
        -0.0260816706301,
        0.00595798753822,
        0.0145445261077,
        -0.00663289334734,
        -0.00284189327204,
        0.0013644816227
    ],

    'const_y': [
        1.55197227115,
        1.67281645863
    ],

    'limits': [
        {
            'lower_limit': 0.792,
            'upper_limit': 40
        },
        {
            'lower_limit': 0.955,
            'upper_limit': 40
        }
    ]
}

is_f2 = Param(obj_is_f2)
is_f2_ft_result = is_f2.get_ft_results()
# print('is_f2 ft result', is_f2_ft_result)
is_f2_alog_ys = is_f2.get_alog_y()
# print('is_f2_alog_ys', is_f2_alog_ys)

sum_is_f = []
idx_cnt = 0
i_s = []
while idx_cnt < 2:
    sum_is_f.append(is_f1_alog_ys[idx_cnt] + is_f2_alog_ys[idx_cnt])
    if sum_is_f[idx_cnt] == 0:
        raise SystemExit("ERROR: sum of Is anti log y are 0")
    else:
        iss = sum_is_f[idx_cnt] * math.pow(TNT_EQ_WT, 0.3333)
        if idx_cnt == 0:
            print('Is (air): ', round(iss, 3))
        else:
            print('Is (surface): ', round(iss, 3))
        i_s.append(iss)
    idx_cnt = idx_cnt + 1
# print('Is', i_s)

'''
    get Pr
'''

obj_pr = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        -0.214362789151,
        1.35034249993
    ],
    'const_u_surface': [
        -0.240657322658,
        1.3663771922
    ],

    'list_slope_u_air': [
        -2.21400538997,
        0.035119031446,
        0.657599992109,
        0.0141818951887,
        -0.243076636231,
        -0.0158699803158,
        0.0492741184234,
        0.00227639644004,
        -0.00397126276058
    ],

    'list_slope_u_surface': [
        -2.21030870597,
        -0.218536586295,
        0.895319589372,
        0.24989009775,
        -0.569249436807,
        -0.11791682383,
        0.224131161411,
        0.0245620259375,
        -0.0455116002694,
        -0.0019093073888,
        0.00361471193389
    ],

    'const_y': [
        3.22958031387,
        3.40283217581
    ],

    'limits': [
        {
            'lower_limit': 0.0531,
            'upper_limit': 40
        },
        {
            'lower_limit': 0.0674,
            'upper_limit': 40
        }
    ]
}

pr = Param(obj_pr)
pr_ft_result = pr.get_ft_results()
# print('pr ft result', pr_ft_result)
pr_alog_ys = pr.get_alog_y()
# print('pr_alog_ys', pr_alog_ys)

for idx, ft_result in enumerate(pr_alog_ys):
    if ft_result == 0:
        raise SystemExit("filtered result: 0")
    else:
        p_r = pr_alog_ys[idx]
        p_r = round(p_r, 3)
        if idx == 0:
            print('Pr(air): ', p_r)
        else:
            print('Pr(surface)', p_r)
'''
    get Ir
'''

obj_ir = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        -0.204004553231,
        1.37882996018
    ],
    'const_u_surface': [
        -0.246208804814,
        1.33422049854
    ],

    'list_slope_u_air': [
        -0.903118886091,
        0.101771877942,
        -0.0242139751146
    ],

    'list_slope_u_surface': [
        -0.949516092853,
        0.112136118689,
        -0.0250659183287
    ],

    'const_y': [
        2.55875660396,
        2.70588058103
    ],

    'limits': [
        {
            'lower_limit': 0.0531,
            'upper_limit': 40
        },
        {
            'lower_limit': 0.0674,
            'upper_limit': 40
        }
    ]
}

ir = Param(obj_ir)
ir_ft_result = ir.get_ft_results()
# print('ir_ft_result', ir_ft_result)
ir_alog_ys = ir.get_alog_y()
# print('ir_alog_ys', ir_alog_ys)

for idx, ft_result in enumerate(ir_alog_ys):
    if ft_result == 0:
        raise SystemExit("filtered result: 0")
    else:
        i_r = ir_alog_ys[idx] * math.pow(TNT_EQ_WT, 0.3333)
        i_r = round(i_r, 3)
        if idx == 0:
            print('Ir(air): ', i_r)
        else:
            print('Ir(surface)', i_r)
'''
    get U
'''

obj_u = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        -0.214362789151,
        1.35034249993
    ],
    'const_u_surface': [
        -0.2024225716178,
        1.37784223635
    ],

    'list_slope_u_air': [
        -0.650507560471,
        0.291320654009,
        0.307916322787,
        -0.183361123489,
        -0.197740454538,
        0.0909119559768,
        0.098926178054,
        -0.0287370990248,
        -0.0248730221702,
        0.00496311705671,
        0.00372242076361,
        -0.0003533736952,
        -0.0002292913709
    ],

    'list_slope_u_surface': [
        -0.698029762594,
        0.158916781906,
        0.4438112098136,
        -0.113402023921,
        -0.369887075049,
        0.129230567449,
        0.19857981197,
        -0.0867636217397,
        -0.0620391900135,
        0.0307482926566,
        0.0102657234407,
        -0.00546533250772,
        -0.000693180974,
        0.0003847494916
    ],

    'const_y': [
        -0.144615443471,
        -0.06621072854
    ],

    'limits': [
        {
            'lower_limit': 0.0531,
            'upper_limit': 40
        },
        {
            'lower_limit': 0.0674,
            'upper_limit': 40
        }
    ]
}

u = Param(obj_u)
u_ft_result = u.get_ft_results()
# print('u_ft_result', u_ft_result)
u_alog_ys = u.get_alog_y()
# print('u_alog_ys', u_alog_ys)

for idx, ft_result in enumerate(u_alog_ys):
    if ft_result == 0:
        raise SystemExit("filtered result: 0")
    else:
        u = u_alog_ys[idx]
        u = round(u, 3)
        if idx == 0:
            print('U(air): ', u)
        else:
            print('U(surface)', u)
'''
    get Ta
'''

obj_ta = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        -0.253273111999,
        1.37407043777
    ],
    'const_u_surface': [
        -0.202425716178,
        1.37784223635
    ],

    'list_slope_u_air': [
        1.36456871214,
        -0.0570035692784,
        -0.182832224796,
        0.0118851436014,
        0.0432648687627,
        -0.0007997367834,
        -0.00436073555033
    ],

    'list_slope_u_surface': [
        1.35706496258,
        0.052492798645,
        -0.196563954086,
        -0.0601770052288,
        0.0696360270891,
        0.0215297490092,
        -0.0161658930785,
        -0.00232531970294,
        0.00147752067524
    ],

    'const_y': [
        0.0720707787637,
        -0.0591634288046
    ],

    'limits': [
        {
            'lower_limit': 0.0531,
            'upper_limit': 40
        },
        {
            'lower_limit': 0.0674,
            'upper_limit': 40
        }
    ]
}

ta = Param(obj_ta)
ta_ft_result = ta.get_ft_results()
# print('ta_ft_result', ta_ft_result)
ta_alog_ys = ta.get_alog_y()
# print('ta_alog_ys', ta_alog_ys)

for idx, ft_result in enumerate(ta_alog_ys):
    if ft_result == 0:
        raise SystemExit("filtered result: 0")
    else:
        ta = ta_alog_ys[idx] * math.pow(TNT_EQ_WT, 0.3333)
        ta = round(ta, 3)
        if idx == 0:
            print('ta(air): ', ta)
        else:
            print('ta(surface)', ta)

# '''
#     get T+ F(I)
# '''

obj_tp_f1 = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        2.26367268496,
        5.11588554305
    ],
    'const_u_surface': [
        1.92946154068,
        5.25099193925
    ],

    'list_slope_u_air': [
        0.164953518069,
        0.127788499497,
        0.00291430135946,
        0.0018795744922,
        0.017341396254,
        0.0026973975804,
        -0.00361976502798,
        -0.00100926577934
    ],

    'list_slope_u_surface': [
        0.130143717675,
        0.134872511954,
        0.0391574276906,
        -0.00475933664702,
        -0.00428144598008
    ],

    'const_y': [
        -0.686608550419,
        -0.614227603559
    ],

    'limits': [
        {
            'lower_limit': 0.147,
            'upper_limit': 0.888
        },
        {
            'lower_limit': 0.178,
            'upper_limit': 1.01
        }
    ]
}

tp_f1 = Param(obj_tp_f1)
tp_f1_ft_result = tp_f1.get_ft_results()
# print('tp_f1_ft_result', tp_f1_ft_result)
tp_f1_alog_ys = tp_f1.get_alog_y()
# print('tp_f1_alog_ys', tp_f1_alog_ys)

# '''
#     get T+ F(II)
# '''

obj_tp_f2 = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        -1.33361206714,
        9.2996288611
    ],
    'const_u_surface': [
        -2.12492525216,
        9.2996288611
    ],

    'list_slope_u_air': [
        -0.0297944268969,
        0.0306329542941,
        0.018340557407,
        -0.0173964666286,
        -0.00106321963576,
        0.0056206003128,
        0.0001618217499,
        -0.0006860188944
    ],

    'list_slope_u_surface': [
        -0.0297944268976,
        0.030632954288,
        0.0183405574086,
        -0.0173964666211,
        -0.00106321963633,
        0.00562060030977,
        0.0001618217499,
        -0.0006860188944
    ],

    'const_y': [
        0.23031841078,
        0.315409245784
    ],

    'limits': [
        {
            'lower_limit': 0.888,
            'upper_limit': 2.28
        },
        {
            'lower_limit': 1.01,
            'upper_limit': 2.78
        }
    ]
}

tp_f2 = Param(obj_tp_f2)
tp_f2_ft_result = tp_f2.get_ft_results()
# print('tp_f2_ft_result', tp_f2_ft_result)
tp_f2_alog_ys = tp_f2.get_alog_y()
# print('tp_f2_alog_ys', tp_f2_alog_ys)

# '''
#     get T+ F(III)
# '''

obj_tp_f3 = {
    'sc_dist': sc_dist,
    'log_sc_dist': log_sc_dist,
    'const_u_air': [
        -3.13005805346,
        3.1524725364
    ],
    'const_u_surface': [
        -3.53626218091,
        3.46349745571
    ],

    'list_slope_u_air': [
        0.0967031995552,
        -0.00801302059667,
        0.00482705779732,
        0.00187587272287,
        0.00246738509321,
        -0.000841116668,
        0.0006193291052
    ],

    'list_slope_u_surface': [
        0.0933035304009,
        -0.0005849420883,
        0.0022688499501,
        -0.00295908591505,
        0.00148029868929
    ],

    'const_y': [
        0.621036276475,
        0.686906642409
    ],

    'limits': [
        {
            'lower_limit': 2.28,
            'upper_limit': 40
        },
        {
            'lower_limit': 2.78,
            'upper_limit': 40
        }
    ]
}

tp_f3 = Param(obj_tp_f3)
tp_f3_ft_result = tp_f3.get_ft_results()
# print('tp_f3_ft_result', tp_f3_ft_result)
tp_f3_alog_ys = tp_f3.get_alog_y()
# print('tp_f3_alog_ys', tp_f3_alog_ys)

sum_tp_f = []
idx_cnt = 0
t_p = []
while idx_cnt < 2:
    sum_tp_f.append(tp_f1_alog_ys[idx_cnt] + tp_f2_alog_ys[idx_cnt] + tp_f3_alog_ys[idx_cnt])
    if sum_tp_f[idx_cnt] == 0:
        raise SystemExit("ERROR: sum of Is anti log y are 0")
    else:
        tps = sum_tp_f[idx_cnt] * math.pow(TNT_EQ_WT, 0.3333)
        tps = round(tps, 3)
        if idx_cnt == 0:
            print('T+ F (air): ', round(tps, 3))
        else:
            print('T+ F (surface): ', round(tps, 3))
        t_p.append(tps)
    idx_cnt = idx_cnt + 1
# print('Tp', t_p)
