def score_analysis(formula, score):
    '''Returns the grade levels corresponding to a score for each formula'''
    formula_scales = [['lix',60,56,44,36,32,28,24],
                  ['rix',8,7.2,4.5,3.0,2.4,1.8,1.3],
                  ['fkgl',16,13,10,8,7,6,5],
                  ['gunning',16,13,10,8,7,6,5],
                  ['smog',16,13,10,8,7,6,5],
                  ['ari',16,13,10,8,7,6,5],
                  ['coleman_liau',17,13,12,10,7,6,5]]
    for x in range(len(formula_scales)):
        for y in range(len(formula_scales)):
            if formula_scales[x][y] == formula :
                if score > formula_scales[x][y+1]:
                    return "Très difficile (>Bac+3)"
                elif score >= formula_scales[x][y+2]:
                    return "Difficile (Bac+3)"
                elif score >= formula_scales[x][y+3]:
                    return "Plutôt difficile (lycée)"
                elif score >= formula_scales[x][y+4]:
                    return "Standard (4e-3e)"
                elif score >= formula_scales[x][y+5]:
                    return "Plutôt facile (5e)"
                elif score >= formula_scales[x][y+6]:
                    return "Facile (6e)"
                elif score >= formula_scales[x][y+7]:
                    return "Très facile (CM2)"
                else:
                    return "Extrêmement facile (>CM1)"