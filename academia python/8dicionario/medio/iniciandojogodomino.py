# def inicia_jogo(n, ldistribuidas):
#     pecas = n * 7
#     i = 0
#     dic = {}
#     dic['jogadores'] = {}
#     dic['monte'] = []
#     dic['mesa'] = []
#     ljog = []
#     lmmonte = []

#     while i < pecas:
#         ljog.append(ldistribuidas[i])
        
#         if i == 6:
#             dic['jogadores'][0] = ljog
#             ljog.clear()
#         if i == 13:
#             dic['jogadores'][1] = ljog
#         i+=1

#     return dic

def inicia_jogo(n, lpecas):
    dic = {}
    dic['jogadores'] = {}
    dic['monte'] = []
    dic['mesa'] = []

    for i in range(n):
        dic['jogadores'][i] = lpecas[i*7 : (i+1)*7]

    dic['monte'] = lpecas[n * 7:]
    return dic


p = [
	[1,3],[0,1],[4,6],[0,3],[0,4],[6,6],[0,6],
	[1,1],[1,2],[0,0],[1,4],[1,5],[1,6],[2,2],
	[3,6],[2,4],[2,5],[2,6],[3,3],[3,4],[2,3],
	[3,5],[4,4],[4,5],[0,2],[5,5],[5,6],[0,5]
]
print(inicia_jogo(4, p))


